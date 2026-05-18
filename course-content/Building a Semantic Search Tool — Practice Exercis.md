# Building a Semantic Search Tool — Practice Exercise

## Expanded Search Tool

**Objective:** Extend the Guided Example’s search tool with additional features that prepare you for the module project.

**Time:** 40 minutes

**What you’ll do:**

1. Start with the search app from the Guided Example (or build a fresh one)
2. Create at least **5 document files** in your `docs/` folder covering different course topics
3. Add these features to the Streamlit app:

**Required features:**

- **Source filter** in the sidebar: a multiselect that lets users search only within specific files (use ChromaDB’s `where` parameter)
- **Result count display**: "Showing 5 of 23 total documents"
- **Expandable full text**: Each result shows a preview (first 150 chars), with an `st.expander` to see the full chunk

**Bonus features (pick at least one):**

- A "Similar to this" button on each result that uses that result’s text as a new query
- Display the relevance as a colored badge (green/yellow/red) based on distance thresholds
- Show the total number of unique source files in the sidebar

**Deliverable:** A running Streamlit search app with source filtering, result counts, and expandable previews.

**Why this exercise?** You’re building incrementally toward the module project. Each feature you add here is one less you’ll need to build from scratch for the Semantic Search Engine project.