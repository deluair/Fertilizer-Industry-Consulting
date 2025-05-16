from pydantic import BaseModel, Field
from typing import List, Optional
from .base_model import Trend

class ServiceOfferingDevelopment(BaseModel):
    service_area: str  # e.g., Sustainability transformation advisory, Carbon neutrality roadmap
    development_trend: Trend
    notes: Optional[str] = None # e.g., Digital ag integration, Precision nutrition design, Portfolio strategy

class DeliveryModelTransformation(BaseModel):
    model_aspect: str  # e.g., Data-driven analytical approach, Remote/hybrid delivery
    transformation_trend: Trend # Scaling, normalization, etc.
    notes: Optional[str] = None # e.g., Outcome-based structures, Continuous advisory, Ecosystem partnerships

class IntellectualPropertyDevelopment(BaseModel):
    ip_type: str  # e.g., Decision support tool, Sustainability assessment framework
    development_trend: Trend # Creation, sophistication, etc.
    notes: Optional[str] = None # e.g., Digital maturity methodology, Market intelligence platform, Farmer segmentation

class CapabilityBuildingPriority(BaseModel):
    capability_area: str  # e.g., Agronomy expertise, Sustainability assessment competency
    priority_trend: Trend # Integration, development, certification, etc.
    notes: Optional[str] = None # e.g., Digital ag knowledge, Process engineering, Carbon accounting

class InnovationMethodologyEvolution(BaseModel):
    methodology_aspect: str  # e.g., Pilot program design, Field trial methodology
    evolution_trend: Trend # Sophistication, optimization, etc.
    notes: Optional[str] = None # e.g., ROI demonstration, Adoption acceleration, Change management

class ConsultingServicePortfolioEvolution(BaseModel):
    service_offering_development: List[ServiceOfferingDevelopment]
    delivery_model_transformation: List[DeliveryModelTransformation]
    intellectual_property_development: List[IntellectualPropertyDevelopment]
    capability_building_priorities: List[CapabilityBuildingPriority]
    innovation_methodology_evolution: List[InnovationMethodologyEvolution] 