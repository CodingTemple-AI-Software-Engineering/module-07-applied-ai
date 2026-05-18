# Building a Semantic Search Tool — Quiz

**Module 7 — Applied AI: Embeddings & Retrieval**

---

**Question 1:** In a semantic search pipeline, why must the ingestion phase and query phase use the same embedding model?

- A) Different models produce different-sized files
- B) Each model creates its own vector space — vectors from different models are incompatible and similarity scores between them are meaningless
- C) Using different models is slower
- D) ChromaDB only supports one model

> **Answer: B** — Each embedding model defines its own vector space with its own learned dimensions. A vector from model A and a vector from model B exist in completely different spaces — comparing them is like comparing GPS coordinates on two different maps with different projections. The distance between them has no semantic meaning.
> 

---

**Question 2:** What is the purpose of including `source` metadata when storing chunks in ChromaDB?

- A) It makes the embeddings more accurate
- B) It lets you trace search results back to their original document and filter results by source
- C) ChromaDB requires a source field
- D) It replaces the need for unique IDs

> **Answer: B** — Source metadata serves two purposes: attribution (users see where the information came from) and filtering (you can restrict searches to specific sources). When a search returns "Use st.session_state to persist data," knowing it came from `streamlit_guide.txt` helps users find the full document.
> 

---

**Question 3:** Why is `@st.cache_resource` used for the ChromaDB client in the Streamlit app?

- A) It makes the database faster
- B) It prevents the ChromaDB client from being recreated on every Streamlit re-run, keeping the connection persistent
- C) It's required by ChromaDB
- D) It caches the search results

> **Answer: B** — Streamlit re-runs the entire script on every interaction. Without caching, a new ChromaDB client would be created on every click, slider move, or text input. `@st.cache_resource` creates the client once and reuses it across re-runs. This is different from `@st.cache_data` (which caches return values) — `@st.cache_resource` is for objects like database connections and ML models that should persist.
>