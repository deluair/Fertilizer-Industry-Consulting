from pydantic import BaseModel, Field
from typing import List, Optional
from .base_model import Trend

class ProprietaryKnowledgeCreation(BaseModel):
    knowledge_area: str  # e.g., Agronomic database, Performance benchmark, Best practice documentation
    creation_trend: Trend # Development, compilation, documentation, standardization, creation
    notes: Optional[str] = None # e.g., Implementation methodology, Tool and framework creation

class ThoughtLeadershipPositioning(BaseModel):
    positioning_activity: str  # e.g., Research agenda development, Publication strategy
    evolution_trend: Trend # Development, formulation, prioritization, design, participation
    notes: Optional[str] = None # e.g., Speaking engagements, Digital content program, Industry forum participation

class KnowledgeManagementEnhancement(BaseModel):
    km_aspect: str  # e.g., Cross-project learning, Regional insight sharing, Case study documentation
    enhancement_trend: Trend # Facilitation, mechanism, process, methodology, capturing
    notes: Optional[str] = None # e.g., Solution replication, Expert knowledge capturing

class ResearchPartnershipApproach(BaseModel):
    partnership_type: str  # e.g., Academic collaboration, Industry consortium participation
    approach_evolution: Trend # Framework, participation, network development, program structure, arrangement design
    notes: Optional[str] = None # e.g., Field research network, On-farm trial program, Data sharing

class IPProtectionStrategy(BaseModel):
    protection_area: str  # e.g., Tool and methodology protection, Dataset ownership
    strategy_evolution: Trend # Protection, clarification, safeguards, limitation, preservation
    notes: Optional[str] = None # e.g., Client confidentiality, Knowledge transfer limitation, Competitive differentiation

class KnowledgeAndIntellectualPropertyDevelopment(BaseModel):
    proprietary_knowledge_creation: List[ProprietaryKnowledgeCreation]
    thought_leadership_positioning: List[ThoughtLeadershipPositioning]
    knowledge_management_enhancement: List[KnowledgeManagementEnhancement]
    research_partnership_approach: List[ResearchPartnershipApproach]
    ip_protection_strategy: List[IPProtectionStrategy] 