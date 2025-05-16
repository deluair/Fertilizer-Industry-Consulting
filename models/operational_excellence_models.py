from pydantic import BaseModel, Field
from typing import List, Optional

class SpecializedOperationalOffering(BaseModel):
    offering_name: str  # e.g., Production efficiency assessment, Supply chain optimization
    description: str
    key_components: List[str]

class OperationalEnablingMethodology(BaseModel):
    methodology_name: str  # e.g., Diagnostic assessment approach, Opportunity prioritization
    description: str
    key_features: List[str]

class OperationalSupportingKnowledgeAsset(BaseModel):
    asset_name: str  # e.g., Industry benchmark compilation, Process optimization toolkit
    description: str
    asset_type: str # e.g., Database, Framework, Tool

class SpecializedOperationalCapability(BaseModel):
    capability_name: str  # e.g., Process engineering expertise, Operational leadership development
    description: str
    key_skills_or_methods: List[str]

class OperationalExcellenceAndPerformanceOptimization(BaseModel):
    specialized_service_offerings: List[SpecializedOperationalOffering]
    enabling_methodologies: List[OperationalEnablingMethodology]
    supporting_knowledge_assets: List[OperationalSupportingKnowledgeAsset]
    specialized_capability: List[SpecializedOperationalCapability] 