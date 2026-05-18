# Prompt Engineering Basics — Quiz

**Module 7 — Applied AI: Embeddings & Retrieval**

---

**Question 1:** What is the primary purpose of giving an AI model a "role" in a prompt?

- A) To make the AI pretend to be a different company’s product
- B) To focus the model’s response style, vocabulary, and depth to match a specific context and audience
- C) To bypass the model’s safety filters
- D) Roles have no effect on the model’s output

> **Answer: B** — Framing with a role tells the model what kind of response to generate. "You are a senior Python developer" produces technical, precise code. "You are a patient teacher for beginners" produces simple explanations with analogies. The model adjusts its vocabulary, depth, and assumptions based on the role.
> 

---

**Question 2:** What is "few-shot prompting"?

- A) Limiting the model to a few words of output
- B) Providing a few input/output examples in the prompt so the model learns the desired pattern and continues it
- C) Asking the model the same question multiple times
- D) Using a small AI model instead of a large one

> **Answer: B** — Few-shot prompting gives the model 2–5 examples of the desired input → output transformation. The model identifies the pattern and applies it to new inputs. This is especially effective for formatting conversions, classifications, and ensuring consistent output structure — because showing is more reliable than telling.
> 

---

**Question 3:** In a RAG application, what role does the system prompt play?

- A) It generates the embeddings for the documents
- B) It tells the model how to use the retrieved context — for example, to answer only from the provided documents and admit when it doesn’t know
- C) It stores the documents in ChromaDB
- D) It replaces the need for retrieval entirely

> **Answer: B** — The system prompt is the instruction layer that tells the model HOW to use the context provided by the retrieval system. A good RAG system prompt says: "Answer based ONLY on the provided context. If the answer isn’t in the context, say you don’t know." Without this instruction, the model might ignore the retrieved documents and hallucinate from its training data.
>