"""
L7 — Similarity Threshold Experiment  (SOLUTION)
=================================================
Run with:
    python solution.py
"""

from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# ── Knowledge base ────────────────────────────────────────────────────────────
knowledge_base = [
    # Python / software development
    "Python functions are defined with the 'def' keyword and can return any value.",
    "FastAPI uses type hints and Pydantic to validate request and response data automatically.",
    "Decorators wrap functions to add behaviour like logging or authentication.",
    "Virtual environments isolate Python dependencies between projects.",
    "Docker packages applications into containers so they run consistently on any machine.",

    # Cooking
    "Sautéing means cooking food quickly in a small amount of oil over high heat.",
    "Mise en place is a French technique meaning 'everything in its place' before cooking.",
    "Deglazing a pan with wine or stock lifts the caramelised bits for a flavourful sauce.",
    "Blanching vegetables in boiling water then plunging them in ice water preserves colour.",
    "Bread needs gluten development from kneading so the dough traps CO2 from the yeast.",

    # Space exploration
    "The James Webb Space Telescope uses infrared light to observe the earliest galaxies.",
    "A geostationary orbit keeps a satellite fixed above the same point on Earth.",
    "Mars has the largest volcano in the solar system — Olympus Mons.",
    "The Voyager 1 probe has crossed into interstellar space beyond the heliosphere.",
    "Astronauts on the ISS experience microgravity because they are in continuous free fall.",

    # Music
    "A chord progression in the key of C major often follows I–V–vi–IV.",
    "The circle of fifths is a diagram showing the relationships between musical keys.",
    "Dynamics in music refer to the variation in loudness between notes or phrases.",
    "Polyrhythm layers two or more conflicting rhythms simultaneously.",
    "A leitmotif is a recurring musical theme associated with a character or idea.",
]

# ── Test queries ──────────────────────────────────────────────────────────────
test_queries = [
    "How do I deploy my Python application?",           # clear match: software
    "What is the best way to brown meat in a pan?",     # clear match: cooking
    "Tell me about telescopes and distant galaxies.",   # clear match: space
    "How do musicians work with rhythm and keys?",     # clear match: music
    "What is the process for creating something from scratch?",  # ambiguous
]

# ── Thresholds ────────────────────────────────────────────────────────────────
THRESHOLDS = [0.3, 0.5, 0.7]

# ── Model & embeddings ────────────────────────────────────────────────────────
print("Loading model and embedding knowledge base...")
model = SentenceTransformer("all-MiniLM-L6-v2")
doc_embeddings = model.encode(knowledge_base)

# ── Run experiment ────────────────────────────────────────────────────────────
for query in test_queries:
    print(f'\nQuery: "{query}"')

    query_embedding = model.encode([query])
    scores = cosine_similarity(query_embedding, doc_embeddings)[0]

    for threshold in THRESHOLDS:
        passing = [
            (score, sentence)
            for score, sentence in zip(scores, knowledge_base)
            if score >= threshold
        ]
        passing.sort(reverse=True)

        print(f"\n  Threshold {threshold}: {len(passing)} result(s)")
        for score, sentence in passing:
            print(f"    [{score:.4f}] {sentence}")
        if not passing:
            print("    (no results above this threshold)")
