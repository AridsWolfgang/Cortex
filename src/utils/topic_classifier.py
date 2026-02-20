"""
Intelligent topic classification for user queries.
"""

import re
from typing import List, Tuple

class TopicClassifier:
    """Classifies user queries into relevant knowledge domains."""
    
    def __init__(self):
        self.topic_keywords = {
            'mathematics': [
                'math', 'algebra', 'calculus', 'geometry', 'equation',
                'derivative', 'integral', 'theorem', 'proof', 'number'
            ],
            'economics': [
                'economy', 'supply', 'demand', 'market', 'inflation',
                'gdp', 'microeconomics', 'macroeconomics', 'trade'
            ],
            'business': [
                'business', 'management', 'strategy', 'marketing',
                'leadership', 'entrepreneurship', 'operations'
            ],
            'finance': [
                'finance', 'investment', 'stock', 'bond', 'portfolio',
                'risk', 'return', 'dividend', 'interest', 'compound'
            ],
            'programming': [
                'code', 'programming', 'algorithm', 'function',
                'python', 'java', 'javascript', 'c++', 'rust',
                'software', 'development', 'debug'
            ],
            'history': [
                'history', 'historical', 'century', 'ancient',
                'medieval', 'war', 'revolution', 'empire', 'civilization'
            ],
            'art': [
                'art', 'painting', 'sculpture', 'artist', 'gallery',
                'museum', 'renaissance', 'modern', 'abstract'
            ],
            'engineering': [
                'engineering', 'circuit', 'voltage', 'current',
                'resistor', 'capacitor', 'electrical', 'electronic',
                'signal', 'system'
            ]
        }
        
    def classify(self, query: str) -> List[str]:
        """
        Classify the query into relevant topics.
        
        Returns:
            List of relevant topic names
        """
        query_lower = query.lower()
        matched_topics = []
        
        for topic, keywords in self.topic_keywords.items():
            for keyword in keywords:
                if re.search(rf'\b{keyword}\b', query_lower):
                    matched_topics.append(topic)
                    break
                    
        return matched_topics if matched_topics else ['general']
        
    def get_topic_confidence(self, query: str) -> List[Tuple[str, float]]:
        """Get confidence scores for each topic."""
        query_lower = query.lower()
        scores = []
        
        for topic, keywords in self.topic_keywords.items():
            score = sum(1 for keyword in keywords 
                       if re.search(rf'\b{keyword}\b', query_lower))
            score = min(1.0, score / 3)  # Normalize
            scores.append((topic, score))
            
        return sorted(scores, key=lambda x: x[1], reverse=True)