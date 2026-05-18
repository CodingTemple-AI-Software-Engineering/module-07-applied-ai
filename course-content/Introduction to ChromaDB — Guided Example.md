# Introduction to ChromaDB — Guided Example

**Module 7 — Applied AI: Embeddings & Retrieval**

`[VIDEO PLACEHOLDER: 10 min — "ChromaDB Hands-On: install ChromaDB, create a collection, add documents with metadata, query by similarity, filter by metadata. Show the complete workflow from adding documents to searching."]`

Let’s build a complete ChromaDB workflow. Create a file called `chromadb_intro.py`:

---

## Step 1: Create a Client and Collection

```python
import chromadb

# Create a persistent client (data survives script restarts)
client = chromadb.PersistentClient(path="./chroma_demo")

# Create (or get) a collection
# If it already exists, get_or_create_collection returns the existing one
collection = client.get_or_create_collection(
    name="course_notes",
    metadata={"description": "AI Engineering Foundations course content"}
)

print(f"Collection '{collection.name}' ready.")
print(f"Current document count: {collection.count()}")
```

Run it once. You should see a count of 0. A `chroma_demo/` folder will appear in your project directory.

---

## Step 2: Add Documents

```python
# Course content chunks with metadata
documents = [
    "FastAPI is a modern Python web framework that automatically validates request data using Pydantic models and generates interactive API documentation.",
    "SQLAlchemy is an ORM that maps Python classes to database tables. It supports relationships like one-to-many and many-to-many.",
    "Streamlit re-runs the entire Python script every time a user interacts with a widget. Use st.session_state to persist data across re-runs.",
    "JWT tokens provide stateless authentication for REST APIs. The token contains encoded user information and is verified on each request.",
    "CSS Flexbox arranges child elements in a row or column. Use display:flex on the container and gap for spacing between items.",
    "The DOM is the browser's tree representation of an HTML page. JavaScript uses querySelector and addEventListener to interact with it.",
    "Embeddings convert text into numerical vectors that capture semantic meaning. Similar texts produce vectors that are close together.",
    "Cosine similarity measures the angle between two vectors. A score of 1.0 means identical direction (same meaning), 0.0 means unrelated.",
]

# Metadata for each document (source module, topic category)
metadatas = [
    {"module": "5", "topic": "api"},
    {"module": "3", "topic": "database"},
    {"module": "6", "topic": "frontend"},
    {"module": "5", "topic": "security"},
    {"module": "6", "topic": "frontend"},
    {"module": "6", "topic": "frontend"},
    {"module": "7", "topic": "ai"},
    {"module": "7", "topic": "ai"},
]

# Unique IDs for each document
ids = [f"doc_{i}" for i in range(len(documents))]

# Add to ChromaDB — it embeds them automatically!
collection.add(
    documents=documents,
    metadatas=metadatas,
    ids=ids
)

print(f"Added {len(documents)} documents.")
print(f"Collection now has {collection.count()} documents.")
```

Run it. ChromaDB automatically embeds each document using its default model. You didn’t need to call `model.encode()` — ChromaDB handled it.

**Important:** If you run this script again, you’ll get an error because the IDs already exist. Either delete the `chroma_demo/` folder first, or use `collection.upsert()` instead of `collection.add()` to update existing documents.

---

## Step 3: Query by Similarity

```python
# Search for documents similar to a query
results = collection.query(
    query_texts=["How do I make my API verify user identity?"],  # Your search query
    n_results=3  # Return top 3 matches
)

print("\n=== Search Results ===")
print(f"Query: 'How do I make my API verify user identity?'\n")

for i in range(len(results['documents'][0])):
    doc = results['documents'][0][i]
    distance = results['distances'][0][i]  # Lower distance = more similar
    metadata = results['metadatas'][0][i]
    doc_id = results['ids'][0][i]

    print(f"{i+1}. [distance: {distance:.4f}] (Module {metadata['module']}, {metadata['topic']})")
    print(f"   {doc[:100]}...")
    print()
```

You should see the JWT authentication document ranked first — even though the query says "verify user identity" and the document says "stateless authentication." Semantic search in action.

**Note:** ChromaDB returns **distances** (lower = more similar), not similarities (higher = more similar). This is the opposite of the cosine similarity scores you used earlier. A distance of 0 means identical; larger values mean less similar.

---

## Step 4: Filter by Metadata

ChromaDB supports filtering results by metadata:

```python
# Search only within Module 6 content
results_filtered = collection.query(
    query_texts=["How do I make my web page interactive?"],
    n_results=3,
    where={"module": "6"}  # Only search Module 6 documents
)

print("\n=== Filtered Results (Module 6 only) ===")
for i in range(len(results_filtered['documents'][0])):
    doc = results_filtered['documents'][0][i]
    metadata = results_filtered['metadatas'][0][i]
    print(f"{i+1}. [{metadata['topic']}] {doc[:100]}...")
```

Metadata filtering is powerful for scoping searches: search only within a specific module, category, date range, or source file.

---

## What You Should See

A working vector database that stores course content, returns relevant results by meaning, and supports metadata-based filtering. Run the query multiple times with different questions — the semantic search consistently finds relevant documents regardless of word choice.

`[DIAGRAM PLACEHOLDER: Screenshot showing the script output with search results, distance scores, and metadata displayed for a sample query]`