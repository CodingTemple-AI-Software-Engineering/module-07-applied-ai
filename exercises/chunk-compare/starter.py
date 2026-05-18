"""
L7 — Chunk and Compare  (STARTER)
===================================
Run with:
    python starter.py

Your goal: implement two chunking strategies, embed both sets of chunks, run
the same queries against each, and compare results.

Required features:
    1. A document of at least 500 words (paste your own notes or write a
       multi-paragraph summary of course concepts)
    2. Fixed-size chunking: 300-character chunks, 50-character overlap
    3. Paragraph-based chunking: split on double newlines (\n\n)
    4. Embed all chunks from both strategies
    5. Run 3 different queries against both sets
    6. For each query display the top 2 results from each strategy with scores
    7. A written analysis at the end (as print statements)

Key concepts:
    Fixed-size chunking with overlap:
        chunks = []
        start = 0
        while start < len(text):
            chunks.append(text[start:start + chunk_size])
            start += chunk_size - overlap

    Paragraph-based chunking:
        chunks = [p.strip() for p in text.split("\\n\\n") if p.strip()]

    Searching a list of embedded chunks:
        scores = cosine_similarity(query_emb, chunk_embeddings)[0]
        top_idx = np.argsort(scores)[::-1][:n]
"""

from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# ── Document ─────────────────────────────────────────────────────────────────
# TODO: Paste or write a 500–800 word document here.
#       It should cover multiple distinct topics so different chunks are
#       retrievable. You can use course notes from Modules 1–6.

DOCUMENT = """
TODO: replace this with your document text (at least 500 words, multiple paragraphs).
"""

# ── Chunking functions ───────────────────────────────────────────────────────
def fixed_size_chunks(text: str, size: int = 300, overlap: int = 50) -> list[str]:
    """Split text into fixed-size chunks with overlap."""
    # TODO: implement the sliding-window approach described above
    chunks = []
    # ...
    return chunks


def paragraph_chunks(text: str) -> list[str]:
    """Split text on double newlines, discarding empty paragraphs."""
    # TODO: split on "\n\n", strip each piece, filter empty strings
    return []


# ── Model & embeddings ───────────────────────────────────────────────────────
print("Loading model...")
# TODO: Load SentenceTransformer('all-MiniLM-L6-v2')

fixed_chunks = fixed_size_chunks(DOCUMENT)
para_chunks  = paragraph_chunks(DOCUMENT)

print(f"Fixed-size chunks : {len(fixed_chunks)}")
print(f"Paragraph chunks  : {len(para_chunks)}")

# TODO: Encode fixed_chunks  → fixed_embeddings
# TODO: Encode para_chunks   → para_embeddings

# ── Search helper ────────────────────────────────────────────────────────────
def search_chunks(query: str, chunks: list[str], embeddings, n: int = 2):
    """Return top-n (score, chunk) pairs for a query."""
    # TODO: encode query, compute similarities, return top-n sorted by score
    return []


# ── Test queries ─────────────────────────────────────────────────────────────
# TODO: Define 3 queries that target different parts of your document

queries = [
    # TODO
]

# ── Compare results ───────────────────────────────────────────────────────────
for query in queries:
    print(f'\n{"="*60}')
    print(f'Query: "{query}"')

    print("\n  [Fixed-size chunks]")
    # TODO: call search_chunks with fixed_chunks & fixed_embeddings, print results

    print("\n  [Paragraph chunks]")
    # TODO: call search_chunks with para_chunks & para_embeddings, print results

# ── Analysis ─────────────────────────────────────────────────────────────────
print("\n" + "="*60)
print("ANALYSIS")
# TODO: Print your observations.
#       Which strategy returned more focused results?
#       Which missed context by cutting mid-sentence?
#       When would you choose each strategy?
print("TODO: write your analysis here")
