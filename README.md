# 🧠 Cortex - Multi-Disciplinary Knowledge Chatbot

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![Contributions Welcome](https://img.shields.io/badge/contributions-welcome-brightgreen)](CONTRIBUTING.md)

![Cortex Banner](/cortex.png)

## 🌟 Overview

Welcome to the **Cortex Multi-Disciplinary Knowledge Chatbot** – your intelligent companion spanning **8 diverse domains** of human knowledge. This isn't just another chatbot; it's a bridge connecting mathematics, economics, business, finance, programming, history, art, and electrical engineering into one coherent, engaging conversational experience.

### Why This Project is Fascinating

- **🧮 Mathematics** – From prime numbers to complex analysis
- **📊 Economics** – Market dynamics to game theory
- **💼 Business** – Strategy, management, and innovation
- **💰 Finance** – Investment, risk, and wealth creation
- **💻 Programming** – Low-level to high-level languages
- **📜 History** – Ancient civilizations to modern events
- **🎨 Art** – Renaissance to contemporary digital art
- **⚡ Engineering** – Circuits, systems, and innovation

## 🚀 Features

### Core Capabilities

- **Cross-Domain Integration**: Understands how economics influences history, how mathematics powers programming, and how art inspires engineering
- **Contextual Awareness**: Remembers conversation context for meaningful follow-ups
- **Intelligent Topic Classification**: Automatically identifies and switches between domains
- **Engaging Responses**: Not just facts, but fascinating connections and insights

### Unique Selling Points

- **The "Aha!" Factor**: Discover unexpected connections between disciplines
- **Practical Applications**: Real-world examples and use cases
- **Depth & Breadth**: Expert-level knowledge with accessible explanations
- **Interactive Learning**: Quiz mode, problem-solving, and guided exploration

## 🏗️ Architecture

```
┌─────────────────────────────────────┐
│         User Interface              │
│  (CLI, Web, API, Discord, etc.)     │
└───────────────┬─────────────────────┘
                │
┌───────────────▼─────────────────────┐
│      Intelligent Router             │
│   - Topic Classification            │
│   - Context Management              │
│   - Query Processing                │
└───────────────┬─────────────────────┘
                │
┌───────────────▼─────────────────────────┐
│         Knowledge Bases                 │
├─────────────┬───────────────┬───────────┤
│ Mathematics │  Economics    │Business   │
├─────────────┼───────────────┼───────────┤
│  Finance    │  Programming  │History    │
├─────────────┼───────────────┼───────────┤
│    Art      │  Engineering  │  ...      │
└─────────────┴───────────────┴───────────┘
```

## 🎯 Getting Started

### Prerequisites

- Python 3.8 or higher
- pip package manager
- Virtual environment (recommended)

### Installation

```bash
# Clone the repository
git clone https://github.com/AridsWolfgang/Cortex
cd Cortex

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the chatbot
python src/main.py
```

## 💡 Usage Examples

### Example 1: Cross-Domain Question

```python
from chatbot import MultidisciplinaryChatbot

bot = MultidisciplinaryChatbot()
response = bot.process_query(
    "How did the Fibonacci sequence influence both Renaissance art and modern algorithm design?"
)
print(response)
```

### Example 2: Deep Dive into a Topic

```python
# Explore the connection between chaos theory and stock market behavior
response = bot.process_query(
    "Explain how mathematical chaos theory applies to financial market volatility"
)
```

## 🧪 Interactive Demo

Try these fascinating queries:

- "What's the relationship between prime numbers and RSA encryption?"
- "How did ancient Greek geometry influence Renaissance art?"
- "Explain the Black-Scholes model like I'm 10"
- "What do quantum computing and classical economics have in common?"

## 🤝 Contributing

This project thrives on community contributions! Here's how you can help:

### Ways to Contribute

1. **Add Knowledge** – Expand our databases with your expertise
2. **Improve Algorithms** – Enhance topic classification and response generation
3. **Create Interfaces** – Build new UIs (web, mobile, voice, etc.)
4. **Fix Bugs** – Help us squash those pesky issues
5. **Write Tests** – Ensure reliability across all domains
6. **Documentation** – Make the project more accessible
7. **Share Ideas** – Suggest new features and connections

### Contribution Guidelines

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📚 Knowledge Base Structure

Each domain has its own module with:

- **Core Concepts**: Fundamental principles and theories
- **Advanced Topics**: Deep dives into specialized areas
- **Practical Applications**: Real-world use cases
- **Historical Context**: How knowledge evolved
- **Cross-Connections**: Links to other domains

## 🎓 Learning Paths

Follow curated learning journeys:

- **📈 From Math to Finance** → Start with calculus → Options pricing → Risk management
- **💻 Programming + Art** → Basic coding → Creative coding → Generative art
- **🔌 Physics to Engineering** → Electromagnetism → Circuit design → System architecture

## 🛣️ Roadmap

### Phase 1 (Current) - Foundation

- [x] Basic architecture
- [x] Topic classification
- [x] Initial knowledge bases

### Phase 2 - Enhancement

- [ ] Machine learning for better responses
- [ ] User preference learning
- [ ] Multi-language support

### Phase 3 - Advanced Features

- [ ] Voice interface
- [ ] Image generation for art/history
- [ ] Real-time data integration (stock prices, news)
- [ ] Collaborative problem-solving

## 📊 Project Metrics

- **8** Knowledge Domains
- **50+** Sub-domains
- **1000+** Core Concepts
- **∞** Possible Connections

## 🤔 Why Contribute?

- **Learn While Building** – Deepen your understanding across disciplines
- **Impact** – Help create a valuable educational resource
- **Community** – Join passionate learners and experts
- **Portfolio** – Showcase your skills in a unique project
- **Fun** – Discover fascinating connections yourself!

## 📝 License

Distributed under the MIT License. See `LICENSE` for more information.

## 🙏 Acknowledgments

- Inspired by polymaths throughout history
- Built with passion for interdisciplinary learning
- Supported by the open-source community

## 📬 Contact & Community

- **Discord**: [Join our server](https://discord.gg/...)
- **Twitter**: [@Cortex](https://twitter.com/...)
- **GitHub Issues**: For bugs and feature requests
- **Discussions**: For ideas and collaborations

---

<div align="center">
  
**"The most interesting discoveries happen at the intersections of disciplines."**

[Star this repo](https://github.com/AridsWolfgang/Cortex) ⭐ | [Report bug](https://github.com/AridsWolfgang/Cortex/issues) 🐛 | [Request feature](https://github.com/AridsWolfgang/Cortexissues) 🚀

</div>
```