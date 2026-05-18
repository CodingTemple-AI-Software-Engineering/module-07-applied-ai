# Module 7 Overview

**Module 7 — Applied AI: Embeddings & Retrieval**

**Duration:** 2 Weeks | **Hours:** 40 | **Prerequisites:** Modules 1–6

---

## Module Philosophy

This module is the conceptual bridge to AI system building. Students understand HOW AI finds and uses information — the foundation of every RAG system, search engine, and recommendation system. The module builds from concept (what are embeddings?) through implementation (ChromaDB) to application (semantic search tool) to security (prompt injection) to measurement (evaluation).

This module does NOT build a full RAG pipeline — that’s Module 8. Here, students focus on the retrieval half: understanding embeddings, building search, and evaluating quality.

---

## Week Structure

### Week 1 — Embeddings & Vector Storage

1. **What Are Embeddings?** — Words as numbers, semantic meaning, keyword vs. semantic search
2. **Vector Spaces & Similarity** — Cosine similarity, distance metrics, interpreting scores
3. **Chunking Strategies & Context Windows** — Why chunking matters, fixed vs. paragraph vs. semantic, the chunk size tradeoff
4. **Introduction to ChromaDB** — Vector database concepts, collections, adding/querying, metadata filtering

### Knowledge Check: Embeddings & Retrieval Concepts (8 questions)

Covers embeddings, similarity, chunking, ChromaDB, and the difference between keyword and semantic search.

### Week 2 — Search, Prompts & Evaluation

1. **Building a Semantic Search Tool** — Complete pipeline from document loading to Streamlit interface
2. **Prompt Engineering Basics** — Framing, specificity, few-shot, system prompts for RAG
3. **Prompt Injection Awareness** — Direct/indirect injection, why it matters for RAG, mitigations
4. **Evaluation: How Good Are Your Search Results?** — Precision, recall, evaluation sets, failure modes

### Module Project: Semantic Search Engine (100 points, 5-minute presentation)

---

## Assessment Summary

| Assessment | Type | Placement | Weight |
| --- | --- | --- | --- |
| Embeddings & Retrieval Concepts Check | Knowledge Check (8 questions) | After Lesson 4 | Mid-module checkpoint |
| Semantic Search Engine | Module Project (5-min presentation) | End of Week 2 | Final module assessment |

---

## Dependencies

```
sentence-transformers
chromadb
streamlit
requests
numpy
openai          # Optional — for prompt engineering exercises
```

---

## Video Placeholders Summary

| Lesson | Placement | Length | Theme |
| --- | --- | --- | --- |
| What Are Embeddings? | Concept | 7 min | Words as vectors, King-Man+Woman=Queen, 2D similarity plot |
| What Are Embeddings? | Guided Example | 8 min | Generate embeddings, compare similarity, build 10-line search |
| Vector Spaces & Similarity | Concept | 7 min | Vectors as arrows, cosine similarity as angle, 2D/3D visuals |
| Vector Spaces & Similarity | Guided Example | 8 min | Similarity matrix, heatmap, cosine vs Euclidean comparison |
| Chunking Strategies | Concept | 6 min | Document split three ways, precision vs context tradeoff |
| Chunking Strategies | Guided Example | 8 min | Same doc chunked 3 ways, same query, compare results |
| Introduction to ChromaDB | Concept | 7 min | Vector database concepts, why not just Python lists |
| Introduction to ChromaDB | Guided Example | 10 min | Install, create collection, add docs, query, filter by metadata |
| Building a Semantic Search Tool | Concept | 8 min | Complete pipeline from raw docs to Streamlit search |
| Building a Semantic Search Tool | Guided Example | 12 min | Full app: load files, chunk, store, search with Streamlit UI |
| Prompt Engineering Basics | Concept | 6 min | Same question 3 ways, framing/specificity/few-shot demo |
| Prompt Engineering Basics | Guided Example | 8 min | Bad vs good prompts side-by-side, mock API comparison |
| Prompt Injection Awareness | Concept | 7 min | Live demo of poisoned document hijacking RAG response |
| Prompt Injection Awareness | Guided Example | 8 min | Attack simulation and mitigation demo |
| Evaluation | Concept | 6 min | Wrong results that look right, precision/recall with concrete example |
| Evaluation | Guided Example | 10 min | Build evaluation set, compute metrics, threshold comparison |