# What Are Embeddings? — Practice Exercise

## Course Content Search

**Objective:** Build a simple semantic search tool over content from modules you’ve already completed, demonstrating how embeddings find relevant results by meaning.

**Time:** 25 minutes

**What you’ll do:**

1. Create a file called `course_search.py`
2. Define a list of at least **10 sentences** summarizing things you’ve learned in this course. For example:
    - "HTML uses tags to define the structure of a web page"
    - "CSS Flexbox arranges elements in rows or columns"
    - "FastAPI automatically validates request data using Pydantic models"
    - "Streamlit re-runs the entire Python script when any widget is interacted with"
    - "JWT tokens provide stateless authentication for REST APIs"
    - (add at least 5 more from modules you’ve completed)
3. Embed all sentences using `SentenceTransformer('all-MiniLM-L6-v2')`
4. Implement a search loop that:
    - Asks the user for a query (using `input()`)
    - Embeds the query
    - Finds and displays the **top 3 most similar** sentences with their similarity scores
    - Continues until the user types "quit"
5. Test with queries that use *different words* than your sentences. For example, if you have "CSS Flexbox arranges elements in rows," try searching "how to put items side by side on a webpage."

**Deliverable:** A working `course_search.py` that performs interactive semantic search over your course summaries.

**Expected interaction:**

```
Search (or 'quit'): how do I make my API check if data is valid?

Top 3 results:
  1. [0.6823] FastAPI automatically validates request data using Pydantic models
  2. [0.4512] Pydantic schemas define what valid data looks like
  3. [0.3891] Error handling in FastAPI returns clear messages for invalid requests

Search (or 'quit'): quit
```

**Why this exercise?** You’re building the core pattern that powers every semantic search system: embed documents once, embed queries on the fly, compare by similarity. The rest of this module adds scale (ChromaDB), strategy (chunking), and evaluation.