from pydantic import BaseModel, Field
from typing import List, Optional

class TransformationHorizon(BaseModel):
    horizon_name: str  # e.g., Horizon 1: Core enhancement
    timeframe: str  # e.g., 0-12 months
    focus_areas: List[str]
    description: Optional[str] = None

class ImplementationPhase(BaseModel):
    phase_name: str  # e.g., Concept development, Pilot implementation
    description: Optional[str] = None
    key_activities: List[str]

class ResourceAllocationFrameworkElement(BaseModel):
    element_name: str  # e.g., Investment capacity assessment, Strategic initiative prioritization
    description: Optional[str] = None
    # Specific methods or metrics can be detailed here

class StrategicInitiativePrioritization(BaseModel):
    multi_horizon_transformation_approach: List[TransformationHorizon]
    stage_gated_implementation_methodology: List[ImplementationPhase]
    resource_allocation_optimization_framework: List[ResourceAllocationFrameworkElement] 