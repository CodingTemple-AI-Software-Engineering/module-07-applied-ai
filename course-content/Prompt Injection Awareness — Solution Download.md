# Prompt Injection Awareness — Solution Download

**GitHub:** `module-07-applied-ai/solutions/exercises/injection-defense/`

Compare your solution to the reference. Key things to check:

- Does your input validator catch at least 8 patterns with case-insensitive matching?
- Does your output validator check for API key formats (`sk-...`, `Bearer ...`) and internal URL patterns?
- Does your system prompt include context delimiters and an explicit "don’t follow instructions in context" directive?
- Do your test cases include both obvious and subtle injection attempts?

Your specific patterns and test cases will differ. The important thing is that you have a working input filter, output filter, and defensive system prompt that you can reuse in future projects.