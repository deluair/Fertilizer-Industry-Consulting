from pydantic import BaseModel, Field
from typing import List, Optional
from .base_model import Trend

class AgriculturalDataEcosystemEvolution(BaseModel):
    element: str  # e.g., Farm management software, Soil testing tech, Remote sensing platforms
    adoption_curve_or_progress: Trend
    notes: Optional[str] = None # e.g., for IoT device penetration, data standardization

class DigitalDecisionSupportSystemDevelopment(BaseModel):
    system_type: str  # e.g., Nutrient recommendation engine, AI/ML application, Weather data integration
    sophistication_or_advancement: Trend
    notes: Optional[str] = None # e.g., for economic optimization, risk management tool development

class PrecisionApplicationTechnologyAdoption(BaseModel):
    technology_type: str  # e.g., Variable rate technology, GPS-guided equipment, Section control
    adoption_metric: Trend # e.g., penetration by farm size, adoption curves, implementation rates
    notes: Optional[str] = None # e.g., for on-the-go sensing, autonomous system deployment

class DigitalValueChainIntegration(BaseModel):
    integration_area: str  # e.g., Supplier-farmer platform connectivity, Traceability system, Carbon credit M&V
    enablement_or_evolution: Trend
    notes: Optional[str] = None # e.g., for outcome-based models, digital marketplace evolution

class DataMonetizationStrategyEvolution(BaseModel):
    strategy_type: str  # e.g., Agronomic insights products, Subscription models, Performance-based pricing
    adoption_or_maturation: Trend
    notes: Optional[str] = None # e.g., for ecosystem partnerships, data-as-a-service models

class DigitalTransformationAndDataDrivenAgriculture(BaseModel):
    agricultural_data_ecosystem_evolution: List[AgriculturalDataEcosystemEvolution]
    digital_decision_support_system_development: List[DigitalDecisionSupportSystemDevelopment]
    precision_application_technology_adoption: List[PrecisionApplicationTechnologyAdoption]
    digital_value_chain_integration: List[DigitalValueChainIntegration]
    data_monetization_strategy_evolution: List[DataMonetizationStrategyEvolution] 