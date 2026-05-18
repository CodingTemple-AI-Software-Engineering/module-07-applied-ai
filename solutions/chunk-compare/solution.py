"""
L7 — Chunk and Compare  (SOLUTION)
=====================================
Run with:
    python solution.py
"""

from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# ── Document ──────────────────────────────────────────────────────────────────
DOCUMENT = """
Python Fundamentals

Python is a high-level, interpreted programming language known for its clean, readable syntax.
Variables in Python are dynamically typed — you don't need to declare a type before assigning a value.
Python uses indentation instead of braces to define code blocks, making structure visually obvious.
Functions are defined with the def keyword and can accept positional, keyword, and default arguments.
List comprehensions offer a concise way to transform or filter sequences in a single readable line.

Object-Oriented Programming in Python

Classes encapsulate data and behaviour together into reusable blueprints.
The __init__ method runs when a new instance is created and sets up its initial state.
Inheritance lets a child class reuse and extend the attributes and methods of a parent class.
Dunder methods like __str__ and __repr__ control how objects are displayed and compared.
Decorators such as @property let you expose computed attributes without calling a method explicitly.

REST APIs and FastAPI

REST APIs communicate over HTTP using verbs: GET to read, POST to create, PUT to update, DELETE to remove.
HTTP status codes signal outcomes — 200 OK, 201 Created, 400 Bad Request, 404 Not Found, 500 Server Error.
FastAPI is a modern Python framework that generates OpenAPI documentation automatically from type hints.
Pydantic models define the shape and validation rules for request and response bodies in FastAPI.
Dependency injection in FastAPI allows shared resources like database connections to be reused across routes.
Path parameters are captured directly from the URL, while query parameters are read from the query string.

Databases and SQL

SQL is the standard language for querying relational databases using tables, rows, and columns.
A SELECT statement retrieves data, a WHERE clause filters rows, and ORDER BY sorts the results.
JOIN combines rows from multiple tables based on a matching key, such as a foreign key relationship.
An index on a frequently queried column speeds up SELECT at the cost of slower INSERT and UPDATE.
Transactions group multiple SQL operations so they either all succeed (COMMIT) or all fail (ROLLBACK).

Embeddings and Semantic Search

An embedding is a dense numeric vector that captures the semantic meaning of text.
The sentence-transformers library provides pre-trained models that convert sentences to 384-dimensional vectors.
Cosine similarity measures the angle between two vectors — a score of 1.0 means perfect semantic alignment.
ChromaDB is a vector database that stores embeddings and supports fast approximate nearest-neighbour search.
Chunking splits long documents into smaller pieces so each embedding remains semantically focused on one idea.
Retrieval-Augmented Generation (RAG) retrieves relevant chunks and feeds them as context to a language model.
"""

# ── Chunking functions ────────────────────────────────────────────────────────
def fixed_size_chunks(text: str, size: int = 300, overlap: int = 50) -> list[str]:
    """Split text into fixed-size chunks with overlap."""
    chunks = []
    start = 0
    while start < len(text):
        chunks.append(text[start:start + size])
        start += size - overlap
    return chunks


def paragraph_chunks(text: str) -> list[str]:
    """Split text on double newlines, discarding empty paragraphs."""
    return [p.strip() for p in text.split("\n\n") if p.strip()]


# ── Model & embeddings ────────────────────────────────────────────────────────
print("Loading model...")
model = SentenceTransformer("all-MiniLM-L6-v2")

fixed_chunks = fixed_size_chunks(DOCUMENT)
para_chunks  = paragraph_chunks(DOCUMENT)

print(f"Fixed-size chunks : {len(fixed_chunks)}")
print(f"Paragraph chunks  : {len(para_chunks)}")

fixed_embeddings = model.encode(fixed_chunks)
para_embeddings  = model.encode(para_chunks)


# ── Search helper ─────────────────────────────────────────────────────────────
def search_chunks(query: str, chunks: list[str], embeddings, n: int = 2):
    """Return top-n (score, chunk) pairs for a query."""
    query_emb = model.encode([query])
    scores    = cosine_similarity(query_emb, embeddings)[0]
    top_idx   = np.argsort(scores)[::-1][:n]
    return [(scores[i], chunks[i]) for i in top_idx]


# ── Test queries ──────────────────────────────────────────────────────────────
queries = [
    "How does FastAPI validate incoming request data?",
    "What is the purpose of database indexes?",
    "How do embeddings capture the meaning of text?",
]

# ── Compare results ───────────────────────────────────────────────────────────
for query in queries:
    print(f'\n{"="*60}')
    print(f'Query: "{query}"')

    print("\n  [Fixed-size chunks]")
    for score, chunk in search_chunks(query, fixed_chunks, fixed_embeddings):
        preview = chunk.replace("\n", " ").strip()[:120]
        print(f"    [{score:.4f}] {preview}...")

    print("\n  [Paragraph chunks]")
    for score, chunk in search_chunks(query, para_chunks, para_embeddings):
        preview = chunk.replace("\n", " ").strip()[:120]
        print(f"    [{score:.4f}] {preview}...")

# ── Analysis ──────────────────────────────────────────────────────────────────
print("\n" + "="*60)
print("ANALYSIS")
print("""
Paragraph chunking tends to return more focused, semantically complete results
because each paragraph covers a single topic. The embeddings capture the full
idea of the paragraph rather than a fragment.

Fixed-size chunking sometimes cuts mid-sentence, which can produce chunks that
mix topics. This causes the embedding to be "diluted" between two ideas, making
it harder to match a specific query precisely.

However, fixed-size chunking with overlap prevents any single idea from being
split across two chunks without any shared context. This can be useful for very
long paragraphs that would otherwise produce one oversized embedding.

When to choose each strategy:
  - Paragraph chunks: structured documents with clear paragraph breaks (articles,
    documentation, course notes).
  - Fixed-size chunks with overlap: unstructured text, transcripts, or documents
    where paragraph boundaries are unreliable.
""")
