# Building a Semantic Search Tool — Guided Example

**Module 7 — Applied AI: Embeddings & Retrieval**

`[VIDEO PLACEHOLDER: 12 min — "Complete Semantic Search Tool: build the full pipeline from loading text files to a Streamlit search interface. Show the tool answering real questions and display results with source file, score, and highlighted text."]`

Let’s build a complete semantic search tool with a Streamlit interface. We’ll create sample documents first, then the search pipeline.

---

## Step 1: Create Sample Documents

Create a folder called `docs/` with 3–4 text files. Here’s an example:

**`docs/fastapi_basics.txt`:**

```
FastAPI is a modern Python web framework for building APIs.

FastAPI uses Pydantic models for automatic data validation. When you define a Pydantic model, FastAPI validates incoming requests automatically and returns detailed error messages for invalid data.

FastAPI generates interactive documentation at /docs (Swagger UI) and /redoc. The documentation is always in sync with your code because it's generated from type hints.

Async support in FastAPI allows handling multiple requests concurrently. When one request waits for a database query, the server processes other requests instead of blocking.
```

**`docs/streamlit_guide.txt`:**

```
Streamlit is a Python library for building web applications.

The most important concept in Streamlit is the re-run model. Every time a user interacts with any widget, the entire Python script re-runs from top to bottom.

Because scripts re-run completely, regular variables reset on every interaction. Use st.session_state to persist data across re-runs. The initialization pattern is: if "key" not in st.session_state: st.session_state["key"] = default_value.

Streamlit provides layout components like st.columns for side-by-side content, st.sidebar for controls, and st.tabs for organizing views. Use st.set_page_config at the top of your script for page-wide settings.
```

Create 2–3 more files about topics you’ve learned (databases, HTML/CSS, embeddings, etc.).

---

## Step 2: Build the Search App

Create `search_app.py`:

```python
import streamlit as st
import chromadb
import os

st.set_page_config(page_title="Semantic Search", page_icon="🔍", layout="wide")

# --- ChromaDB Setup ---
@st.cache_resource  # Cache the client so it persists across re-runs
def get_collection():
    client = chromadb.PersistentClient(path="./search_db")
    return client.get_or_create_collection(name="course_docs")

collection = get_collection()

# --- Document Loading & Chunking ---
def load_and_chunk(directory, chunk_size=400, overlap=50):
    """Load text files and split into chunks."""
    chunks = []
    for filename in sorted(os.listdir(directory)):
        if not filename.endswith(('.txt', '.md')):
            continue
        filepath = os.path.join(directory, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Split by paragraphs (double newline)
        paragraphs = [p.strip() for p in content.split('\n\n') if p.strip()]

        for i, para in enumerate(paragraphs):
            chunks.append({
                "text": para,
                "source": filename,
                "chunk_id": f"{filename}_{i}",
                "chunk_index": i,
            })
    return chunks

# --- Sidebar: Ingestion Controls ---
with st.sidebar:
    st.title("📁 Document Manager")

    if st.button("🔄 Re-index Documents"):
        chunks = load_and_chunk("docs")
        if chunks:
            collection.upsert(
                documents=[c["text"] for c in chunks],
                metadatas=[{"source": c["source"], "chunk_index": str(c["chunk_index"])} for c in chunks],
                ids=[c["chunk_id"] for c in chunks],
            )
            st.success(f"Indexed {len(chunks)} chunks from {len(set(c['source'] for c in chunks))} files")
        else:
            st.warning("No .txt or .md files found in docs/ folder")

    st.metric("Documents in DB", collection.count())

    st.divider()
    n_results = st.slider("Results to show", 1, 10, 5)

# --- Main Search Interface ---
st.title("🔍 Semantic Search")
st.write("Search your course documents by meaning, not just keywords.")

query = st.text_input("Enter your search query", placeholder="How does authentication work?")

if query and collection.count() > 0:
    results = collection.query(
        query_texts=[query],
        n_results=min(n_results, collection.count())
    )

    st.subheader(f"Top {len(results['documents'][0])} Results")

    for i in range(len(results['documents'][0])):
        doc = results['documents'][0][i]
        metadata = results['metadatas'][0][i]
        distance = results['distances'][0][i]

        # Color-code by relevance
        if distance < 0.5:
            relevance = "🟢 High"
        elif distance < 1.0:
            relevance = "🟡 Medium"
        else:
            relevance = "🔴 Low"

        with st.container():
            col_meta, col_score = st.columns([3, 1])
            with col_meta:
                st.write(f"**{metadata['source']}** — chunk {metadata['chunk_index']}")
            with col_score:
                st.write(f"{relevance} (dist: {distance:.3f})")
            st.write(doc)
            st.divider()

elif collection.count() == 0:
    st.info("👈 Click 'Re-index Documents' in the sidebar to load your documents first.")
```

---

## Step 3: Run It

```bash
streamlit run search_app.py
```

1. Click "Re-index Documents" in the sidebar to load and embed your text files
2. Type a search query like "How does Streamlit handle state?"
3. See ranked results with source files, relevance indicators, and distance scores
4. Try queries that use different words than the documents contain

`[DIAGRAM PLACEHOLDER: Screenshot of the working search app showing a query, ranked results with source files and relevance indicators, and the sidebar with document count and controls]`

You now have a complete semantic search tool. In the module project, you’ll expand this with a larger document collection and chunking experiments.