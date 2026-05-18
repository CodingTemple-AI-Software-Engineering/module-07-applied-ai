# Chunking Strategies & Context Windows — Quiz

**Module 7 — Applied AI: Embeddings & Retrieval**

---

**Question 1:** Why can’t you just embed an entire 50-page document as one vector?

- A) Embedding models only accept single words
- B) The embedding model has a limited context window and would truncate most of the text, plus the resulting embedding would be a diluted average of all topics, reducing search precision
- C) Documents are too large to fit in memory
- D) Embeddings only work with sentences, not documents

> **Answer: B** — Two problems arise. First, models have context windows (e.g., 256 tokens for MiniLM) — text beyond that limit is silently dropped. Second, even if the window were unlimited, averaging 50 pages of diverse content into one vector produces a blurry representation that isn’t close to any specific query. Chunking solves both by creating focused, manageable pieces.
> 

---

**Question 2:** What is the main tradeoff when choosing chunk size?

- A) Larger chunks are more expensive to store; smaller chunks are free
- B) Smaller chunks give more precise search results but lose surrounding context; larger chunks preserve context but dilute the embedding across multiple ideas
- C) Chunk size doesn’t matter — all sizes produce the same results
- D) Smaller chunks are always better

> **Answer: B** — This is the fundamental chunking tradeoff. A 50-word chunk about Pydantic validation gives a precise match for validation queries, but it lacks the surrounding context about *how* to use it. A 1000-word chunk captures everything but its embedding blends FastAPI, Pydantic, async, and testing into one vector. The sweet spot (typically 200–500 words) balances precision and context.
> 

---

**Question 3:** Why do chunks typically include overlap with adjacent chunks?

- A) To make the document longer
- B) To ensure ideas that span chunk boundaries aren’t lost — the overlapping text appears in both chunks
- C) Overlap makes the embedding model more accurate
- D) It’s required by ChromaDB

> **Answer: B** — Without overlap, a sentence at the exact boundary between chunk N and chunk N+1 gets split in half — neither chunk has the complete thought. Overlap (typically 10–20% of chunk size) ensures boundary content appears in both adjacent chunks, so at least one chunk has the full idea. It’s not required by any tool (D) but it’s a best practice for quality.
> 

---

**Question 4:** Which chunking strategy is best for a well-structured document with clear paragraph breaks and section headings?

- A) Fixed-size chunking with no overlap
- B) Character-level chunking (one character per chunk)
- C) Paragraph or section-based chunking, since the document already has natural semantic boundaries
- D) Random chunking

> **Answer: C** — When a document is well-structured, paragraphs and sections represent natural units of meaning. Paragraph chunking produces focused chunks where each one covers a specific topic. Fixed-size chunking (A) ignores these natural boundaries and may cut mid-paragraph. For poorly formatted documents without clear structure, fixed-size with overlap becomes the better fallback.
>