from pydantic import BaseModel, Field
from typing import List, Optional
from .base_model import Trend

class MarketSegmentationApproach(BaseModel):
    segmentation_criteria: str  # e.g., Producer vs. retailer vs. farmer, Geographic market
    approach_evolution: Trend # Targeting, prioritization, optimization, strategy
    notes: Optional[str] = None # e.g., Specialty vs. commodity, Sustainability leader vs. follower, Digital maturity-based

class ValuePropositionDifferentiation(BaseModel):
    differentiation_factor: str  # e.g., Technical depth, Outcome guarantee, Implementation support
    evolution_trend: Trend # Emphasis, consideration, distinctiveness, capability, approach
    notes: Optional[str] = None # e.g., Ecosystem orchestration, Integrated solution

class BusinessDevelopmentMethodology(BaseModel):
    methodology_element: str  # e.g., Industry network leverage, Thought leadership positioning
    evolution_trend: Trend # Leverage, positioning, presence, optimization, development
    notes: Optional[str] = None # e.g., Conference/field day presence, Digital marketing, Reference client program

class PartnershipEcosystemDevelopment(BaseModel):
    partner_type: str  # e.g., Technology provider, Academic institution, Industry association
    development_trend: Trend # Alliance formation, collaboration, engagement, relationships, connections
    notes: Optional[str] = None # e.g., Complementary service providers, Research organizations

class PricingStrategyEnhancement(BaseModel):
    pricing_model: str  # e.g., Value-based pricing, Outcome-linked fees, Subscription model
    enhancement_trend: Trend # Implementation, development, exploration, optimization, assessment
    notes: Optional[str] = None # e.g., Project-retainer balance, IP licensing

class GoToMarketStrategyRefinement(BaseModel):
    market_segmentation_approach: List[MarketSegmentationApproach]
    value_proposition_differentiation: List[ValuePropositionDifferentiation]
    business_development_methodology: List[BusinessDevelopmentMethodology]
    partnership_ecosystem_development: List[PartnershipEcosystemDevelopment]
    pricing_strategy_enhancement: List[PricingStrategyEnhancement] 