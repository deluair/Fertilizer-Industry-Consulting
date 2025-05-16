from pydantic import Field
from typing import List, Optional
from .base_model import Trend, SerializableModel

class ProductionTechTransformation(SerializableModel):
    transformation_area: str  # e.g., Energy source shifting, Process electrification, Carbon capture retrofit
    feasibility_timeline_or_adoption: Trend
    notes: Optional[str] = None  # e.g., Efficiency enhancement, Smart manufacturing deployment

class RawMaterialSourcingEvolution(SerializableModel):
    sourcing_area: str  # e.g., Alternative phosphate, Recycled nutrient integration, Renewable hydrogen
    development_scaling_or_innovation: Trend
    notes: Optional[str] = None  # e.g., Secondary/micronutrient sourcing, Supply diversification

class LogisticsOptimization(SerializableModel):
    optimization_area: str  # e.g., Modal shift potential, Last-mile delivery, Regional storage
    potential_innovation_or_development: Trend
    notes: Optional[str] = None  # e.g., Export infrastructure, Carbon optimization of transport

class SupplyChainResilienceEnhancement(SerializableModel):
    enhancement_factor: str  # e.g., Inventory strategy optimization, Supplier diversification, Digital visibility
    implementation_or_improvement: Trend
    notes: Optional[str] = None  # e.g., Manufacturing flexibility, Regional self-sufficiency

class SupplyDemandBalanceEvolution(SerializableModel):
    balance_factor: str  # e.g., Production capacity rationalization, Geopolitical disruption risk mitigation
    reconfiguration_or_management_approach: Trend
    notes: Optional[str] = None  # e.g., Trade flow changes, Regional self-sufficiency policies, Seasonal imbalance management

class ManufacturingAndSupplyChainReconfiguration(SerializableModel):
    production_technology_transformation: List[ProductionTechTransformation]
    raw_material_sourcing_evolution: List[RawMaterialSourcingEvolution]
    logistics_optimization: List[LogisticsOptimization]
    supply_chain_resilience_enhancement: List[SupplyChainResilienceEnhancement]
    supply_demand_balance_evolution: List[SupplyDemandBalanceEvolution]