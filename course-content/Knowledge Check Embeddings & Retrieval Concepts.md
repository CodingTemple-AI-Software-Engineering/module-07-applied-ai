# Knowledge Check: Embeddings & Retrieval Concepts

**Module 7 — Applied AI: Embeddings & Retrieval**

**Mid-Module Assessment — Covers Lessons 1–4 (Embeddings, Similarity, Chunking, ChromaDB)**

---

**Question 1:** What does an embedding represent?

- A) A compressed version of the original text
- B) A list of numbers (vector) that captures the semantic meaning of text, where similar meanings produce similar vectors
- C) An encrypted version of text for security
- D) A translation of text into a different language

> **Answer: B** — Embeddings convert text into numerical vectors that encode meaning. The defining property is that semantically similar texts produce vectors that are close together in the embedding space, enabling computers to compare meaning mathematically.
> 

---

**Question 2:** A cosine similarity score of 0.92 between two sentence embeddings indicates:

- A) The sentences share exactly 92% of their words
- B) The sentences have very similar meaning — likely paraphrases or about the same specific topic
- C) One sentence is 92 characters long
- D) The embedding model is 92% accurate

> **Answer: B** — Cosine similarity measures direction alignment in embedding space, not word overlap. A score of 0.92 indicates very high semantic similarity. Two sentences with zero shared words can have 0.92 similarity if they express the same idea in different terms.
> 

---

**Question 3:** Why is chunking necessary before embedding a 50-page document?

- A) Embedding models can only process single words
- B) The embedding model has a limited context window that would truncate most of the text, and the resulting single vector would average all topics, reducing search precision
- C) ChromaDB can only store short texts
- D) Chunking makes the document smaller to save disk space

> **Answer: B** — Two problems: most embedding models truncate text beyond their context window (e.g., 256 tokens), silently losing most of a long document. Even with unlimited windows, one vector averaging 50 pages of diverse content would be too diluted to match any specific query well. Chunking creates focused pieces that fit the model and represent specific topics.
> 

---

**Question 4:** What is the main tradeoff when choosing chunk size?

- A) Cost vs. speed
- B) Smaller chunks give precise but context-poor results; larger chunks give context-rich but less precise results
- C) Chunk size doesn’t affect search quality
- D) Larger chunks are always better

> **Answer: B** — Small chunks (50–100 words) find the exact relevant sentence but miss surrounding context. Large chunks (500–1000 words) provide full context but their embeddings blend multiple ideas, reducing precision. The sweet spot (200–500 words) balances both, but the ideal size depends on your documents and use case.
> 

---

**Question 5:** What does a vector database like ChromaDB do that a Python list of embeddings cannot?

- A) Generate embeddings from text
- B) Persist data to disk, use optimized search algorithms for large collections, and support metadata filtering
- C) Run faster than any other approach
- D) Connect to the internet

> **Answer: B** — A Python list works for 10–100 embeddings but doesn’t persist across script runs, requires linear scans through every vector, and has no metadata filtering. ChromaDB provides disk persistence, approximate nearest neighbor algorithms for fast search at scale, and metadata-based filtering — all essential for real applications.
> 

---

**Question 6:** In ChromaDB, what is the difference between the value returned by `.query()` and the cosine similarity scores you computed manually in earlier lessons?

- A) No difference — they’re the same metric
- B) ChromaDB returns distances (lower = more similar), while cosine similarity gives scores (higher = more similar) — they’re inversely related
- C) ChromaDB returns boolean values (relevant or not)
- D) ChromaDB only returns document text, not scores

> **Answer: B** — ChromaDB’s default `.query()` returns distances, where lower values mean more similar documents. This is the inverse of cosine similarity where higher values mean more similar. A distance of 0.1 (very close) corresponds roughly to a cosine similarity of 0.9 (very similar). This is a common source of confusion when switching between tools.
> 

---

**Question 7:** What is the difference between keyword search and semantic search?

- A) Keyword search uses Google; semantic search uses ChromaDB
- B) Keyword search matches exact words in the query to words in documents; semantic search compares the meaning of the query to the meaning of documents using embeddings
- C) Semantic search is slower and less accurate
- D) They produce identical results

> **Answer: B** — Keyword search relies on word matching — the query "build an API" only finds documents containing those exact words. Semantic search converts both query and documents to embeddings and compares meaning vectors, so "build an API" also finds documents about "creating web services" or "developing backend endpoints." Semantic search finds conceptually relevant results that keyword search would miss.
> 

---

**Question 8:** Why do chunks typically include overlap with adjacent chunks?

- A) To increase the total number of chunks
- B) To ensure ideas that span chunk boundaries aren’t lost, since the overlapping text appears in both chunks
- C) ChromaDB requires overlapping IDs
- D) Overlap makes embedding models more accurate

> **Answer: B** — Without overlap, a thought that spans the boundary between two chunks gets split — neither chunk has the complete idea. Overlap (typically 10–20% of chunk size) ensures the boundary content appears in both adjacent chunks. At least one chunk will contain the full thought, making it findable by search.
>