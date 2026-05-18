# Personal Knowledge Base

**Module:** 7 — Applied AI: Embeddings & Retrieval
**Estimated time:** 30 minutes

## Objective

Build a persistent ChromaDB knowledge base with course content, demonstrating the full add-and-query workflow including metadata filtering.

## What You'll Build

A script that creates a persistent ChromaDB collection called `"my_knowledge"`, adds 15+ documents with module and topic metadata, and runs three test queries — one broad, one filtered to a specific module, and one where the query uses different words than the stored documents.

## Reference Code

The starter file (`starter.py`) provides a scaffold with TODOs — fill in each section, then compare with the solution.

## Running

```bash
python starter.py
```

## Deliverable

A working `starter.py` that creates a persistent ChromaDB collection, adds 15+ documents with metadata, and demonstrates both unfiltered and filtered semantic search.
