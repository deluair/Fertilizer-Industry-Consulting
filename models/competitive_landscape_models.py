from pydantic import BaseModel, Field
from typing import List, Optional
from .base_model import Trend

class ConsultancyEvolution(BaseModel):
    consultancy_type: str # e.g., Traditional agricultural, Engineering, Management
    evolution_area: str   # e.g., Digital capability, Sustainability expertise, Agronomic capability
    pathway_or_positioning: Trend
    notes: Optional[str] = None

class NicheSpecialistEmergence(BaseModel):
    specialist_type: str  # e.g., Sustainability boutiques, Digital ag specialists, Biologicals consultancies
    emergence_pattern: Trend
    notes: Optional[str] = None # e.g., Carbon market advisory, Regulatory compliance

class NewEntrantThreat(BaseModel):
    entrant_type: str  # e.g., Agtech company advisory, Equipment manufacturer consulting
    threat_assessment_or_expansion: Trend
    notes: Optional[str] = None # e.g., Agronomic service provider expansion, Retail technical service, Academic research services

class CompetitiveLandscapeReshaping(BaseModel):
    traditional_agricultural_consultancy_evolution: List[ConsultancyEvolution]
    engineering_consultancy_adaptation: List[ConsultancyEvolution]
    management_consultancy_positioning: List[ConsultancyEvolution]
    niche_specialist_emergence_patterns: List[NicheSpecialistEmergence]
    new_entrant_threat_assessment: List[NewEntrantThreat] 