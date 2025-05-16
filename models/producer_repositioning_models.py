from pydantic import BaseModel, Field
from typing import List, Optional
from .base_model import Trend

class IndustryConsolidationPattern(BaseModel):
    scenario_type: str  # e.g., M&A by segment, Vertical integration, Geographic expansion
    evolution_or_trajectory: Trend
    notes: Optional[str] = None # e.g., Portfolio diversification, Divestment patterns

class SustainabilityLeadershipStrategy(BaseModel):
    strategy_element: str  # e.g., Carbon-neutral production investment, Circularity initiative
    adoption_rate_or_implementation: Trend
    notes: Optional[str] = None # e.g., Science-based targets, Green product line development

class BusinessModelInnovation(BaseModel):
    model_type: str  # e.g., Outcome-based service, Nutrient-as-a-service, Carbon credit integration
    penetration_or_emergence: Trend
    notes: Optional[str] = None # e.g., Digital service monetization, Ag retail partnerships

class RDPrioritization(BaseModel):
    focus_area: str  # e.g., Biologicals, Efficiency enhancement, Digital tech
    investment_shift_or_emphasis: Trend
    notes: Optional[str] = None # e.g., Application innovation, Formulation tech

class GeographicFootprintOptimization(BaseModel):
    optimization_factor: str  # e.g., Production relocation, Market proximity vs. energy cost
    assessment_or_recalibration: Trend # Could be impact assessment, strategy recalibration, scaling trend
    notes: Optional[str] = None # e.g., Regional regulatory impact, Export strategy, Local production scaling

class ProducerStrategicRepositioning(BaseModel):
    industry_consolidation_patterns: List[IndustryConsolidationPattern]
    sustainability_leadership_strategies: List[SustainabilityLeadershipStrategy]
    business_model_innovation: List[BusinessModelInnovation]
    rd_reprioritization: List[RDPrioritization]
    geographic_footprint_optimization: List[GeographicFootprintOptimization] 