# Module 7: Applied AI — Embeddings & Retrieval — Starter Kit

## Quick Setup

### Option A: Clone with Git
```bash
git clone <repo-url>
cd module-07-applied-ai
```

### Option B: Download ZIP (no Git required)
1. Go to this repo on GitHub
2. Click the green **Code** button
3. Click **Download ZIP**
4. Unzip the downloaded file and open the folder

---

### Shared steps (both options)

1. **Create a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate        # Mac/Linux
   venv\Scripts\activate           # Windows
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Start working:** Open any exercise folder and edit the starter file.

---

### Running the exercises

| Script type | Command |
|-------------|---------|
| Plain Python script | `python starter.py` |
| Streamlit app | `streamlit run starter.py` |

> **Note:** ChromaDB creates a `chroma_db/` folder in the current directory the
> first time it runs. This is normal — the data persists between runs so you
> don't have to re-index every time.

---

## Exercises

| # | Exercise | Folder | Key Packages |
|---|----------|--------|--------------|
| L1 | What Are Embeddings? | `exercises/course-search/` | **sentence-transformers**, **scikit-learn** |
| L2 | Vector Spaces & Similarity | `exercises/threshold-experiment/` | **sentence-transformers**, **scikit-learn** |
| L3 | Chunking Strategies | `exercises/chunk-compare/` | **sentence-transformers**, **scikit-learn** |
| L4 | Intro to ChromaDB | `exercises/knowledge-base/` | **chromadb** |
| L5 | Building a Semantic Search Tool | `exercises/semantic-search-app/` | **chromadb**, **sentence-transformers**, **streamlit** |
| L6 | Prompt Engineering Basics | `exercises/prompt-workshop/` | built-in only (optional: **openai**) |
| L7 | Prompt Injection Awareness | `exercises/injection-defense/` | built-in only |
| L8 | Evaluating Your Search System | `exercises/search-eval/` | **chromadb** |

---

## Module Project

The project is a **Document Search Engine** — a full Streamlit app backed by
ChromaDB that lets users upload documents, search semantically, and experiment
with chunking strategies.

### Setup
```bash
cd project/starter
pip install -r requirements.txt
```

### Ingest documents
```bash
python ingest.py               # default chunk size (500) and overlap (100)
python ingest.py --chunk-size 300 --overlap 50   # experiment with settings
```

### Run the app
```bash
streamlit run app.py
```

The starter includes:
- `app.py` — Streamlit UI skeleton
- `ingest.py` — document loading, chunking, and ChromaDB storage pipeline
- `search.py` — query and retrieval functions
- `evaluate.py` — precision/recall evaluation framework
- `docs/` — sample document corpus to get started

See the project brief on the course platform for full requirements and the
chunking experiment task.

---

## Solutions

Solutions are in the `solutions/` folder — one `solution.py` per exercise.
**Try each exercise yourself first!** Compare your approach after you've made
your attempt. Differences are fine — there are many valid ways to solve these
problems.

---
