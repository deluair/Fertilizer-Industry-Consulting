from pydantic import BaseModel, Field
from typing import List, Optional

class InvestmentArea(BaseModel):
    area_name: str  # e.g., Tool and methodology development, Field research initiatives
    description: Optional[str] = None
    # Allocation percentage or priority can be added

class EvaluationCriterion(BaseModel):
    criterion_name: str  # e.g., Market differentiation potential, Client value creation magnitude
    description: Optional[str] = None
    # Weighting or scoring mechanism can be added

class InnovationInvestmentAllocation(BaseModel):
    description: str = "Portfolio approach for allocating innovation investments."
    investment_portfolio_areas: List[InvestmentArea]
    evaluation_methodology_criteria: List[EvaluationCriterion] 