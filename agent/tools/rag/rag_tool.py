"""
RAG Search Tool

Allows agents to search an external local knowledge base using semantic and keyword search.
"""

import os
from pathlib import Path
from typing import Dict, Any, Optional
import asyncio

from agent.tools.base_tool import BaseTool, ToolResult
from agent.memory.manager import MemoryManager
from agent.memory.config import MemoryConfig, get_default_memory_config


class RagSearchTool(BaseTool):
    """Tool for searching an external local knowledge base"""
    
    name: str = "rag_search"
    description: str = (
        "Search the external local knowledge base for factual information, documents, and reference material. "
        "Use this tool when you need to answer questions based on the user's uploaded knowledge base files."
    )
    params: dict = {
        "type": "object",
        "properties": {
            "query": {
                "type": "string",
                "description": "Search query to find relevant information in the knowledge base"
            },
            "max_results": {
                "type": "integer",
                "description": "Maximum number of results to return (default: 5)",
                "default": 5
            }
        },
        "required": ["query"]
    }
    
    def __init__(self):
        super().__init__()
        
        # Get base workspace from global config, but point to a specific knowledge_base folder
        base_config = get_default_memory_config()
        # Default to ./knowledge_base if we can find the project root, else use current dir
        # In this project, tools are located in `agent/tools/rag/rag_tool.py`
        # So project root is three levels up
        project_root = Path(__file__).resolve().parent.parent.parent.parent
        kb_path = project_root / "knowledge_base"
        
        # Create a specific config for knowledge base
        self.kb_config = MemoryConfig(
            workspace_root=str(kb_path),
            embedding_provider=base_config.embedding_provider,
            embedding_model=base_config.embedding_model,
            embedding_dim=base_config.embedding_dim,
            chunk_max_tokens=800,  # Slightly larger chunks for KB
            chunk_overlap_tokens=100,
            max_results=5,
            min_score=0.1
        )
        
        # Ensure the directory exists
        os.makedirs(kb_path / "memory", exist_ok=True)
        
        # Initialize custom embedding provider if needed
        from agent.memory.embedding import create_embedding_provider
        from config import conf
        
        api_key = conf().get("open_ai_api_key", os.environ.get("OPENAI_API_KEY"))
        api_base = conf().get("open_ai_api_base", os.environ.get("OPENAI_API_BASE"))
        
        embedding_provider = None
        if api_key:
            try:
                embedding_provider = create_embedding_provider(
                    provider=self.kb_config.embedding_provider,
                    model=self.kb_config.embedding_model,
                    api_key=api_key,
                    api_base=api_base
                )
            except Exception as e:
                from common.log import logger
                logger.warning(f"[RagSearchTool] Failed to initialize embedding provider: {e}")
        
        # Initialize memory manager for knowledge base
        self.memory_manager = MemoryManager(
            config=self.kb_config,
            embedding_provider=embedding_provider
        )
        
    def execute(self, args: dict):
        """
        Execute RAG search
        
        Args:
            args: Dictionary with query and max_results
            
        Returns:
            ToolResult with formatted search snippets
        """
        query = args.get("query")
        max_results = args.get("max_results", 5)
        
        if not query:
            return ToolResult.fail("Error: query parameter is required")
            
        try:
            # First, force sync to ingest any new files the user dropped in
            asyncio.run(self.memory_manager.sync())
            
            # Then perform the search
            results = asyncio.run(self.memory_manager.search(
                query=query,
                max_results=max_results,
                include_shared=True
            ))
            
            if not results:
                return ToolResult.success(
                    f"No relevant information found in the knowledge base for '{query}'.\n"
                    f"Tip: Ensure documents (.md, .txt) are placed in the '{self.kb_config.get_workspace()}/memory' directory."
                )
                
            # Format results
            output = [f"Found {len(results)} relevant snippets across the knowledge base:\n"]
            
            for i, result in enumerate(results, 1):
                # Only show filename, not full path to keep it clean
                filename = Path(result.path).name
                output.append(f"--- Result {i} (from: {filename}) [Relevance: {result.score:.2f}] ---")
                output.append(result.snippet.strip())
                output.append("")
                
            return ToolResult.success("\n".join(output))
            
        except Exception as e:
            from common.log import logger
            logger.error(f"Error in rag_search: {e}")
            return ToolResult.fail(f"Error querying knowledge base: {str(e)}")
