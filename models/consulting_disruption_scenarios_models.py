from pydantic import BaseModel, Field
from typing import List, Optional

class DisruptionFactor(BaseModel):
    factor: str # e.g., Data platform-based advisory, Automated recommendation engine
    description: Optional[str] = None

class ResponseImplication(BaseModel):
    implication: str # e.g., Digital capability integration, Value-added focus
    details: Optional[str] = None

class ConsultingIndustryDisruptionScenario(BaseModel):
    scenario_name: str # e.g., Digital-Driven Disruption, Industry Convergence Disruption
    description: Optional[str] = None
    key_disruption_factors: List[DisruptionFactor]
    response_implications: List[ResponseImplication]

class ConsultingIndustryDisruptionScenarios(BaseModel):
    scenarios: List[ConsultingIndustryDisruptionScenario] 