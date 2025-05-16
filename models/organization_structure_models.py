from pydantic import BaseModel, Field
from typing import List, Optional
from .base_model import Trend

class PracticeOrganizationApproach(BaseModel):
    approach_area: str  # e.g., Regional vs. global balance, Technical center of excellence
    evolution_trend: Trend # Balance, development, specialization, integration, embedding
    notes: Optional[str] = None # e.g., Industry subsegment specialization, Digital capability integration

class LeadershipTeamComposition(BaseModel):
    composition_aspect: str  # e.g., Technical-business balance, Industry experience representation
    evolution_trend: Trend # Balance, representation, integration, optimization
    notes: Optional[str] = None # e.g., Digital transformation expertise, Sustainability leadership, Geographic diversity

class CareerPathInnovation(BaseModel):
    pathway_type: str  # e.g., Technical specialist track, Industry specialization pathway
    innovation_trend: Trend # Development, progression, advancement, recognition
    notes: Optional[str] = None # e.g., Digital expert career, Sustainability professional, Business developer recognition

class GovernanceModelAdaptation(BaseModel):
    governance_area: str  # e.g., Quality assurance for agronomic advice, Risk management for outcomes
    adaptation_trend: Trend # Enhancement, incentives, governance improvement
    notes: Optional[str] = None # e.g., Knowledge management protocol, Cross-regional collaboration, Innovation investment

class CultureTransformationRequirement(BaseModel):
    cultural_value: str  # e.g., Farmer-centricity, Scientific rigor, Data-driven decision making
    transformation_trend: Trend # Cultivation, normalization, internalization, encouragement
    notes: Optional[str] = None # e.g., Sustainability value internalization, Entrepreneurial approach

class OrganizationStructureOptimization(BaseModel):
    practice_organization_approaches: List[PracticeOrganizationApproach]
    leadership_team_composition: List[LeadershipTeamComposition]
    career_path_innovation: List[CareerPathInnovation]
    governance_model_adaptation: List[GovernanceModelAdaptation]
    culture_transformation_requirements: List[CultureTransformationRequirement] 