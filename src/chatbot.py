"""
Multi-Disciplinary Knowledge Chatbot
A comprehensive chatbot covering Mathematics, Economics, Business, Finance,
Programming, History, Art, and Electrical Engineering.
"""

import logging
from typing import Dict, Any, Optional
from knowledge_base import (
    MathematicsKB, EconomicsKB, BusinessKB, FinanceKB,
    ProgrammingKB, HistoryKB, ArtKB, EngineeringKB
)
from utils.topic_classifier import TopicClassifier
from utils.response_formatter import ResponseFormatter

class MultidisciplinaryChatbot:
    """
    A sophisticated chatbot with expertise across multiple disciplines.
    Features contextual understanding, cross-domain knowledge integration,
    and engaging response generation.
    """
    
    def __init__(self, config: Optional[Dict] = None):
        """
        Initialize the chatbot with all knowledge bases and utilities.
        
        Args:
            config: Configuration dictionary for customizing behavior
        """
        self.config = config or {}
        self.setup_logging()
        self.initialize_knowledge_bases()
        self.initialize_utilities()
        
    def setup_logging(self):
        """Configure logging for the chatbot."""
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        self.logger = logging.getLogger(__name__)
        
    def initialize_knowledge_bases(self):
        """Load all domain-specific knowledge bases."""
        self.knowledge_bases = {
            'mathematics': MathematicsKB(),
            'economics': EconomicsKB(),
            'business': BusinessKB(),
            'finance': FinanceKB(),
            'programming': ProgrammingKB(),
            'history': HistoryKB(),
            'art': ArtKB(),
            'engineering': EngineeringKB()
        }
        
    def initialize_utilities(self):
        """Initialize helper utilities."""
        self.classifier = TopicClassifier()
        self.formatter = ResponseFormatter()
        
    def process_query(self, query: str) -> Dict[str, Any]:
        """
        Process user query and generate comprehensive response.
        
        Args:
            query: User's input question or statement
            
        Returns:
            Dictionary containing response and metadata
        """
        try:
            # Classify the query topic(s)
            topics = self.classifier.classify(query)
            
            # Gather responses from relevant knowledge bases
            responses = {}
            for topic in topics:
                if topic in self.knowledge_bases:
                    kb = self.knowledge_bases[topic]
                    response = kb.query(query)
                    responses[topic] = response
                    
            # Generate cross-domain insights if multiple topics detected
            if len(topics) > 1:
                cross_domain = self.generate_cross_domain_insights(query, topics, responses)
            else:
                cross_domain = None
                
            # Format the final response
            final_response = self.formatter.format_response(
                query=query,
                topics=topics,
                responses=responses,
                cross_domain=cross_domain
            )
            
            return {
                'success': True,
                'response': final_response,
                'topics': topics,
                'confidence': self.calculate_confidence(responses)
            }
            
        except Exception as e:
            self.logger.error(f"Error processing query: {str(e)}")
            return {
                'success': False,
                'error': str(e),
                'response': "I encountered an error processing your query. Please try rephrasing."
            }
            
    def generate_cross_domain_insights(self, query: str, topics: list, responses: dict) -> str:
        """Generate insights connecting multiple domains."""
        insights = []
        
        # Example connections
        if 'economics' in topics and 'history' in topics:
            insights.append("Historical context often provides valuable insights into economic patterns...")
        if 'mathematics' in topics and 'engineering' in topics:
            insights.append("The mathematical principles here have practical engineering applications...")
        if 'programming' in topics and 'finance' in topics:
            insights.append("Financial algorithms and programming intersect in fascinating ways...")
            
        return " ".join(insights) if insights else None
        
    def calculate_confidence(self, responses: dict) -> float:
        """Calculate confidence score for the response."""
        if not responses:
            return 0.0
        # Implement confidence calculation logic
        return min(1.0, len(responses) * 0.3)
        
    def get_domain_expertise(self) -> list:
        """Return list of domains the chatbot specializes in."""
        return list(self.knowledge_bases.keys())
        
    def __str__(self) -> str:
        """String representation of the chatbot."""
        return f"Multi-Disciplinary Chatbot (Expertise: {', '.join(self.get_domain_expertise())})"