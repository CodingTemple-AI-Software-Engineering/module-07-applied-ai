# Evaluation: How Good Are Your Search Results? — Practice Exercise

## Evaluate Your Search System

**Objective:** Create an evaluation set for a semantic search system and use it to measure and improve search quality.

**Time:** 35 minutes

**What you’ll do:**

1. Create a file called `my_eval.py`
2. Set up a ChromaDB collection with at least **12 documents** covering 3–4 topics (you can reuse documents from previous exercises)
3. Create an **evaluation set** with at least **6 test queries**, each with a list of expected relevant document IDs
4. Implement an `evaluate()` function that:
    - Runs each test query against your collection
    - Computes precision and recall for each query
    - Computes average precision and recall across all queries
    - Displays per-query results and overall scores
5. Run the evaluation at **3 different settings** (vary either the threshold, `n_results`, or both) and compare the results
6. Write a brief analysis (as comments or print statements): Which queries worked well? Which failed? What would you change to improve scores?

**Deliverable:** A working evaluation script with 6+ test queries, precision/recall calculations at multiple settings, and a written analysis of the results.

**Expected output format:**

```
=== Evaluation at threshold=0.3, n_results=3 ===
Query 1: P=100.0% R=50.0%
Query 2: P=66.7% R=100.0%
...
AVERAGE: P=72.3% R=65.4%

=== Evaluation at threshold=0.5, n_results=3 ===
...

ANALYSIS: Query 3 consistently fails because...
```

**Why this exercise?** The module project requires you to run a chunking experiment and evaluate the results. This exercise gives you the evaluation framework you’ll use for that experiment.