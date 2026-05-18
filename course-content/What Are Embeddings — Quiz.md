# What Are Embeddings? — Quiz

**Module 7 — Applied AI: Embeddings & Retrieval**

---

**Question 1:** What is an embedding in the context of AI?

- A) A compressed image file format
- B) A list of numbers (vector) that represents the meaning of text, where similar meanings produce similar vectors
- C) A database that stores text documents
- D) A type of encryption for securing API keys

> **Answer: B** — An embedding converts text into a numerical vector that captures semantic meaning. The key property is that texts with similar meanings get similar vectors, so "build an API" and "create a web service" would have vectors close together, while "best pizza recipe" would be far away. This enables computers to compare meaning mathematically.
> 

---

**Question 2:** What is the fundamental difference between keyword search and semantic search?

- A) Keyword search is faster; semantic search is slower
- B) Keyword search matches exact words; semantic search matches meaning, finding relevant results even when the specific words differ
- C) Keyword search only works in English; semantic search works in all languages
- D) There is no meaningful difference

> **Answer: B** — Keyword search requires the exact words from the query to appear in the document. Semantic search converts both the query and documents to embeddings and compares their meaning vectors. This means searching for "how to build a REST API" can find a document titled "creating web services with Python" — same meaning, different words. This is why semantic search is transformative for AI applications.
> 

---

**Question 3:** Why does the "King - Man + Woman = Queen" example matter?

- A) It proves that AI understands grammar
- B) It demonstrates that embeddings capture relationships between concepts, not just individual word meanings
- C) It shows that embeddings are perfectly accurate
- D) It only works with English words

> **Answer: B** — This example shows that the vector space captures abstract relationships (like "royalty" and "gender") as directions. The relationship between "king" and "man" is encoded the same way as between "queen" and "woman." This means embeddings don’t just know what words mean in isolation — they encode how concepts relate to each other, which is what makes them so powerful for search and reasoning.
> 

---

**Question 4:** When you call `model.encode("Hello world")`, what do you get back?

- A) A translated version of the text in another language
- B) A summary of the text
- C) A list of hundreds of numbers (a vector) representing the meaning of the text
- D) A boolean indicating whether the text is valid

> **Answer: C** — `model.encode()` returns a numerical vector — typically 384 or 768 numbers, depending on the model. Each number represents some learned aspect of the text’s meaning. This vector can then be compared to other vectors using cosine similarity to find semantically similar text.
>