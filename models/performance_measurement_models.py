from pydantic import BaseModel, Field
from typing import List, Optional, Dict

class KpiCategory(BaseModel):
    category_name: str  # e.g., Financial performance, Market position, Client satisfaction
    description: Optional[str] = None
    key_metrics: List[str] # Specific KPIs like 'Revenue Growth', 'Market Share', 'NPS'

class ProgressTrackingMethodology(BaseModel):
    method_name: str  # e.g., Leading indicator identification, Performance dashboard development
    description: Optional[str] = None
    key_elements: List[str]

class PerformanceMeasurementFramework(BaseModel):
    multi_dimensional_kpi_system: List[KpiCategory]
    progress_tracking_methodology: List[ProgressTrackingMethodology]
    # Could include success celebration protocols or specific review cadences 