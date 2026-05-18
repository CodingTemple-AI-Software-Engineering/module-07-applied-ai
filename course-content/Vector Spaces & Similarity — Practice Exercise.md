# Vector Spaces & Similarity — Practice Exercise

## Similarity Threshold Experiment

**Objective:** Explore how different similarity thresholds affect search quality, building intuition for tuning search systems.

**Time:** 25 minutes

**What you’ll do:**

1. Create a file called `threshold_experiment.py`
2. Define a knowledge base of at least **15 sentences** covering 3-4 distinct topics (e.g., Python development, cooking, space, music)
3. Define **5 test queries** — some clearly matching one topic, some ambiguous
4. For each query, compute similarity scores against all documents
5. Display results at **three different thresholds**: 0.3, 0.5, and 0.7
6. For each threshold, show:
    - How many results pass the threshold
    - Which results are included
    - Which relevant results are *missed* at strict thresholds

**Expected output format:**

```
Query: "How do I deploy my Python app?"

  Threshold 0.3: 6 results
    [0.72] Deploy FastAPI with uvicorn and Docker
    [0.65] Python web frameworks comparison
    [0.48] Setting up a virtual environment
    [0.41] Git basics for version control
    [0.35] Writing automated tests with pytest
    [0.31] SQL database migration strategies

  Threshold 0.5: 3 results
    [0.72] Deploy FastAPI with uvicorn and Docker
    [0.65] Python web frameworks comparison

  Threshold 0.7: 1 result
    [0.72] Deploy FastAPI with uvicorn and Docker
```

**Deliverable:** A working script that demonstrates how threshold choice affects result quantity and relevance.

**Why this exercise?** Threshold tuning is a critical skill for building search systems. Too strict and you miss relevant results. Too loose and you return noise. This experiment builds intuition you’ll apply in the module project.