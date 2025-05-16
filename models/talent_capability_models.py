from pydantic import BaseModel, Field
from typing import List, Optional
from .base_model import Trend

class ConsultantProfileEvolution(BaseModel):
    attribute: str  # e.g., Agronomic knowledge, Sustainability expertise, Digital fluency
    importance_or_value_trend: Trend
    notes: Optional[str] = None # e.g., Process engineering background, Business transformation experience

class RecruitingSourceDiversification(BaseModel):
    source_type: str  # e.g., Industry technical experts, Digital ag specialists, Sustainability professionals
    diversification_trend: Trend # Attraction, recruitment, integration, acquisition
    notes: Optional[str] = None # e.g., Academic partnerships, Adjacent industry talent

class DevelopmentTrainingTransformation(BaseModel):
    training_area: str  # e.g., Agronomic certification, Sustainability assessment training
    transformation_trend: Trend # Implementation, development, building
    notes: Optional[str] = None # e.g., Digital ag knowledge, Process improvement methodology, Change management capability

class WorkingModelAdaptation(BaseModel):
    model_aspect: str  # e.g., Field/farm presence, Remote analytical work, Global-local expertise balancing
    adaptation_trend: Trend # Requirement, optimization, balancing
    notes: Optional[str] = None # e.g., Cross-functional teams, Expert network integration

class CompensationModelEvolution(BaseModel):
    model_element: str  # e.g., Outcome-based incentives, Technical premium adjustment
    evolution_trend: Trend # Structure, adjustment, valuation, balancing
    notes: Optional[str] = None # e.g., Industry experience valuation, Specialized knowledge compensation, Biz dev reward

class TalentAndCapabilityRequirements(BaseModel):
    consultant_profile_evolution: List[ConsultantProfileEvolution]
    recruiting_source_diversification: List[RecruitingSourceDiversification]
    development_and_training_transformation: List[DevelopmentTrainingTransformation]
    working_model_adaptation: List[WorkingModelAdaptation]
    compensation_model_evolution: List[CompensationModelEvolution] 