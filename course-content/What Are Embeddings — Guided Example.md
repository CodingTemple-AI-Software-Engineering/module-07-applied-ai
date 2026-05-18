# What Are Embeddings? — Guided Example

**Module 7 — Applied AI: Embeddings & Retrieval**

`[VIDEO PLACEHOLDER: 8 min — "Embeddings hands-on: install sentence-transformers, generate embeddings for sentences, compare them, and visualize similarity. Show how 'How do I build an API?' and 'Creating a web service' are close while 'Best pizza recipe' is far away."]`

Let’s generate real embeddings and see how they capture meaning. You’ll use the `sentence-transformers` library, which provides pre-trained models that convert text into vectors.

---

## Step 1: Install the Library

In your module’s virtual environment:

```bash
pip install sentence-transformers
```

This installs the library and downloads a small embedding model the first time you use it. The download is about 80MB — it only happens once.

---

## Step 2: Generate Your First Embeddings

Create a file called `embeddings_intro.py`:

```python
from sentence_transformers import SentenceTransformer

# Load a pre-trained embedding model
# 'all-MiniLM-L6-v2' is small, fast, and good for learning
model = SentenceTransformer('all-MiniLM-L6-v2')

# Sentences to embed
sentences = [
    "How do I build a REST API in Python?",
    "Creating a web service using FastAPI",
    "Best pizza recipe with mozzarella",
    "What is the capital of France?",
    "Building backend services with Python frameworks",
]

# Generate embeddings — each sentence becomes a vector of 384 numbers
embeddings = model.encode(sentences)

# Let's see what we got
print(f"Number of sentences: {len(embeddings)}")
print(f"Embedding dimensions: {embeddings[0].shape}")  # Should be (384,)
print(f"\nFirst 10 values of 'How do I build a REST API in Python?':")
print(embeddings[0][:10])  # Just the first 10 of 384 numbers
```

Run it:

```bash
python embeddings_intro.py
```

You should see:

```
Number of sentences: 5
Embedding dimensions: (384,)

First 10 values of 'How do I build a REST API in Python?':
[ 0.0345  -0.0891   0.0234  ...  (384 numbers total) ]
```

Each sentence is now a list of 384 numbers. Those numbers encode the meaning of the sentence.

---

## Step 3: Compare Similarity Between Sentences

Now let’s measure how similar these sentences are to each other. We’ll use **cosine similarity** (which you’ll learn about in depth in the next lesson):

```python
from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer('all-MiniLM-L6-v2')

sentences = [
    "How do I build a REST API in Python?",       # [0]
    "Creating a web service using FastAPI",        # [1]
    "Best pizza recipe with mozzarella",           # [2]
    "What is the capital of France?",              # [3]
    "Building backend services with Python frameworks",  # [4]
]

embeddings = model.encode(sentences)

# Compare the first sentence against all others
query = embeddings[0]  # "How do I build a REST API in Python?"

print("Similarity to 'How do I build a REST API in Python?':\n")
for i, sentence in enumerate(sentences):
    # cosine_similarity returns a value between -1 and 1
    # 1 = identical meaning, 0 = unrelated, -1 = opposite
    similarity = util.cos_sim(query, embeddings[i]).item()  # .item() converts tensor to float
    print(f"  {similarity:.4f} — {sentence}")
```

You should see something like:

```
Similarity to 'How do I build a REST API in Python?':

  1.0000 — How do I build a REST API in Python?
  0.7234 — Creating a web service using FastAPI
  0.0812 — Best pizza recipe with mozzarella
  0.1345 — What is the capital of France?
  0.6891 — Building backend services with Python frameworks
```

Look at the scores:

- **1.0** for the same sentence (perfect match)
- **~0.72** for "Creating a web service using FastAPI" — high similarity despite different words
- **~0.69** for "Building backend services with Python frameworks" — also semantically related
- **~0.08** and **~0.13** for pizza and France — completely unrelated topics

The model understood that building APIs and creating web services are about the same thing, even though the sentences share almost no words. That’s semantic understanding encoded as numbers.

---

## Step 4: Semantic Search in 10 Lines

Let’s build the simplest possible semantic search:

```python
from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer('all-MiniLM-L6-v2')

# Our "knowledge base" — imagine these are paragraphs from documentation
documents = [
    "FastAPI automatically generates interactive API documentation using Swagger UI.",
    "Use pip install to add Python packages to your virtual environment.",
    "SQLAlchemy is an ORM that maps Python classes to database tables.",
    "Streamlit re-runs the entire script every time a user interacts with a widget.",
    "JWT tokens are used for stateless authentication in REST APIs.",
    "The requests library lets you make HTTP calls from Python.",
    "CSS Flexbox arranges elements in a row or column with flexible sizing.",
    "ChromaDB stores document embeddings for fast similarity search.",
]

# Embed all documents (do this once, store the results)
doc_embeddings = model.encode(documents)

# User asks a question
query = "How do I authenticate users in my API?"
query_embedding = model.encode(query)

# Find the most similar documents
scores = util.cos_sim(query_embedding, doc_embeddings)[0]  # Compare query to all docs

# Sort by score (highest first)
ranked = sorted(enumerate(scores), key=lambda x: x[1], reverse=True)

print(f"Query: '{query}'\n")
print("Top 3 results:")
for rank, (idx, score) in enumerate(ranked[:3], 1):
    print(f"  {rank}. [{score:.4f}] {documents[idx]}")
```

You should see the JWT authentication document ranked first, followed by other API-related documents — even though the query doesn’t mention "JWT" or "token."

That’s semantic search. In 10 lines of Python, you built a system that finds relevant information by *meaning*, not keywords. The rest of this module builds on this foundation — adding vector databases for scale, chunking strategies for longer documents, and evaluation techniques to measure quality.

`[DIAGRAM PLACEHOLDER: Simple flow diagram showing: Query text → Embedding model → Query vector → Compare to document vectors → Ranked results by similarity score]`