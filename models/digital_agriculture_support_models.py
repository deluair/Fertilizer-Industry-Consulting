from pydantic import BaseModel, Field
from typing import List, Optional

class SpecializedDigitalOffering(BaseModel):
    offering_name: str  # e.g., Digital maturity assessment, Technology selection support
    description: str
    key_components: List[str]

class EnablingMethodology(BaseModel):
    methodology_name: str  # e.g., Value case development, Implementation roadmap design
    description: str
    key_features: List[str]

class SupportingKnowledgeAsset(BaseModel):
    asset_name: str  # e.g., Technology landscape mapping, Best practice documentation
    description: str
    content_type: str # e.g., Report, Database, Framework

class EnablingCapability(BaseModel):
    capability_name: str  # e.g., Digital technology expertise, Data science competency
    description: str
    key_skills: List[str]

class DigitalAgricultureIntegrationSupport(BaseModel):
    specialized_service_offerings: List[SpecializedDigitalOffering]
    enabling_methodologies: List[EnablingMethodology]
    supporting_knowledge_assets: List[SupportingKnowledgeAsset]
    enabling_capabilities: List[EnablingCapability] 