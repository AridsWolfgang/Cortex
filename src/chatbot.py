"""
 ██████╗ ██████╗ ██████╗ ████████╗███████╗██╗  ██╗
██╔════╝██╔═══██╗██╔══██╗╚══██╔══╝██╔════╝╚██╗██╔╝
██║     ██║   ██║██████╔╝   ██║   █████╗   ╚███╔╝ 
██║     ██║   ██║██╔══██╗   ██║   ██╔══╝   ██╔██╗ 
╚██████╗╚██████╔╝██║  ██║   ██║   ███████╗██╔╝ ██╗
 ╚═════╝ ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═╝  ╚═╝
                                                  
Cortex - Multi-Disciplinary Knowledge Chatbot
A comprehensive chatbot covering Mathematics, Economics, Business, Finance,
Programming, History, Art, and Electrical Engineering.
"""

import re
import wikipedia 

class MultidisciplinaryChatbot:
    def __init__(self):
        # Expanded keywords for better classification
        self.domains = {
            'mathematics': ['math', 'calculus', 'algebra', 'geometry', 'fibonacci', 'stochastic', 'derivative', 'equation'],
            'economics': ['economy', 'supply', 'demand', 'inflation', 'gdp', 'market'],
            'business': ['business', 'management', 'marketing', 'strategy', 'swot', 'entrepreneur'],
            'finance': ['finance', 'stock', 'investment', 'black-scholes', 'option', 'portfolio', 'risk'],
            'programming': ['programming', 'code', 'algorithm', 'python', 'java', 'debug', 'function'],
            'history': ['history', 'war', 'renaissance', 'revolution', 'empire', 'era'],
            'art': ['art', 'painting', 'sculpture', 'renaissance', 'impressionism', 'artist'],
            'electrical_engineering': ['electrical', 'circuit', 'voltage', 'current', 'resistor', 'transistor', 'ohm']
        }
        # Sample hard-coded knowledge for quick, accurate responses (expand as needed)
        self.knowledge_bases = {
            'mathematics': {
                'derivative': 'A derivative in calculus represents the instantaneous rate of change of a function. For example, the derivative of f(x) = x^2 is 2x.',
                'fibonacci sequence': 'The Fibonacci sequence is defined as F(0) = 0, F(1) = 1, and F(n) = F(n-1) + F(n-2) for n > 1. It appears in nature, art, and algorithms.',
                'black-scholes': 'While primarily finance, it uses stochastic calculus from math to model option prices.'  # Cross-reference example
            },
            'economics': {
                'supply and demand': 'Supply and demand is a model where the price of a good adjusts to balance the quantity supplied and demanded, leading to market equilibrium.',
            },
            'business': {
                'swot analysis': 'SWOT stands for Strengths, Weaknesses, Opportunities, and Threats—a framework for strategic planning.'
            },
            'finance': {
                'black-scholes': 'The Black-Scholes model prices European call and put options using variables like stock price, strike price, time to expiration, risk-free rate, and volatility.'
            },
            'programming': {
                'hello world in python': 'In Python, it\'s simply: print("Hello, World!")',
                'algorithm design': 'Algorithm design involves creating efficient steps to solve problems, often using data structures like trees or graphs.'
            },
            'history': {
                'renaissance': 'The Renaissance (14th-17th century) was a period of cultural, artistic, and scientific revival in Europe, starting in Italy.'
            },
            'art': {
                'renaissance art': 'Renaissance art emphasized realism, perspective, and humanism, influenced by math (e.g., golden ratio in Da Vinci\'s works).'
            },
            'electrical_engineering': {
                'ohms law': 'Ohm\'s Law states V = I * R, where V is voltage, I is current, and R is resistance.'
            }
        }
        self.context = []  # Store conversation history for future context-aware responses

    def classify_query(self, query):
        matched = set()  # Use set to avoid duplicates
        lower_query = query.lower()
        for domain, keywords in self.domains.items():
            for kw in keywords:
                if re.search(r'\b' + re.escape(kw) + r'\b', lower_query):
                    matched.add(domain)
                    break
        return list(matched) or ['general']

    def process_query(self, query):
        domains = self.classify_query(query)
        responses = []
        lower_query = query.lower()
        for domain in domains:
            if domain == 'general':
                responses.append("I'm not sure which domain this falls under. Can you provide more details?")
            else:
                kb = self.knowledge_bases.get(domain, {})
                found = False
                for key in sorted(kb, key=len, reverse=True):  # Match longer phrases first
                    if key in lower_query:
                        responses.append(f"In {domain.capitalize()}: {kb[key]}")
                        found = True
                if not found:
                    # Fallback to Wikipedia for dynamic knowledge
                    try:
                        wiki_summary = wikipedia.summary(query, sentences=3)
                        responses.append(f"In {domain.capitalize()} (from Wikipedia): {wiki_summary}")
                    except wikipedia.exceptions.PageError:
                        responses.append(f"In {domain.capitalize()}: No specific info found on '{query}'. Try rephrasing.")
                    except Exception as e:
                        responses.append(f"In {domain.capitalize()}: Error fetching info - {str(e)}.")

        if len(domains) > 1:
            responses.append("\nCross-domain insight: These areas often intersect. For example, math underpins finance models, and history influences art movements.")

        response = '\n'.join(responses)
        self.context.append(query)  # Add to context (future: use for follow-ups)
        return response