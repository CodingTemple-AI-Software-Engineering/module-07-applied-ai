"""
L7 — Course Content Search  (SOLUTION)
=======================================
Run with:
    python solution.py
"""

from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# ── Knowledge base ────────────────────────────────────────────────────────────
sentences = [
    # Module 1 — AI Fundamentals
    "Large language models are trained on massive text datasets to predict the next token.",
    "Prompt engineering shapes how a language model interprets and responds to a request.",
    "Temperature controls the randomness of a model's output; lower values are more deterministic.",
    # Module 2 — Advanced Python
    "List comprehensions provide a concise way to create lists from iterables in Python.",
    "Decorators in Python wrap functions to extend their behaviour without modifying the original code.",
    "Context managers using 'with' ensure resources like files are properly opened and closed.",
    # Module 3 — Databases & SQL
    "SQL JOIN combines rows from two or more tables based on a related column.",
    "An index in a database speeds up SELECT queries at the cost of slower writes.",
    "Transactions guarantee that a group of SQL operations either all succeed or all fail.",
    # Module 4 — REST API Fundamentals
    "REST APIs communicate over HTTP using verbs like GET, POST, PUT, and DELETE.",
    "A 404 status code means the requested resource was not found on the server.",
    "JSON is the standard data format for sending and receiving data in REST APIs.",
    # Module 5 — FastAPI
    "FastAPI automatically validates request data and generates OpenAPI docs from type hints.",
    "Pydantic models define the shape and validation rules for request and response bodies.",
    "Dependency injection in FastAPI lets you share database sessions and other resources across routes.",
    # Module 6 — Streamlit
    "Streamlit re-runs the entire script from top to bottom whenever a widget is interacted with.",
    "st.session_state persists values across re-runs so user actions are not lost.",
    "st.cache_resource caches expensive objects like database connections and ML models.",
    # Module 7 — Embeddings & Retrieval
    "Embeddings are dense numeric vectors that capture the semantic meaning of text.",
    "Cosine similarity measures the angle between two vectors; a score of 1.0 means identical direction.",
    "ChromaDB is a vector database that stores embeddings and supports similarity search.",
    "Chunking splits long documents into smaller pieces so each embedding stays focused.",
    "RAG — Retrieval-Augmented Generation — grounds an LLM's answer in retrieved documents.",
]

# ── Model ─────────────────────────────────────────────────────────────────────
print("Loading model...")
model = SentenceTransformer("all-MiniLM-L6-v2")

# ── Encode knowledge base ─────────────────────────────────────────────────────
print(f"Embedding {len(sentences)} sentences...")
doc_embeddings = model.encode(sentences)

# ── Search loop ───────────────────────────────────────────────────────────────
print("\nSemantic Search — type 'quit' to exit\n")

while True:
    query = input("Search: ").strip()

    if query.lower() == "quit":
        break

    if not query:
        continue

    query_embedding = model.encode([query])
    scores = cosine_similarity(query_embedding, doc_embeddings)[0]
    top_indices = np.argsort(scores)[::-1][:3]

    print("\nTop 3 results:")
    for rank, idx in enumerate(top_indices, 1):
        print(f"  {rank}. [{scores[idx]:.4f}] {sentences[idx]}")
    print()
