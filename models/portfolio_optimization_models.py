from pydantic import BaseModel, Field
from typing import List, Optional

class EvaluationDimension(BaseModel):
    dimension_name: str  # e.g., Market growth potential, Competitive position strength
    description: Optional[str] = None
    # Weighting or scoring can be added later if needed for a live matrix

class DecisionArea(BaseModel):
    area_name: str  # e.g., Service offering investment, Client segment focus
    description: Optional[str] = None
    # Specific options or choices for this area can be added

class PortfolioOptimizationDecisionMatrix(BaseModel):
    description: str = "Framework to evaluate strategic choices for portfolio optimization."
    decision_areas_to_evaluate: List[DecisionArea]
    evaluation_dimensions: List[EvaluationDimension]
    # This model could be expanded to include actual matrix data or links to it 