from pydantic import BaseModel, Field
from typing import List, Optional
from .base_model import Trend

class SustainablePracticeAdoption(BaseModel):
    practice_type: str  # e.g., Precision nutrition, 4R stewardship, Carbon farming
    implementation_rate_or_penetration: Trend # Could be by segment, or overall timeline
    notes: Optional[str] = None # e.g., Organic conversion trajectories

class PurchasingBehaviorEvolution(BaseModel):
    behavior_aspect: str  # e.g., Decision factor priority, Information source use, Brand loyalty
    shifting_or_variation: Trend
    notes: Optional[str] = None # e.g., Price sensitivity by segment, Service valuation

class FarmOperationTransformation(BaseModel):
    transformation_area: str  # e.g., Scale evolution, Technology adoption sequencing, Knowledge sophistication
    evolution_or_advancement: Trend # Can be by region/production type for scale
    notes: Optional[str] = None # e.g., Data utilization, Management professionalization

class CropMixEvolutionImpact(BaseModel):
    crop_factor: str  # e.g., High-value crop expansion, Climate-adapted varieties, Novel crops
    trajectory_or_influence: Trend
    notes: Optional[str] = None # e.g., Protein source diversification, Changing nutritional demands

class FinancingModelAdaptation(BaseModel):
    financing_model: str  # e.g., Input financing, Sustainability-linked financing, Outcome-based payment
    evolution_or_adoption: Trend
    notes: Optional[str] = None # e.g., Risk-sharing arrangements, Carbon credit integration

class FarmerAdoptionAndDemandEvolution(BaseModel):
    sustainable_practice_adoption: List[SustainablePracticeAdoption]
    purchasing_behavior_evolution: List[PurchasingBehaviorEvolution]
    farm_operation_transformation: List[FarmOperationTransformation]
    crop_mix_evolution_impact: List[CropMixEvolutionImpact]
    financing_model_adaptation: List[FinancingModelAdaptation] 