# Module Project: Semantic Search Engine

**Module 7 — Applied AI: Embeddings & Retrieval**

---

## Project Overview

Build a working **semantic search tool** over a provided document collection. The tool should load, chunk, embed, and store documents in ChromaDB, then provide a Streamlit interface where users can type a question and see ranked results. You’ll also run a chunking experiment and document the results.

**Time:** 10–15 hours

**Presentation:** 5 minutes (live demo + chunking experiment results)

---

## Project Structure

```
semantic-search/
├── app.py               # Streamlit search interface
├── ingest.py            # Document loading, chunking, and ChromaDB storage
├── search.py            # Search functions (query ChromaDB, rank results)
├── evaluate.py          # Evaluation framework (precision, recall)
├── docs/                # Document collection to search
│   ├── document1.txt
│   ├── document2.md
│   └── ...
├── chroma_data/         # Persistent ChromaDB storage
├── requirements.txt
└── README.md            # Setup instructions and chunking experiment results
```

---

## Requirements & Rubric

### 1. Document Ingestion (20 points)

- Load documents from a `docs/` folder (at least 8 documents, 5+ pages of total content)
- Implement a clear chunking strategy with configurable chunk size and overlap
- Store chunks in a persistent ChromaDB collection with metadata (source file, chunk index)
- Documents can be: course notes, technical documentation, Wikipedia articles, or the provided starter corpus

### 2. Semantic Search (25 points)

- Accept a text query and return the top-N most relevant chunks
- Display results with: the matched text, source file, similarity/distance score, and relevance indicator
- Support configurable `n_results` and similarity threshold
- Handle edge cases: empty queries, no results above threshold

### 3. Streamlit Interface (20 points)

- Search input with results displayed below
- Sidebar with: document count, re-index button, result count slider, source file filter (multiselect)
- At least one `st.metric()` showing collection stats
- Clean layout with `st.set_page_config()`

### 4. Chunking Experiment (20 points)

- Re-index documents with at least **2 different chunk sizes** (e.g., 200 chars vs 500 chars)
- Run the **same 5 test queries** against both versions
- Compare results: which chunk size produced better results for each query?
- Document your findings in the README (which size worked better overall and why)

### 5. Code Quality & Documentation (15 points)

- Modular code (separate files for ingestion, search, evaluation, UI)
- Functions with docstrings
- Working `requirements.txt`
- README with: setup instructions, architecture description, chunking experiment results

---

## Grading Rubric

| Category | Points | Criteria |
| --- | --- | --- |
| Document Ingestion | 20 | Load 8+ docs, configurable chunking, ChromaDB with metadata |
| Semantic Search | 25 | Ranked results with scores, configurable N and threshold, edge cases |
| Streamlit Interface | 20 | Search input, sidebar controls, source filter, metrics, clean layout |
| Chunking Experiment | 20 | 2+ chunk sizes, 5 test queries, comparison, documented findings |
| Code Quality & Docs | 15 | Modular files, docstrings, requirements.txt, README |
| **Total** | **100** |  |

---

## Document Collection Options

**Option A (Recommended):** Use the provided starter corpus — a set of technical articles and documentation snippets about Python, APIs, databases, and AI concepts.

**Option B:** Use your own course notes from Modules 1–6. Export or copy your notes into `.txt` or `.md` files.

**Option C:** Use Wikipedia articles or open-source documentation. Choose 8–12 articles on related topics.

---

## Chunking Experiment Guide

The experiment is a core part of this project. Here’s the approach:

1. Choose 2–3 chunk sizes (e.g., 150 chars, 300 chars, 600 chars)
2. For each size, re-index all documents and run 5 identical test queries
3. For each query and chunk size, record: top-3 results, their scores, and whether they’re relevant
4. Write up: which chunk size worked best overall, which queries showed the biggest difference, and your hypothesis about why

This experiment teaches something no tutorial can: the practical impact of a design choice on real results. You’ll carry this skill into every AI project.

---

## 5-Minute Presentation

1. **Live demo** (2 min) — Type a search query, show the results with scores and sources. Show the source filter working.
2. **Chunking experiment** (2 min) — Show results from two different chunk sizes for the same query. Explain which worked better and why.
3. **One challenge + one improvement** (1 min) — What was hardest? What would you add with more time?

---

## Starter Code

**GitHub:** `module-07-applied-ai/project/starter/`

The starter includes: project folder structure, a `requirements.txt` with pinned versions (`chromadb`, `sentence-transformers`, `streamlit`), a sample document corpus in `docs/`, an `ingest.py` skeleton with function stubs, and a `search.py` skeleton with the query function interface.

You build the actual implementation and the Streamlit interface.