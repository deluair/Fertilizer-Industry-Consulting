from pydantic import BaseModel, Field
from typing import List, Optional
from .base_model import Trend

class RetailConsolidationPattern(BaseModel):
    retailer_type_or_model: str  # e.g., Independent retailer, Cooperative, Corporate retail, E-commerce
    evolution_scenario_or_impact: Trend
    notes: Optional[str] = None # e.g., Direct-to-farm model penetration

class ServicePortfolioExpansion(BaseModel):
    service_type: str  # e.g., Agronomic advisory, Precision ag service, Sustainability advisory
    sophistication_or_development: Trend
    notes: Optional[str] = None # e.g., Digital platform offering, Custom application service

class InfrastructureAdaptation(BaseModel):
    infrastructure_element: str  # e.g., Warehouse network, Specialty product handling, Blending facility
    optimization_or_evolution: Trend
    notes: Optional[str] = None # e.g., Application equipment fleet, Logistics optimization

class SalesApproachTransformation(BaseModel):
    approach_element: str  # e.g., Value-based selling, Solution selling model, Technical expertise
    capability_building_or_development: Trend
    notes: Optional[str] = None # e.g., Digital engagement, Outcome documentation

class InventoryManagementEvolution(BaseModel):
    management_aspect: str  # e.g., Just-in-time, Forecasting accuracy, Seasonal risk management
    improvement_or_optimization: Trend
    notes: Optional[str] = None # e.g., Working capital optimization, Digital inventory tracking

class AgriculturalRetailAndDistributionTransformation(BaseModel):
    retail_consolidation_patterns: List[RetailConsolidationPattern]
    service_portfolio_expansion: List[ServicePortfolioExpansion]
    infrastructure_adaptation: List[InfrastructureAdaptation]
    sales_approach_transformation: List[SalesApproachTransformation]
    inventory_management_evolution: List[InventoryManagementEvolution] 