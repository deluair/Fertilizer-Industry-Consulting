from pydantic import BaseModel, Field
from typing import List, Optional
from .base_model import Trend

class ProjectMethodologyEvolution(BaseModel):
    methodology_aspect: str  # e.g., Field trial integration, Remote sensing data utilization
    evolution_trend: Trend # Approach, utilization, leveraging, protocol, extension
    notes: Optional[str] = None # e.g., Digital tool leveraging, Outcome measurement, Implementation support

class ToolAssetLeverageEnhancement(BaseModel):
    tool_or_asset_type: str  # e.g., Agronomic decision support tool, Sustainability assessment framework
    enhancement_trend: Trend # Development, creation, sophistication, enhancement
    notes: Optional[str] = None # e.g., Digital maturity methodology, ROI calculation model, KM system

class ClientEngagementModelInnovation(BaseModel):
    engagement_model_type: str  # e.g., Continuous advisory relationship, Seasonal support program
    innovation_trend: Trend # Development, structuring, design, approach, facilitation
    notes: Optional[str] = None # e.g., Outcome-based fees, Multi-year partnerships, Ecosystem collaboration

class TeamConfigurationOptimization(BaseModel):
    configuration_aspect: str  # e.g., Agronomic-business expertise balancing, Regional knowledge integration
    optimization_trend: Trend # Balancing, integration, embedding, focus
    notes: Optional[str] = None # e.g., Digital specialist embedding, Senior guidance/junior execution, Client capability building

class QualityAssuranceEnhancement(BaseModel):
    qa_area: str  # e.g., Field recommendation review, Economic impact verification
    enhancement_trend: Trend # Process, methodology, documentation, assessment, evaluation
    notes: Optional[str] = None # e.g., Environmental outcome documentation, Implementation effectiveness, Client capability transfer

class DeliveryModelTransformation(BaseModel):
    project_methodology_evolution: List[ProjectMethodologyEvolution]
    tool_and_asset_leverage_enhancement: List[ToolAssetLeverageEnhancement]
    client_engagement_model_innovation: List[ClientEngagementModelInnovation]
    team_configuration_optimization: List[TeamConfigurationOptimization]
    quality_assurance_enhancement: List[QualityAssuranceEnhancement] 