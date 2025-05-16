from pydantic import BaseModel, Field
from typing import List, Optional
from .industry_divergence_scenarios_models import ConsultingImplication # Reusing

class ClientFocusArea(BaseModel):
    area: str # e.g., Portfolio reconfiguration, Production decarbonization
    description: Optional[str] = None

class ClientTypeEvolutionScenario(BaseModel):
    client_type: str  # e.g., Major Producer, Agricultural Retailer, Large-Scale Farm, Agtech Innovator
    description: Optional[str] = None
    focus_areas: List[ClientFocusArea]
    consulting_implications: List[ConsultingImplication]

class ClientTypeEvolutionScenarios(BaseModel):
    scenarios: List[ClientTypeEvolutionScenario] 