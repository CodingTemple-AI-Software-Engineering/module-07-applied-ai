"""
L7 — Personal Knowledge Base  (SOLUTION)
=========================================
Run with:
    python solution.py

Creates a persistent ChromaDB collection under ./chroma_db/
"""

import chromadb

# ── Client & collection ───────────────────────────────────────────────────────
client = chromadb.PersistentClient(path="./chroma_db")
collection = client.get_or_create_collection("my_knowledge")

# ── Documents ─────────────────────────────────────────────────────────────────
ids = [
    "doc_01", "doc_02", "doc_03", "doc_04", "doc_05",
    "doc_06", "doc_07", "doc_08", "doc_09", "doc_10",
    "doc_11", "doc_12", "doc_13", "doc_14", "doc_15",
]

documents = [
    # Module 1 — AI Fundamentals
    "Large language models are pre-trained on internet text and fine-tuned to follow instructions.",
    "Tokens are the units an LLM processes; a token is roughly 4 characters or ¾ of a word.",
    "Temperature controls randomness in model outputs: 0 is deterministic, 1 is creative.",

    # Module 3 — Databases
    "SQL SELECT with JOIN retrieves related rows from multiple tables based on matching keys.",
    "An index on a frequently queried column dramatically speeds up SELECT statements.",
    "Transactions use COMMIT and ROLLBACK to ensure groups of operations are atomic.",

    # Module 4 — REST APIs
    "REST uses HTTP verbs: GET to read, POST to create, PUT to update, DELETE to remove.",
    "Status codes communicate outcomes: 200 OK, 201 Created, 400 Bad Request, 404 Not Found.",
    "Authentication tokens like JWTs are passed in the Authorization header of HTTP requests.",

    # Module 5 — FastAPI
    "FastAPI generates interactive OpenAPI documentation automatically from route definitions.",
    "Pydantic BaseModel validates incoming JSON bodies and returns clear error messages on failure.",
    "Background tasks in FastAPI run after a response is returned, keeping endpoints fast.",

    # Module 6 — Streamlit
    "Streamlit re-runs the entire script from top to bottom on every widget interaction.",
    "st.session_state stores values that persist across script re-runs within a user session.",
    "st.cache_resource caches objects like ML models so they are only loaded once.",
]

metadatas = [
    {"module": "1", "topic": "ai"},
    {"module": "1", "topic": "ai"},
    {"module": "1", "topic": "ai"},
    {"module": "3", "topic": "database"},
    {"module": "3", "topic": "database"},
    {"module": "3", "topic": "database"},
    {"module": "4", "topic": "api"},
    {"module": "4", "topic": "api"},
    {"module": "4", "topic": "api"},
    {"module": "5", "topic": "api"},
    {"module": "5", "topic": "api"},
    {"module": "5", "topic": "api"},
    {"module": "6", "topic": "frontend"},
    {"module": "6", "topic": "frontend"},
    {"module": "6", "topic": "frontend"},
]

collection.upsert(ids=ids, documents=documents, metadatas=metadatas)
print(f"Collection '{collection.name}' ready — {collection.count()} documents.\n")


# ── Search function ───────────────────────────────────────────────────────────
def search(query: str, module_filter: str = None, n_results: int = 5):
    """Return top results for query, optionally filtered to a specific module."""
    where = {"module": module_filter} if module_filter else None

    results = collection.query(
        query_texts=[query],
        n_results=n_results,
        where=where,
    )

    ids_     = results["ids"][0]
    docs_    = results["documents"][0]
    metas_   = results["metadatas"][0]
    dists_   = results["distances"][0]

    for rank, (doc_id, doc, meta, dist) in enumerate(
        zip(ids_, docs_, metas_, dists_), 1
    ):
        print(f"  {rank}. [{dist:.4f}] (module {meta['module']}, {meta['topic']})")
        print(f"       {doc}")
    print()


# ── Test queries ──────────────────────────────────────────────────────────────
print("=== Broad search (no filter) ===")
search("How does data validation work when building an API?")

print("=== Filtered to Module 3 (databases) ===")
search("How do I make queries faster?", module_filter="3")

print("=== Different words than stored documents ===")
search("What keeps user choices alive between page loads in a web app?")
