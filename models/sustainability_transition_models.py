from pydantic import Field
from typing import List, Optional
from .base_model import PercentageRange, Trend, SerializableModel

class FertilizerAdoption(SerializableModel):
    fertilizer_type: str  # e.g., Organic, Biological
    market_growth: PercentageRange
    target_year: int

class TechnologyPenetration(SerializableModel):
    technology_name: str  # e.g., Controlled-release, Precision application
    category: str  # e.g., Crop category, Farm size
    adoption_rate: Optional[Trend] = None
    penetration_forecast: Optional[PercentageRange] = None  # If specific target like organic market growth

class CarbonFootprintReduction(SerializableModel):
    product_type: str = "Conventional Products"
    reduction_trajectory: Trend

class CircularEconomyModel(SerializableModel):
    model_type: str  # e.g., Nutrient recovery and recycling
    adoption_trajectory: Trend

class RegulatoryEvolution(SerializableModel):
    region: str
    regulation_type: str  # e.g., Nitrogen regulation, Phosphorus runoff restriction
    intensification_timeline: Optional[Trend] = None
    impact_description: Optional[str] = None

class IndustryResponseStrategy(SerializableModel):
    strategy_type: str  # e.g., Major producer sustainability transformation, R&D investment reallocation
    pathway_or_pattern: Trend

class SustainableTechnologyInvestment(SerializableModel):
    investment_source: str  # e.g., Venture capital, Corporate venture
    focus_area: Optional[str] = None
    investment_volume_trajectory: Optional[Trend] = None
    activity_pattern: Optional[Trend] = None

class CarbonNeutralityPathway(SerializableModel):
    pathway_component: str  # e.g., Green ammonia production, Renewable energy integration
    scaling_trajectory: Optional[Trend] = None
    implementation_timeline: Optional[Trend] = None
    description: Optional[str] = None

class SustainabilityTransition(SerializableModel):
    fertilizer_adoption_curves: List[FertilizerAdoption]
    controlled_release_tech_penetration: List[TechnologyPenetration]
    precision_application_tech_adoption: List[TechnologyPenetration]
    carbon_footprint_reduction_trajectories: List[CarbonFootprintReduction]
    circular_economy_model_adoption: List[CircularEconomyModel]
    regional_regulatory_evolution: List[RegulatoryEvolution]
    industry_response_strategies: List[IndustryResponseStrategy]
    sustainable_tech_investment_flows: List[SustainableTechnologyInvestment]
    carbon_neutrality_pathways: List[CarbonNeutralityPathway]