# Vector Spaces & Similarity — Guided Example

**Module 7 — Applied AI: Embeddings & Retrieval**

`[VIDEO PLACEHOLDER: 8 min — "Visualizing Similarity: compute a full similarity matrix, display it as a heatmap, and compare cosine similarity with Euclidean distance. Show how cosine correctly groups similar meanings."]`

Let’s explore similarity hands-on. We’ll build a similarity matrix, compare metrics, and learn to interpret the results.

Create a file called `similarity_explorer.py`:

```python
from sentence_transformers import SentenceTransformer, util
import numpy as np

model = SentenceTransformer('all-MiniLM-L6-v2')

# Sentences grouped by topic (we'll see if similarity reflects this)
sentences = [
    # Group 1: Python/API development
    "How to build a REST API with FastAPI",             # 0
    "Creating web services in Python",                   # 1
    "Python backend development with async support",     # 2
    # Group 2: Cooking
    "The best homemade pasta recipe with fresh tomatoes", # 3
    "How to make pizza dough from scratch",               # 4
    # Group 3: Space
    "NASA's latest Mars rover discovered water ice",     # 5
    "SpaceX launched a new satellite into orbit",        # 6
]

embeddings = model.encode(sentences)

# --- Build a similarity matrix ---
print("=== Cosine Similarity Matrix ===")
print("(Higher = more similar)\n")

# Short labels for readability
labels = ["FastAPI", "WebSvc", "PyBack", "Pasta", "Pizza", "Mars", "SpaceX"]

# Print header
print(f"{'':>8}", end="")
for label in labels:
    print(f"{label:>8}", end="")
print()

# Compute and print pairwise similarities
for i in range(len(sentences)):
    print(f"{labels[i]:>8}", end="")
    for j in range(len(sentences)):
        sim = util.cos_sim(embeddings[i], embeddings[j]).item()
        print(f"{sim:>8.3f}", end="")
    print()
```

Run it:

```bash
python similarity_explorer.py
```

You should see a grid where the Python/API sentences (first three) have high similarity to each other (~0.5–0.7), the cooking sentences are similar to each other (~0.5+), and the space sentences are similar to each other — but cross-group similarities are low (~0.0–0.2).

---

## Step 2: Finding the Best Match

Add this to the script:

```python
print("\n=== Finding Best Matches ===")

queries = [
    "How do I create an API endpoint?",
    "What's a good recipe for Italian food?",
    "Tell me about recent space exploration",
]

for query in queries:
    query_emb = model.encode(query)
    scores = util.cos_sim(query_emb, embeddings)[0]

    # Get the index of the highest score
    best_idx = scores.argmax().item()
    best_score = scores[best_idx].item()

    print(f"\nQuery: '{query}'")
    print(f"  Best match: [{best_score:.4f}] {sentences[best_idx]}")
```

You should see each query matched to the most semantically relevant sentence — even though the words don’t overlap much.

---

## Step 3: Cosine vs. Euclidean Distance

Let’s see why cosine similarity is preferred. Add this:

```python
from numpy.linalg import norm

print("\n=== Cosine vs. Euclidean ===")

# Compare two similar sentences and one unrelated
pairs = [
    (0, 1, "FastAPI vs WebServices (similar)"),
    (0, 3, "FastAPI vs Pasta (different)"),
    (3, 4, "Pasta vs Pizza (similar)"),
]

for i, j, label in pairs:
    cos_sim = util.cos_sim(embeddings[i], embeddings[j]).item()
    euc_dist = norm(embeddings[i] - embeddings[j])  # Euclidean distance

    print(f"\n{label}:")
    print(f"  Cosine similarity: {cos_sim:.4f}  (higher = more similar)")
    print(f"  Euclidean distance: {euc_dist:.4f}  (lower = more similar)")
```

Both metrics should agree on which pairs are similar and which aren’t. For modern embedding models, both work well, but cosine similarity gives you a bounded 0–1 score that’s easier to interpret and threshold.

`[DIAGRAM PLACEHOLDER: Heatmap visualization of the similarity matrix, with warm colors (red/orange) for high similarity and cool colors (blue) for low similarity. The topic clusters should be clearly visible as warm blocks along the diagonal.]`