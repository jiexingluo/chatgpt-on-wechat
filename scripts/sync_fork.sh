#!/usr/bin/env bash
set -euo pipefail

REPO_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
LOG_FILE="${REPO_DIR}/sync_fork.log"

cd "${REPO_DIR}"

{
  echo "[$(date '+%Y-%m-%d %H:%M:%S')] sync start"

  if [[ -n "$(git status --porcelain)" ]]; then
    echo "working tree is dirty, skip sync"
    exit 0
  fi

  git fetch origin --prune
  git fetch upstream --prune
  git checkout main

  if ! git merge --no-edit upstream/master; then
    echo "merge conflict detected, abort merge"
    git merge --abort || true
    exit 1
  fi

  git push origin main
  echo "sync complete"
} >> "${LOG_FILE}" 2>&1
