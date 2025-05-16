from pydantic import BaseModel, Field
from typing import List, Optional
from .industry_divergence_scenarios_models import ConsultingImplication # Reusing

class RegionalCharacteristic(BaseModel):
    characteristic: str
    description: Optional[str] = None

class RegionalMarketTrajectory(BaseModel):
    region_name: str  # e.g., North America, Europe, Asia-Pacific, Latin America
    key_characteristics: List[RegionalCharacteristic]
    consulting_implications: List[ConsultingImplication]

class RegionalMarketDivergence(BaseModel):
    regional_trajectories: List[RegionalMarketTrajectory] 