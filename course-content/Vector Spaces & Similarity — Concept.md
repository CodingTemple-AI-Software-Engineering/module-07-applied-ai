# Vector Spaces & Similarity — Concept

**Module 7 — Applied AI: Embeddings & Retrieval**

**Estimated time: 35 minutes**

---

### Learning Objectives

By the end of this lesson, you will be able to:

1. Explain what a vector space is and how embeddings live inside it
2. Describe cosine similarity intuitively and explain why it’s preferred over raw distance
3. Interpret similarity scores (what’s "high enough" to be relevant?)
4. Identify common distance metrics and when each is useful

---

`[VIDEO PLACEHOLDER: 7 min — "Vector Spaces & Similarity: Use 2D and 3D visualizations to show vectors as arrows, demonstrate cosine similarity as the angle between arrows, and show why two long documents about the same topic have high cosine similarity even if their magnitudes differ."]`

In the last lesson, you turned sentences into lists of numbers. Now the question becomes: how do you use those numbers to figure out which sentences are *similar*?

Imagine you’re standing on a vast, flat plain. Each document you’ve embedded is a flag planted somewhere on this plain. Documents about Python APIs are clustered in one area. Documents about cooking are in another. When a user asks a question, you embed their query and plant a new flag. The closest existing flags to your query flag are the most relevant results.

That plain is a **vector space**. The flags are **vectors** (your embeddings). And the method for measuring "closest" is **similarity** — which is what this lesson is about.

---

## Vectors as Arrows

A vector is just an ordered list of numbers. In 2D, a vector [3, 4] describes a point (or an arrow from the origin to that point). In embedding space, your vectors have 384 dimensions instead of 2, but the same principles apply.

Every embedding model creates a space where:

- **Direction** represents meaning (what the text is about)
- **Similar meanings** point in similar directions
- **Different meanings** point in different directions

`[DIAGRAM PLACEHOLDER: 2D diagram showing three vectors as arrows from the origin. Two arrows (labeled "build an API" and "create a web service") point in nearly the same direction. A third arrow (labeled "best pizza recipe") points in a completely different direction. Caption: "Similar meanings = similar directions."]`

---

## Cosine Similarity: Measuring the Angle

The most common way to compare embeddings is **cosine similarity**. It measures the angle between two vectors, ignoring their length.

Think of it this way: if two arrows point in exactly the same direction, the angle between them is 0°, and the cosine similarity is **1** (maximum similarity). If they point in completely unrelated directions (90°), the cosine similarity is **0**. If they point in opposite directions (180°), it’s **-1**.

Why ignore length? Because a short document about Python APIs and a long document about Python APIs should have the same similarity to a query about Python APIs. They’re about the same thing — one is just longer. Cosine similarity cares about *direction* (meaning), not *magnitude* (length).

Mathematically, cosine similarity is:

```
cosine_similarity(A, B) = (A · B) / (|A| × |B|)
```

Where `A · B` is the dot product (multiply corresponding elements and sum them), and `|A|` and `|B|` are the magnitudes (lengths) of each vector. You don’t need to implement this yourself — libraries do it for you — but understanding the intuition matters.

---

## Interpreting Similarity Scores

Cosine similarity returns a number between -1 and 1. But what do the numbers mean in practice?

For sentence embeddings from models like `all-MiniLM-L6-v2`:

- **0.8 – 1.0:** Very similar. Nearly identical meaning, possibly paraphrases.
- **0.5 – 0.8:** Related. Same topic or domain, might answer the query.
- **0.2 – 0.5:** Loosely related. Some overlap but not a direct match.
- **0.0 – 0.2:** Unrelated. Different topics entirely.
- **Below 0.0:** Rare for modern embedding models, would indicate opposing meaning.

These thresholds are rough guides, not hard rules. The right threshold for "relevant" depends on your application. For a search engine, you might show anything above 0.3. For a strict Q&A system, you might require 0.6+.

---

## Other Distance Metrics

Cosine similarity is the most common for text embeddings, but you’ll encounter others:

**Euclidean distance:** The straight-line distance between two points. Sensitive to magnitude (longer vectors are farther from shorter ones). Less ideal for text because document length affects the result.

**Dot product:** The raw A · B without normalizing by length. Faster to compute, and some embedding models are trained to work best with dot product. ChromaDB supports this.

**Manhattan distance:** The "city block" distance (sum of absolute differences). Less commonly used for embeddings.

For this course, you’ll primarily use cosine similarity. It’s the default in most tools and the most intuitive for text.

---

## Why This Matters for Search Systems

The choice of similarity metric and the threshold you set determine the quality of your search results. Too strict a threshold (0.9+) and you miss relevant documents that are phrased differently. Too loose (0.1+) and you return irrelevant noise.

In the upcoming lessons, you’ll store your embeddings in ChromaDB (a vector database) and use cosine similarity to retrieve the most relevant chunks for any query. Understanding what the similarity scores mean helps you tune your system and explain why certain results appear.