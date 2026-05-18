# Prompt Engineering Basics — Concept

**Module 7 — Applied AI: Embeddings & Retrieval**

**Estimated time: 30 minutes**

---

### Learning Objectives

By the end of this lesson, you will be able to:

1. Explain why how you phrase a request to an AI model affects the quality of the response
2. Apply three key techniques: framing (role/context), specificity (constraints), and examples (few-shot)
3. Structure prompts that produce consistently useful outputs from LLMs
4. Connect prompt engineering to the search and retrieval systems you’re building

---

`[VIDEO PLACEHOLDER: 6 min — "Prompt Engineering Basics: show the same question asked three different ways with dramatically different results. Demonstrate framing, specificity, and few-shot examples in action."]`

Imagine asking someone for directions. You could say: "How do I get there?" You’d probably get a confused look. But if you said: "I’m at the corner of 5th and Main, driving a car, and I need to get to the airport by 3pm. What’s the fastest route avoiding the highway?" — you’d get a useful answer.

The difference? **Context**, **specificity**, and **constraints**. The same principle applies to AI language models. The way you phrase your request — your **prompt** — dramatically affects the quality of the response.

This matters for two reasons in your work. First, you’ll use AI tools throughout your career, and better prompts save time. Second, when you build AI-powered applications, the prompts your system sends to the model are part of your code. A bad system prompt means bad results for every user, every time.

---

## Technique 1: Framing (Role and Context)

Giving the model a **role** and **context** focuses its response:

**Without framing:**

```
Explain embeddings.
```

The model might give a physics answer, a math answer, or an AI answer. It’s guessing what you want.

**With framing:**

```
You are a patient programming instructor teaching career changers 
who have completed a Python and FastAPI bootcamp. Explain what 
embeddings are in the context of AI and semantic search. 
Use analogies before technical terms.
```

Now the model knows: the audience (career changers), their background (Python + FastAPI), the domain (AI/semantic search), and the teaching style (analogies first). The response will be dramatically more useful.

Framing works because LLMs generate text that "fits" the context. If the context says "you are a senior engineer," the model generates text that sounds like a senior engineer. If it says "explain to a 5-year-old," you get simpler language.

---

## Technique 2: Specificity (Constraints and Format)

Vague prompts get vague answers. Specific prompts get specific answers.

**Vague:**

```
Write about databases.
```

**Specific:**

```
Write a 200-word comparison of SQL databases vs. vector databases 
for an AI engineering student. Include: what each stores, how each 
is queried, and when to use which. Format as a table.
```

The specific version constrains: length (200 words), audience (AI engineering student), content (stores/queries/use cases), and format (table). The model has clear guardrails.

Useful constraints include:

- **Length:** "In 3 sentences," "In under 100 words," "As a bullet list of 5 items"
- **Format:** "As a JSON object," "As a Python function," "As a markdown table"
- **Scope:** "Only cover X," "Don’t include Y," "Focus on Z"
- **Audience:** "For a beginner," "For a technical reviewer," "For a non-technical manager"

---

## Technique 3: Examples (Few-Shot Prompting)

Showing the model what you want is often more effective than describing it. This is called **few-shot prompting** — giving a few examples of the desired input/output pattern:

```
Convert these informal descriptions to Pydantic model fields:

Input: "the user's email"
Output: email: EmailStr

Input: "how old they are, must be 18+"
Output: age: int = Field(ge=18)

Input: "their full name"
Output: name: str = Field(min_length=1, max_length=100)

Input: "what department they work in"
Output:
```

The model sees the pattern (informal → Pydantic field with validation) and continues it. Few-shot prompting is extremely effective for:

- Formatting conversions (natural language → code, data → table)
- Classification tasks (categorizing text into predefined categories)
- Consistent output style (ensuring every response follows the same structure)

---

## The System Prompt: Your App’s Personality

When you build AI-powered applications, the **system prompt** is the instruction you give the model before the user’s message. It sets the model’s behavior for the entire conversation:

```python
messages = [
    {"role": "system", "content": "You are a helpful study assistant for AI "
     "engineering students. Answer questions based on the provided context. "
     "If the context doesn't contain the answer, say so honestly. "
     "Keep responses under 200 words."},
    {"role": "user", "content": user_question}
]
```

The system prompt is where framing, specificity, and constraints all come together. In Module 8, when you build a RAG pipeline, your system prompt will tell the model to answer *based on the retrieved documents* — not from its general knowledge.

---

## Why This Matters for Retrieval Systems

Prompt engineering connects directly to the search tools you’re building. When your semantic search returns relevant chunks, those chunks become the **context** in a prompt to an LLM. The quality of that prompt determines whether the model gives a grounded, useful answer or hallucinates.

A well-engineered prompt says: "Here are the relevant documents. Answer the user’s question based ONLY on this context. If the context doesn’t contain the answer, say you don’t know."

A poorly-engineered prompt says: "Answer this question." — and the model happily makes things up.

The retrieval quality (from your embeddings and ChromaDB) determines *what context* the model sees. The prompt quality determines *how the model uses* that context. Both matter.