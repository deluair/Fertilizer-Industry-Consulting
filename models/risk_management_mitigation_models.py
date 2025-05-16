from pydantic import BaseModel, Field
from typing import List, Optional

class RiskCategory(BaseModel):
    category_name: str  # e.g., Market evolution uncertainty, Competitive response possibility
    description: Optional[str] = None
    potential_risks: List[str]

class MitigationStrategyElement(BaseModel):
    element_name: str  # e.g., Early warning indicator identification, Contingency plan preparation
    description: Optional[str] = None
    # Specific actions or responsibilities can be detailed here

class RiskManagementAndMitigation(BaseModel):
    comprehensive_risk_assessment_framework: List[RiskCategory]
    mitigation_strategy_development: List[MitigationStrategyElement] 