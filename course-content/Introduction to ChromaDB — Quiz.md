# Introduction to ChromaDB — Quiz

**Module 7 — Applied AI: Embeddings & Retrieval**

---

**Question 1:** What is a vector database, and why can’t you just use a regular SQL database for embeddings?

- A) A vector database is exactly like SQL but faster
- B) A vector database is optimized for storing and searching numerical vectors by similarity, using algorithms that avoid scanning every document — something SQL databases aren’t designed for
- C) Regular SQL databases can’t store numbers
- D) Vector databases only work with images, not text

> **Answer: B** — SQL databases store rows and query them with exact conditions (WHERE age > 25). Vector databases store high-dimensional vectors and query them by *similarity* — finding the nearest neighbors in embedding space. They use specialized algorithms (approximate nearest neighbor search) that are much faster than comparing every vector. You *could* store embeddings in SQL as arrays, but searching would require a full table scan on every query.
> 

---

**Question 2:** What is a ChromaDB collection?

- A) A file format for saving embeddings
- B) A group of documents with their embeddings and metadata, analogous to a table in a relational database
- C) A Python list of strings
- D) A web API endpoint

> **Answer: B** — A collection in ChromaDB is the equivalent of a table in SQL. It holds documents (text), their embeddings (vectors), optional metadata (key-value pairs), and unique IDs. You can have multiple collections for different purposes — one for course notes, one for documentation, etc.
> 

---

**Question 3:** ChromaDB’s `.query()` returns distances. A result with distance 0.15 and another with distance 0.82 — which is more relevant?

- A) 0.82, because higher numbers mean more similar
- B) 0.15, because lower distance means the vectors are closer together (more similar)
- C) They are equally relevant
- D) Neither — distance doesn’t indicate relevance

> **Answer: B** — ChromaDB returns distances (lower = more similar), which is the opposite of the cosine similarity scores (higher = more similar) you used in earlier lessons. A distance of 0.15 means the query and document vectors are very close in embedding space — strong match. A distance of 0.82 means they’re far apart — weak match. This is a common gotcha when switching between tools.
> 

---

**Question 4:** What is the purpose of metadata in ChromaDB documents?

- A) It makes the embeddings more accurate
- B) It stores additional information (like source file, category, date) that you can use to filter search results
- C) It’s required for every document
- D) It replaces the document text

> **Answer: B** — Metadata is optional key-value data attached to each document. It doesn’t affect the embedding or similarity calculation, but it lets you filter results — for example, searching only documents from a specific module, category, or date range. This is like adding a WHERE clause to your similarity search.
>