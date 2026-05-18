# Prompt Injection Awareness — Practice Exercise

## Injection Defense Lab

**Objective:** Build input validation and output checking functions that could protect a RAG-powered application from common prompt injection attacks.

**Time:** 25 minutes

**What you’ll do:**

1. Create a file called `injection_defense.py`
2. Build an **input validator** function that:
    - Takes a user query string
    - Checks for at least 8 suspicious patterns (e.g., "ignore previous," "system prompt," "you are now," etc.)
    - Returns a tuple: `(is_safe: bool, reason: str)`
    - Handles case variations (uppercase, mixed case)
3. Build an **output validator** function that:
    - Takes a model response string
    - Checks for patterns that shouldn’t appear in responses (e.g., API key formats, internal URLs, the system prompt text itself)
    - Returns a tuple: `(is_safe: bool, flagged_patterns: list)`
4. Build a **safe system prompt** for a RAG assistant that includes:
    - Clear role framing
    - Context delimiters (`<context>` tags)
    - Explicit instruction to ignore commands in the context
    - Length constraints on the response
5. Test all three components with at least 5 test cases (mix of safe inputs, direct injections, and edge cases)

**Deliverable:** A working `injection_defense.py` with input/output validators and a safe system prompt template, demonstrated against test cases.

**Why this exercise?** Every AI application you build from here forward should include these defensive patterns. Building them now means they’re ready to drop into your Module 8 RAG pipeline and your capstone project.