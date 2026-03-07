"""
Embedding providers for memory

Supports OpenAI and local embedding models
"""

import hashlib
from abc import ABC, abstractmethod
from typing import List, Optional


class EmbeddingProvider(ABC):
    """Base class for embedding providers"""

    @abstractmethod
    def embed(self, text: str) -> List[float]:
        """Generate embedding for text"""
        pass

    @abstractmethod
    def embed_batch(self, texts: List[str]) -> List[List[float]]:
        """Generate embeddings for multiple texts"""
        pass
    
    @property
    @abstractmethod
    def dimensions(self) -> int:
        """Get embedding dimensions"""
        pass


class OpenAIEmbeddingProvider(EmbeddingProvider):
    """OpenAI compatible embedding provider using REST API
    
    Supports OpenAI, Moonshot, DashScope (阿里云百炼), and other OpenAI-compatible APIs
    """
    
    # Default model mappings for different providers
    DEFAULT_MODELS = {
        "openai": "text-embedding-3-small",
        "dashscope": "text-embedding-v3",
        "moonshot": "text-embedding-3-small",  # Moonshot may not support embedding
    }
    
    # Dimension mappings for different models
    MODEL_DIMENSIONS = {
        "text-embedding-3-small": 1536,
        "text-embedding-3-large": 3072,
        "text-embedding-v3": 1024,
        "text-embedding-v2": 1536,
        "text-embedding-v1": 1536,
    }
    
    def __init__(self, model: str = "text-embedding-3-small", api_key: Optional[str] = None, api_base: Optional[str] = None):
        """
        Initialize OpenAI compatible embedding provider
        
        Args:
            model: Model name (e.g., text-embedding-3-small, text-embedding-v3)
            api_key: API key
            api_base: Optional API base URL
        """
        self.api_key = api_key
        self.api_base = api_base or "https://api.openai.com/v1"
        
        # Auto-detect provider and adjust model if needed
        self.provider = self._detect_provider(self.api_base)
        self.model = self._resolve_model(model, self.provider)

        # Validate API key
        if not self.api_key or self.api_key in ["", "YOUR API KEY", "YOUR_API_KEY"]:
            raise ValueError("API key is not configured. Please check your API key settings.")

        # Set dimensions based on model
        self._dimensions = self.MODEL_DIMENSIONS.get(self.model, 1536)
        
        # Adjust API base for DashScope if needed
        if self.provider == "dashscope" and "compatible-mode" not in self.api_base:
            # Convert coding.dashscope.aliyuncs.com/v1 to dashscope.aliyuncs.com/compatible-mode/v1
            self.api_base = self.api_base.replace("coding.dashscope.aliyuncs.com", "dashscope.aliyuncs.com/compatible-mode")
            if not self.api_base.endswith("/v1"):
                self.api_base = self.api_base.rstrip("/") + "/v1"

    def _detect_provider(self, api_base: str) -> str:
        """Detect provider from API base URL"""
        api_base_lower = api_base.lower()
        if "dashscope" in api_base_lower or "aliyun" in api_base_lower:
            return "dashscope"
        elif "moonshot" in api_base_lower:
            return "moonshot"
        elif "openai" in api_base_lower:
            return "openai"
        return "openai"  # Default to openai compatible
    
    def _resolve_model(self, model: str, provider: str) -> str:
        """Resolve model name based on provider"""
        # If model is default but provider needs different model, use provider's default
        if model == "text-embedding-3-small" and provider in self.DEFAULT_MODELS:
            return self.DEFAULT_MODELS[provider]
        return model

    def _call_api(self, input_data):
        """Call embedding API using requests"""
        import requests

        url = f"{self.api_base}/embeddings"
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}"
        }
        data = {
            "input": input_data,
            "model": self.model
        }

        try:
            response = requests.post(url, headers=headers, json=data, timeout=10)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.ConnectionError as e:
            raise ConnectionError(f"Failed to connect to API at {url}. Please check your network connection and api_base configuration. Error: {str(e)}")
        except requests.exceptions.Timeout as e:
            raise TimeoutError(f"API request timed out after 10s. Please check your network connection. Error: {str(e)}")
        except requests.exceptions.HTTPError as e:
            if e.response.status_code == 401:
                raise ValueError(f"Invalid API key. Please verify your API key is correct.")
            elif e.response.status_code == 404:
                raise ValueError(f"Model '{self.model}' not found at {url}. For DashScope, use 'text-embedding-v3'. Error: {e.response.text}")
            elif e.response.status_code == 429:
                raise ValueError(f"API rate limit exceeded. Please try again later.")
            else:
                raise ValueError(f"API request failed: {e.response.status_code} - {e.response.text}")

    def embed(self, text: str) -> List[float]:
        """Generate embedding for text"""
        result = self._call_api(text)
        return result["data"][0]["embedding"]

    def embed_batch(self, texts: List[str]) -> List[List[float]]:
        """Generate embeddings for multiple texts"""
        if not texts:
            return []

        result = self._call_api(texts)
        return [item["embedding"] for item in result["data"]]

    @property
    def dimensions(self) -> int:
        return self._dimensions


# LocalEmbeddingProvider removed - only use OpenAI embedding or keyword search


class EmbeddingCache:
    """Cache for embeddings to avoid recomputation"""

    def __init__(self):
        self.cache = {}

    def get(self, text: str, provider: str, model: str) -> Optional[List[float]]:
        """Get cached embedding"""
        key = self._compute_key(text, provider, model)
        return self.cache.get(key)
    
    def put(self, text: str, provider: str, model: str, embedding: List[float]):
        """Cache embedding"""
        key = self._compute_key(text, provider, model)
        self.cache[key] = embedding
    
    @staticmethod
    def _compute_key(text: str, provider: str, model: str) -> str:
        """Compute cache key"""
        content = f"{provider}:{model}:{text}"
        return hashlib.md5(content.encode('utf-8')).hexdigest()
    
    def clear(self):
        """Clear cache"""
        self.cache.clear()


def create_embedding_provider(
    provider: str = "openai",
    model: Optional[str] = None,
    api_key: Optional[str] = None,
    api_base: Optional[str] = None
) -> EmbeddingProvider:
    """
    Factory function to create embedding provider
    
    Only supports OpenAI embedding via REST API.
    If initialization fails, caller should fall back to keyword-only search.
    
    Args:
        provider: Provider name (only "openai" is supported)
        model: Model name (default: text-embedding-3-small)
        api_key: OpenAI API key (required)
        api_base: API base URL (default: https://api.openai.com/v1)
        
    Returns:
        EmbeddingProvider instance
        
    Raises:
        ValueError: If provider is not "openai" or api_key is missing
    """
    if provider != "openai":
        raise ValueError(f"Only 'openai' provider is supported, got: {provider}")

    model = model or "text-embedding-3-small"
    return OpenAIEmbeddingProvider(model=model, api_key=api_key, api_base=api_base)
