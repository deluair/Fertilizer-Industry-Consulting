from pydantic import BaseModel, Field
from typing import List, Optional

class TalentFocusArea(BaseModel):
    area_name: str  # e.g., Technical expertise acquisition, Industry experience integration
    description: Optional[str] = None
    # Specific strategies or goals for this area can be added

class ImplementationConsideration(BaseModel):
    consideration_name: str  # e.g., Critical skill prioritization, Geographic market talent availability
    description: Optional[str] = None
    # Specific metrics or approaches for this consideration can be added

class TalentStrategyFramework(BaseModel):
    description: str = "Comprehensive approach for talent development and acquisition."
    talent_focus_areas: List[TalentFocusArea]
    implementation_roadmap_considerations: List[ImplementationConsideration] 