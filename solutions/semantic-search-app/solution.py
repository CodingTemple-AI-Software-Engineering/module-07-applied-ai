"""
L7 — Expanded Semantic Search App  (SOLUTION)
==============================================
Run with:
    streamlit run solution.py

Expects a docs/ folder containing .txt or .md files in the same directory.
"""

import streamlit as st
import chromadb
from pathlib import Path
from sentence_transformers import SentenceTransformer

DOCS_DIR   = Path(__file__).parent / "docs"
CHUNK_SIZE = 500
OVERLAP    = 100
N_RESULTS  = 5

# ── Page config ───────────────────────────────────────────────────────────────
st.set_page_config(page_title="Semantic Search", page_icon="🔍", layout="wide")


# ── Model & ChromaDB ──────────────────────────────────────────────────────────
@st.cache_resource
def load_resources():
    model      = SentenceTransformer("all-MiniLM-L6-v2")
    client     = chromadb.PersistentClient(path=str(Path(__file__).parent / "chroma_db"))
    collection = client.get_or_create_collection("docs_search")
    return model, collection


model, collection = load_resources()


# ── Chunking ──────────────────────────────────────────────────────────────────
def chunk_text(text: str, size: int = CHUNK_SIZE, overlap: int = OVERLAP) -> list[str]:
    """Fixed-size chunking with overlap."""
    chunks = []
    start  = 0
    while start < len(text):
        chunks.append(text[start:start + size])
        start += size - overlap
    return chunks


def index_docs():
    """Read docs/ folder and upsert all chunks into ChromaDB."""
    if not DOCS_DIR.exists():
        st.warning(f"No `docs/` folder found at {DOCS_DIR}. Create one and add .txt or .md files.")
        return

    all_ids, all_docs, all_metas, all_embeds = [], [], [], []

    for file in sorted(DOCS_DIR.glob("*.txt")) + sorted(DOCS_DIR.glob("*.md")):
        text   = file.read_text(encoding="utf-8")
        chunks = chunk_text(text)
        for i, chunk in enumerate(chunks):
            all_ids.append(f"{file.name}_chunk_{i}")
            all_docs.append(chunk)
            all_metas.append({"source": file.name})

    if all_ids:
        embeddings = model.encode(all_docs).tolist()
        collection.upsert(
            ids=all_ids,
            documents=all_docs,
            metadatas=all_metas,
            embeddings=embeddings,
        )


# Index once per session
if "indexed" not in st.session_state:
    with st.spinner("Indexing documents..."):
        index_docs()
    st.session_state.indexed = True


# ── Sidebar ───────────────────────────────────────────────────────────────────
st.sidebar.header("Filters")

all_metas    = collection.get(include=["metadatas"])["metadatas"]
all_sources  = sorted({m["source"] for m in all_metas}) if all_metas else []
total_unique = len(all_sources)

st.sidebar.metric("Unique source files", total_unique)

selected_sources = st.sidebar.multiselect(
    "Filter by source",
    options=all_sources,
    default=[],
    placeholder="All sources",
)

# ── Main UI ───────────────────────────────────────────────────────────────────
st.title("🔍 Semantic Search")
st.caption("Powered by ChromaDB + sentence-transformers")

query = st.text_input("Search your documents", placeholder="Type a question or phrase...")

if query:
    # Build where filter only when a non-empty subset is selected
    where = None
    if selected_sources and selected_sources != all_sources:
        where = {"source": {"$in": selected_sources}}

    results = collection.query(
        query_texts=[query],
        n_results=N_RESULTS,
        where=where,
        include=["documents", "metadatas", "distances"],
    )

    docs_    = results["documents"][0]
    metas_   = results["metadatas"][0]
    dists_   = results["distances"][0]
    total    = collection.count()

    st.caption(f"Showing {len(docs_)} of {total} total chunks")

    for doc, meta, dist in zip(docs_, metas_, dists_):
        source = meta["source"]

        # Relevance badge based on distance
        if dist < 0.3:
            badge = "🟢 High"
        elif dist < 0.6:
            badge = "🟡 Medium"
        else:
            badge = "🔴 Low"

        st.subheader(f"{source}  —  dist: {dist:.4f}  {badge}")
        st.write(doc[:150] + "...")

        with st.expander("Show full text"):
            st.write(doc)
