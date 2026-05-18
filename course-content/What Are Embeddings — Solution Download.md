# What Are Embeddings? — Solution Download

**GitHub:** `module-07-applied-ai/solutions/exercises/course-search/`

Compare your solution to the reference. Key things to check:

- Did you embed the documents *once* outside the search loop (not on every query)?
- Are your results sorted by similarity score (highest first)?
- Does searching with different words than your documents still return relevant results?
- Does the loop exit cleanly when the user types "quit"?

Your document list and search queries will be different from the reference. The important thing is that semantically related queries return relevant results.