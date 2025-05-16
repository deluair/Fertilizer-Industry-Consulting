from pydantic import BaseModel, Field
from typing import List, Optional

class SpecializedPrecisionOffering(BaseModel):
    offering_name: str  # e.g., Precision agriculture strategy development, Technology stack design
    description: str
    key_components: List[str]

class PrecisionEnablingMethodology(BaseModel):
    methodology_name: str  # e.g., Field variability assessment, ROI calculation framework
    description: str
    key_features: List[str]

class PrecisionSupportingKnowledgeAsset(BaseModel):
    asset_name: str  # e.g., Technology provider evaluation, Economic impact modeling
    description: str
    asset_type: str # e.g., Database, Tool, Report

class SpecializedPrecisionCapability(BaseModel):
    capability_name: str  # e.g., Precision agriculture expertise, Agronomy knowledge integration
    description: str
    key_skills_or_methods: List[str]

class PrecisionNutritionSystemDesign(BaseModel):
    specialized_offering_suite: List[SpecializedPrecisionOffering]
    enabling_methodologies: List[PrecisionEnablingMethodology]
    supporting_knowledge_assets: List[PrecisionSupportingKnowledgeAsset]
    specialized_capability: List[SpecializedPrecisionCapability] 