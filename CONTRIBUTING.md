# Contributing to Cortex 🧠

Thank you for considering contributing to **Cortex** — an open-source multi-disciplinary knowledge acquisition engine!  
Whether you're fixing a typo, adding a fascinating cross-domain insight, expanding a knowledge base, improving the router logic, or suggesting a new learning journey, your help makes Cortex a better tool for curious minds everywhere.

This project is still in its **early foundation phase** (Phase 1), so contributions of **all sizes** are especially valuable and usually merge quickly.

## Table of Contents

- [Contributing to Cortex 🧠](#contributing-to-cortex-)
  - [Table of Contents](#table-of-contents)
  - [Code of Conduct](#code-of-conduct)
  - [How Can I Contribute?](#how-can-i-contribute)
    - [Non-Code Contributions (Great for Beginners!)](#non-code-contributions-great-for-beginners)
    - [Code Contributions](#code-contributions)
  - [Getting Started – Development Setup](#getting-started--development-setup)
  - [Contribution Workflow](#contribution-workflow)
  - [Coding \& Style Guidelines](#coding--style-guidelines)
  - [Commit Message Convention](#commit-message-convention)
  - [Pull Request Guidelines](#pull-request-guidelines)
  - [Where to Go for Help?](#where-to-go-for-help)
  - [Thank You!](#thank-you)

## Code of Conduct

We follow the [Contributor Covenant Code of Conduct v2.1](https://www.contributor-covenant.org/version/2/1/code_of_conduct/).  
Be kind, respectful, and constructive — we're all here to learn and build something meaningful.

## How Can I Contribute?

### Non-Code Contributions (Great for Beginners!)

These are fantastic starting points and have huge impact:

- **Expand knowledge bases**  
  Add new entries to domain modules (e.g., `src/knowledge_bases/mathematics.py` or future JSON files).  
  Example: Add concise explanations + cross-domain links like "How game theory (economics) appears in evolutionary biology (history of science)".

- **Suggest / write cross-domain insights**  
  Short, insightful one-liners or paragraphs that connect two or more domains.

- **Create or improve learning journeys**  
  Propose guided paths (e.g., "Finance → History → Programming: From tulip mania to blockchain via cryptographic primitives").

- **Improve documentation**  
  Fix typos, clarify examples, add more usage demos in README.md, or write tutorial-style explanations.

- **Report bugs or suggest features**  
  Open an issue with clear steps to reproduce (for bugs) or motivation + rough idea (for features).

- **Add tests**  
  Even simple ones for the router classification or Wikipedia fallback.

### Code Contributions

- Improve the **Intelligent Router** (better keyword matching, future ML classification with spaCy/transformers)
- Enhance context memory & follow-up handling
- Add new interactive modes (quizzes, Socratic questioning)
- Refactor for better modularity (e.g., load knowledge from JSON/YAML)
- Integrate early Phase 2 features (RAG basics, local LLM stubs)
- Performance / error-handling improvements

## Getting Started – Development Setup

1. Fork & clone the repo  
   ```bash
   git clone https://github.com/AridsWolfgang/Cortex.git
   cd Cortex
   ```

2. Create & activate virtual environment  
   ```bash
   python -m venv venv
   source venv/bin/activate   # Windows: venv\Scripts\activate
   ```

3. Install dependencies  
   ```bash
   pip install -r requirements.txt
   # Optional for dev: pip install pytest black isort
   ```

4. Run the chatbot to verify  
   ```bash
   python src/main.py
   ```

You're ready!

## Contribution Workflow

Standard GitHub flow:

1. **Find or create an issue**  
   Look for `good first issue`, `help wanted`, or open a new one.

2. **Create a branch** (clear name!)  
   ```bash
   git checkout -b add-fibonacci-insights-to-math-and-art
   # or fix/router-keyword-overlap
   ```

3. **Make changes**  
   Small & focused → one PR = one logical change.

4. **Commit** (see convention below)

5. **Push & open Pull Request**  
   ```bash
   git push origin add-fibonacci-insights-to-math-and-art
   ```
   Use a descriptive PR title & body. Reference any related issue (#123).

6. **Respond to feedback**  
   We'll review quickly — feel free to ask questions!

## Coding & Style Guidelines

- Python 3.8+
- Follow **PEP 8** (use `black` for auto-formatting if possible)
- Imports: standard library → third-party → local
- Docstrings: Google or NumPy style (especially for new functions/classes)
- Variable/function names: descriptive, snake_case
- Keep functions short & single-responsibility
- Add comments for non-obvious logic
- When adding knowledge: aim for concise (2–5 sentences), accurate, engaging tone + at least one cross-domain hook when relevant

Example snippet for a knowledge entry:

```python
"black-scholes": (
    "The Black-Scholes model prices European options assuming log-normal stock prices and constant volatility. "
    "Formula: ... (LaTeX if we add rendering later). "
    "Cross-domain note: Built on stochastic calculus (mathematics) and revolutionized risk management (finance → economics)."
)
```

## Commit Message Convention

Simple & clear:

```
Add golden ratio insight linking math, art, and programming

- New entry in mathematics knowledge base
- Cross-reference to Renaissance art & fractal algorithms
```

Or for fixes:

```
Fix router false-positive on "current events" → history instead of electrical
```

## Pull Request Guidelines

- Title: Summarize the change (e.g., "feat: add Ohm's law + signal-processing cross-insight to EE")
- Body:
  - What & why
  - How to test / example query
  - Screenshots if UI-related (future)
  - Checklist: [ ] Tests added? [ ] Docs updated? [ ] PEP8/black compliant?
- Link related issues: `Closes #45`

We love PRs that include:
- Before/after examples
- Why this knowledge/connection matters

## Where to Go for Help?

- Open a **Discussion** → https://github.com/AridsWolfgang/Cortex/discussions
- Comment on an existing issue
- Tag @AridsWolfgang in a PR or issue

No question is too small — we're excited to help you contribute!

## Thank You!

Every contribution — code, knowledge, typo fix, or idea — helps turn Cortex into a more powerful bridge between disciplines.  
You're helping people discover connections they might never have seen otherwise.

Happy contributing, and let's build something insightful together! 🚀

