from pydantic import Field
from typing import List, Optional
from .base_model import Trend, PercentageRange, SerializableModel

class ProductionTechnologyEvolution(SerializableModel):
    technology_name: str  # e.g., Green ammonia, Bio-based fertilizer, Nanotechnology
    metric_type: str  # e.g., Cost reduction, Scaling, Application, Adoption, Efficiency improvement
    trajectory_or_curve: Trend

class RawMaterialDiversification(SerializableModel):
    material_focus: str  # e.g., Alternative phosphate, Nitrogen fixation, Secondary nutrient, Micronutrient, Waste stream
    development_stage: Optional[str] = None  # e.g., Breakthrough, Recuperation, Advancement, Valorization
    description: Optional[str] = None
    impact_trajectory: Optional[Trend] = None

class ProductionEfficiencyTransformation(SerializableModel):
    efficiency_metric: str  # e.g., Energy consumption, Water usage, Process intensification, Automation penetration
    reduction_or_improvement_pathway: Trend

class GHGEmissionReductionPathway(SerializableModel):
    emission_type_or_technology: str  # e.g., Nitrous oxide, Carbon capture, Methane emissions, Electrification
    abatement_or_adoption_trajectory: Trend

class ProductionCapacityEvolution(SerializableModel):
    region: Optional[str] = None
    factor: str  # e.g., Expansion/contraction, Retirement rates, Stranded asset risk, Retrofit vs. new-build, Investment drivers
    pattern_or_assessment: Trend  # Can represent rates, risk levels, threshold shifts, driver evolution
    description: Optional[str] = None

class ProductionTechnologyAndProcessInnovation(SerializableModel):
    production_technology_evolution: List[ProductionTechnologyEvolution]
    raw_material_diversification: List[RawMaterialDiversification]
    production_efficiency_transformation: List[ProductionEfficiencyTransformation]
    ghg_emission_reduction_pathways: List[GHGEmissionReductionPathway]
    production_capacity_evolution: List[ProductionCapacityEvolution]