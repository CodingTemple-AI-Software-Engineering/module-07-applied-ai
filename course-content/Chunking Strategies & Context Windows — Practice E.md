# Chunking Strategies & Context Windows — Practice Exercise

## Chunk and Compare

**Objective:** Chunk a real document using two different strategies, embed both sets, and compare which strategy produces better search results for the same queries.

**Time:** 30 minutes

**What you’ll do:**

1. Create a file called `chunk_compare.py`
2. Use the following document text (or write your own 500+ word document summarizing what you’ve learned in this course):

```python
# Copy a substantial text ~500-800 words covering multiple topics.
# You can paste content from your Module 5 or Module 6 notes,
# or write a multi-paragraph summary of course concepts.
```

1. Implement **two chunking strategies:**
    - Fixed-size (300 characters, 50 character overlap)
    - Paragraph-based (split on double newlines)
2. Embed all chunks from both strategies
3. Run **3 different queries** against both sets
4. For each query, display the **top 2 results** from each strategy with scores
5. At the bottom, write a brief comparison: which strategy performed better and why?

**Deliverable:** A working script that demonstrates the practical impact of chunking strategy on search quality, with your written analysis.

**Why this exercise?** In the module project, you’ll need to choose a chunking strategy for a real document collection. This exercise builds the instinct for when to use which approach.