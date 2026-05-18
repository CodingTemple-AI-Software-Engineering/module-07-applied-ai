# Chunking Strategies & Context Windows — Guided Example

**Module 7 — Applied AI: Embeddings & Retrieval**

`[VIDEO PLACEHOLDER: 8 min — "Chunking in Practice: take a real document, chunk it three different ways, embed all versions, run the same query against each, and compare which chunking strategy returns the best results."]`

Let’s take a real piece of text, chunk it different ways, and compare the search results. This will build your intuition for the chunk size tradeoff.

Create a file called `chunking_demo.py`:

```python
from sentence_transformers import SentenceTransformer, util
import re

model = SentenceTransformer('all-MiniLM-L6-v2')

# A sample "document" — a mini lesson about FastAPI
document = """FastAPI is a modern Python web framework for building APIs. It was created by 
Sebastián Ramírez and released in 2018. FastAPI is built on top of Starlette for the web 
parts and Pydantic for the data parts.

One of FastAPI's biggest advantages is automatic data validation. When you define a Pydantic 
model for your endpoint, FastAPI automatically validates incoming request data. If the data 
doesn't match the model, the client gets a detailed 422 error response.

FastAPI also generates interactive API documentation automatically. Visit /docs for Swagger 
UI or /redoc for ReDoc. The documentation stays in sync with your code because it's 
generated from your type hints and Pydantic models.

Async support is another key feature. FastAPI supports Python's async/await syntax natively. 
This means your API can handle multiple concurrent requests without blocking. When one 
request is waiting for a database query, the server processes other requests.

JWT authentication is commonly used with FastAPI. You create a /auth/token endpoint that 
validates credentials and returns a signed token. Protected endpoints then require a valid 
token in the Authorization header.

Testing FastAPI applications uses pytest with TestClient. You can test endpoints without 
running a server. TestClient simulates HTTP requests and returns the responses for 
assertion."""

# --- Strategy 1: Fixed-size chunks (200 chars, 50 overlap) ---
def fixed_chunks(text, size=200, overlap=50):
    chunks = []
    start = 0
    while start < len(text):
        end = min(start + size, len(text))
        chunks.append(text[start:end].strip())
        start = end - overlap
    return [c for c in chunks if c]  # Remove empty chunks

# --- Strategy 2: Paragraph chunks ---
def paragraph_chunks(text):
    paragraphs = text.strip().split('\n\n')  # Split on double newlines
    return [p.strip() for p in paragraphs if p.strip()]

# --- Strategy 3: Sentence chunks (group ~3 sentences) ---
def sentence_group_chunks(text, sentences_per_chunk=3):
    sentences = re.split(r'(?<=[.!?])\s+', text.strip())
    chunks = []
    for i in range(0, len(sentences), sentences_per_chunk):
        chunk = ' '.join(sentences[i:i + sentences_per_chunk])
        if chunk.strip():
            chunks.append(chunk.strip())
    return chunks

# Generate chunks with each strategy
strategies = {
    "Fixed (200 chars)": fixed_chunks(document),
    "Paragraph": paragraph_chunks(document),
    "3-Sentence Groups": sentence_group_chunks(document),
}

# Show chunk counts and sizes
for name, chunks in strategies.items():
    sizes = [len(c) for c in chunks]
    print(f"{name}: {len(chunks)} chunks, avg {sum(sizes)//len(sizes)} chars")

# --- Search comparison ---
query = "How does FastAPI validate data?"
print(f"\nQuery: '{query}'\n")

for name, chunks in strategies.items():
    # Embed chunks
    chunk_embeddings = model.encode(chunks)
    query_embedding = model.encode(query)

    # Find best match
    scores = util.cos_sim(query_embedding, chunk_embeddings)[0]
    best_idx = scores.argmax().item()
    best_score = scores[best_idx].item()

    print(f"--- {name} ---")
    print(f"Best score: {best_score:.4f}")
    print(f"Best chunk ({len(chunks[best_idx])} chars):")
    print(f"  '{chunks[best_idx][:120]}...'\n")
```

Run it:

```bash
python chunking_demo.py
```

---

## What You Should See

The query "How does FastAPI validate data?" should match best against the paragraph about Pydantic validation. But the *quality* of the match depends on the chunking strategy:

- **Fixed-size chunks** might cut the validation paragraph in half, giving a partial answer with a lower score.
- **Paragraph chunks** should return the complete validation paragraph with a high score.
- **3-sentence groups** might capture the key sentences but include some context from adjacent topics.

The "right" strategy depends on your documents. For this well-structured text with clear paragraphs, paragraph chunking wins. For a poorly formatted document with no paragraph breaks, fixed-size or sentence-based would be better.

Experiment by changing the query to test other topics ("What is async/await?", "How do I test my API?") and see how the results change across strategies.

`[DIAGRAM PLACEHOLDER: Side-by-side comparison showing the same document chunked three ways, with the best-matching chunk for the same query highlighted in each version]`