# Evaluation: How Good Are Your Search Results? — Quiz

**Module 7 — Applied AI: Embeddings & Retrieval**

---

**Question 1:** What does "precision" measure in a search system?

- A) How fast the search returns results
- B) Of the results returned, what percentage are actually relevant
- C) Of all relevant documents in the collection, what percentage were found
- D) The total number of documents searched

> **Answer: B** — Precision measures the quality of what you returned. If your search returns 5 results and 3 are relevant, precision is 60%. High precision means the user isn’t wading through junk. Low precision means too many irrelevant results. This is different from recall (C), which measures how many relevant documents you *found* out of all that exist.
> 

---

**Question 2:** You lower your similarity threshold from 0.5 to 0.2. What is the most likely effect?

- A) Both precision and recall increase
- B) Precision increases but recall decreases
- C) Recall increases but precision likely decreases, because you’re now including more loosely-related results
- D) No effect on either metric

> **Answer: C** — A lower threshold means more documents pass the filter, so you’re more likely to include all the relevant ones (higher recall). But you’re also including documents that are only loosely related (lower precision). This precision-recall tradeoff is fundamental to search systems — there’s no free lunch.
> 

---

**Question 3:** Why is an evaluation set (gold standard) necessary?

- A) ChromaDB requires it to function
- B) It provides a systematic, repeatable way to measure search quality against known correct answers, rather than relying on subjective "it looks right" judgments
- C) It improves the embedding model’s accuracy
- D) It’s only needed for production systems, not prototypes

> **Answer: B** — Without an evaluation set, you can only judge results by looking at them, which is biased (you test queries you expect to work) and not repeatable (did that last change make things better or worse?). An evaluation set with known relevant documents for each query gives you actual numbers to compare across experiments. It’s worth creating even for prototypes — the module project asks you to build one.
>