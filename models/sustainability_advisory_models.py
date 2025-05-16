from pydantic import BaseModel, Field
from typing import List, Optional
from .base_model import Trend # Assuming Trend might be useful for roadmap/timeline aspects

class SpecializedOffering(BaseModel):
    offering_name: str  # e.g., Carbon footprint assessment, Green ammonia roadmap
    description: str
    key_components: List[str]

class DifferentiatedMethodology(BaseModel):
    methodology_name: str  # e.g., Life cycle assessment adaptation, ROI calculation
    description: str
    key_features: List[str]

class ThoughtLeadershipPlatformElement(BaseModel):
    element_name: str  # e.g., Research initiative, Case study documentation
    description: str
    focus_areas: List[str]

class SpecializedCapability(BaseModel):
    capability_name: str  # e.g., Carbon accounting expertise, Process engineering knowledge
    description: str
    key_aspects: List[str]

class SustainabilityTransformationAdvisory(BaseModel):
    specialized_offering_suite: List[SpecializedOffering]
    differentiated_methodologies: List[DifferentiatedMethodology]
    thought_leadership_platform: List[ThoughtLeadershipPlatformElement]
    specialized_capability_center: List[SpecializedCapability] 