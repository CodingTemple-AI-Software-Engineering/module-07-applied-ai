# Prompt Engineering Basics — Practice Exercise

## Prompt Workshop

**Objective:** Practice writing engineered prompts using framing, specificity, and few-shot examples, and observe how prompt quality affects output quality.

**Time:** 25 minutes

**What you’ll do:**

1. Create a file called `prompt_workshop.py`
2. For each of the **3 tasks** below, write **two prompts**: a “bad” prompt (vague, no framing) and a “good” prompt (using at least 2 of the 3 techniques)
3. Send both prompts to an API (or use the mock function from the Guided Example) and display the results side by side

**Task 1 — Code explanation:**

Get the model to explain what `st.session_state` does in Streamlit.

**Task 2 — Data formatting:**

Get the model to convert a natural language list of tasks into a JSON array with `title`, `priority`, and `status` fields.

**Task 3 — System prompt design:**

Write a system prompt for a "Course Study Assistant" that answers questions based on provided context from course notes. The system prompt should instruct the model to: use the provided context only, admit when it doesn’t know, keep answers under 150 words, and include which source document the answer came from.

**Deliverable:** A script that demonstrates 3 pairs of bad/good prompts with their outputs, plus a written system prompt for Task 3.

**Why this exercise?** In Module 8, your RAG pipeline will include a system prompt that tells the model how to use retrieved documents. Practicing prompt engineering now means your RAG system will produce better answers.