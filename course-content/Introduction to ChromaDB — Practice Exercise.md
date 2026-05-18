# Introduction to ChromaDB — Practice Exercise

## Personal Knowledge Base

**Objective:** Build a persistent ChromaDB knowledge base with content from this course, demonstrating the full add-and-query workflow with metadata filtering.

**Time:** 30 minutes

**What you’ll do:**

1. Create a file called `knowledge_base.py`
2. Create a **persistent** ChromaDB client (data survives restarts)
3. Create a collection called `"my_knowledge"`
4. Add at least **15 documents** covering content from at least 3 different modules you’ve completed. Each document should include:
    - A unique ID
    - The text content (a sentence or short paragraph summarizing a concept)
    - Metadata with at least: `module` (which module it’s from) and `topic` (general category like "api", "database", "frontend", "ai")
5. Implement a search function that:
    - Accepts a query string and an optional module filter
    - Returns the top 5 results with distances and metadata
6. Run at least **3 test queries:**
    - One broad query (no filter)
    - One filtered to a specific module
    - One where the query uses completely different words than the stored documents

**Deliverable:** A working `knowledge_base.py` that creates a persistent ChromaDB collection, adds 15+ documents with metadata, and demonstrates both unfiltered and filtered search.

**Hints:**

- Use `client.get_or_create_collection()` so the script works on repeated runs
- Use `collection.upsert()` instead of `collection.add()` to handle re-runs without ID conflicts
- The `where` parameter for filtering uses the format: `where={"module": "5"}`

**Why this exercise?** You’re building the exact storage and retrieval pattern used in the module project. The knowledge base you create here could evolve into a real study tool.