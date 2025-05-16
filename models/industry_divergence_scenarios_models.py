from pydantic import BaseModel, Field
from typing import List, Optional, Dict
from .base_model import Trend, PercentageRange

class ScenarioAssumption(BaseModel):
    assumption: str
    metric: Optional[str] = None # e.g., "Green ammonia adoption", "Market share"
    value: Optional[str] = None # e.g., "50%+ by 2035", "40% by 2030"
    description: Optional[str] = None

class ConsultingImplication(BaseModel):
    implication: str
    details: Optional[str] = None

class IndustryDivergenceScenario(BaseModel):
    scenario_name: str # e.g., Accelerated Sustainability Transformation, Technology-Driven Evolution
    description: Optional[str] = None
    key_assumptions: List[ScenarioAssumption]
    consulting_implications: List[ConsultingImplication]

class IndustryDivergenceScenarios(BaseModel):
    scenarios: List[IndustryDivergenceScenario] 