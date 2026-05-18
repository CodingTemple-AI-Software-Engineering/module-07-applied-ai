# Vector Spaces & Similarity — Quiz

**Module 7 — Applied AI: Embeddings & Retrieval**

---

**Question 1:** What does a cosine similarity score of 0.85 between two text embeddings mean?

- A) The texts share exactly 85% of their words
- B) The texts have very similar meaning — they point in nearly the same direction in embedding space
- C) One text is 85% as long as the other
- D) The embedding model is 85% confident in its output

> **Answer: B** — Cosine similarity measures the angle between two vectors, not word overlap. A score of 0.85 means the vectors point in nearly the same direction, indicating very similar meaning. Two sentences can have 0.85 similarity with zero words in common if they express the same idea in different words. Conversely, two sentences sharing many words but different meanings would have lower similarity.
> 

---

**Question 2:** Why is cosine similarity preferred over Euclidean distance for comparing text embeddings?

- A) Cosine similarity is faster to compute
- B) Cosine similarity measures direction (meaning) regardless of magnitude (length), so a short and long document about the same topic get high similarity
- C) Euclidean distance doesn’t work with numbers
- D) Cosine similarity always returns higher scores

> **Answer: B** — Cosine similarity cares only about the *direction* of the vectors, not their length. This is ideal for text because a 3-sentence summary and a 30-page document about the same topic should be recognized as similar. Euclidean distance is affected by vector magnitude, meaning longer documents naturally have larger vectors and appear more distant. Both are valid metrics, but cosine similarity’s direction-only focus makes it more intuitive for text similarity.
> 

---

**Question 3:** A semantic search returns these results for the query "how to set up a database":

```
[0.71] SQLAlchemy ORM maps Python classes to database tables
[0.45] FastAPI generates interactive API documentation
[0.12] The best pasta recipe uses fresh tomatoes
```

Which result is most relevant, and why is the pasta result included?

- A) The pasta result is relevant because cooking involves organizing ingredients (like a database)
- B) The SQLAlchemy result is most relevant because it has the highest similarity score; the pasta result appears because you’re displaying all results, not just relevant ones
- C) All three are equally relevant
- D) The FastAPI result is most relevant because APIs always use databases

> **Answer: B** — The similarity scores tell the story: 0.71 indicates strong relevance (database topic), 0.45 is moderate (APIs are related to databases but the doc focuses on documentation), and 0.12 means essentially unrelated. The pasta result appears only because the system is showing all documents. In a real application, you’d set a threshold (e.g., 0.3) and filter out low-scoring results.
>