"""
L7 — Evaluate Your Search System  (SOLUTION)
==============================================
Run with:
    python solution.py

Uses an in-memory ChromaDB client — no files are created.
"""

import chromadb

# ── Documents ─────────────────────────────────────────────────────────────────
ids = [
    "doc_01", "doc_02", "doc_03", "doc_04",
    "doc_05", "doc_06", "doc_07", "doc_08",
    "doc_09", "doc_10", "doc_11", "doc_12",
]

documents = [
    # FastAPI / REST APIs
    "FastAPI uses Pydantic models to validate incoming request bodies and return clear 422 errors.",
    "Path parameters are extracted from the URL path; query parameters come from the query string.",
    "FastAPI dependency injection lets you share database sessions and auth checks across routes.",
    "REST uses HTTP verbs: GET retrieves data, POST creates resources, PUT updates, DELETE removes.",

    # Databases / SQL
    "An SQL index on a frequently queried column dramatically speeds up SELECT performance.",
    "Transactions ensure a group of SQL operations either all commit or all roll back together.",
    "SQL JOIN combines rows from two tables where a foreign key matches a primary key.",

    # Embeddings and semantic search
    "Embeddings are dense numeric vectors that represent text meaning in a high-dimensional space.",
    "Cosine similarity measures the angle between two embedding vectors; 1.0 means identical direction.",
    "ChromaDB stores embeddings and supports approximate nearest-neighbour queries over large corpora.",

    # Streamlit
    "Streamlit re-runs the entire Python script whenever a user interacts with any widget.",
    "st.session_state persists values across script re-runs within a single user session.",
]

metadatas = [
    {"topic": "api"}, {"topic": "api"}, {"topic": "api"}, {"topic": "api"},
    {"topic": "database"}, {"topic": "database"}, {"topic": "database"},
    {"topic": "embeddings"}, {"topic": "embeddings"}, {"topic": "embeddings"},
    {"topic": "streamlit"}, {"topic": "streamlit"},
]

# ── ChromaDB setup ────────────────────────────────────────────────────────────
client     = chromadb.EphemeralClient()
collection = client.get_or_create_collection("eval_collection")
collection.upsert(ids=ids, documents=documents, metadatas=metadatas)

# ── Evaluation set ────────────────────────────────────────────────────────────
eval_set = [
    {"query": "How does FastAPI validate request data?",               "relevant_ids": ["doc_01", "doc_03"]},
    {"query": "What HTTP verbs does REST use?",                        "relevant_ids": ["doc_04"]},
    {"query": "How do database indexes improve query performance?",    "relevant_ids": ["doc_05"]},
    {"query": "How do I make multiple SQL changes safe and atomic?",   "relevant_ids": ["doc_06"]},
    {"query": "What are embeddings and how do they represent text?",   "relevant_ids": ["doc_08", "doc_09"]},
    {"query": "How do I keep a counter alive between page reloads in Streamlit?", "relevant_ids": ["doc_12"]},
]


# ── Evaluation function ───────────────────────────────────────────────────────
def evaluate(n_results: int, distance_threshold: float = None):
    """
    Run every query in eval_set, compute precision and recall for each,
    and print per-query results plus averages.
    """
    print(f"\n=== Evaluation: n_results={n_results}, threshold={distance_threshold} ===")

    precisions = []
    recalls    = []

    for i, entry in enumerate(eval_set, 1):
        query        = entry["query"]
        relevant_ids = set(entry["relevant_ids"])

        results = collection.query(
            query_texts=[query],
            n_results=n_results,
            include=["ids", "distances"],
        )

        retrieved_ids  = results["ids"][0]
        retrieved_dists = results["distances"][0]

        # Apply distance threshold if specified
        if distance_threshold is not None:
            retrieved_ids = [
                doc_id
                for doc_id, dist in zip(retrieved_ids, retrieved_dists)
                if dist <= distance_threshold
            ]

        overlap   = len(relevant_ids & set(retrieved_ids))
        precision = overlap / len(retrieved_ids) if retrieved_ids else 0.0
        recall    = overlap / len(relevant_ids)  if relevant_ids  else 0.0

        precisions.append(precision)
        recalls.append(recall)

        print(
            f"  Query {i}: P={precision*100:.1f}%  R={recall*100:.1f}%"
            f"  | '{query[:55]}'"
        )

    avg_p = sum(precisions) / len(precisions) if precisions else 0
    avg_r = sum(recalls)    / len(recalls)    if recalls    else 0
    print(f"  AVERAGE : P={avg_p*100:.1f}%  R={avg_r*100:.1f}%")
    return avg_p, avg_r


# ── Run at 3 settings ─────────────────────────────────────────────────────────
evaluate(n_results=3)
evaluate(n_results=5)
evaluate(n_results=5, distance_threshold=0.6)

# ── Analysis ──────────────────────────────────────────────────────────────────
print("\n=== ANALYSIS ===")
print("""
Queries that performed well:
  - Queries closely matching the vocabulary of the stored documents (e.g. "FastAPI validate
    request data") returned high precision and recall even at n_results=3.

Queries that struggled:
  - The Streamlit session_state query ("keep a counter alive between page reloads") uses
    different vocabulary than doc_12. Recall improves when n_results is increased because
    the relevant document eventually surfaces in a larger candidate set.

Effect of increasing n_results:
  - Going from 3 → 5 raises recall (more relevant docs retrieved) but can lower precision
    (more irrelevant docs included). This is the classic precision–recall trade-off.

Effect of distance_threshold:
  - Applying a threshold of 0.6 removes low-confidence results, which can improve precision
    at the cost of recall — relevant documents with weaker embedding overlap get filtered out.

Improvements:
  - Better document coverage (more docs per topic) would raise recall.
  - Hybrid search (keyword + vector) would help queries with out-of-vocabulary terms.
  - Query expansion or rewriting could bridge vocabulary gaps.
""")
