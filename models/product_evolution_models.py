from pydantic import BaseModel, Field
from typing import List, Optional
from .base_model import Trend

class PortfolioTransformation(BaseModel):
    product_type_or_technology: str  # e.g., Enhanced efficiency fertilizer, Controlled/slow-release, Bio-stimulant integration
    adoption_curve_or_evolution: Trend
    segment: Optional[str] = None  # e.g., Crop segment for specialty blends

class PrecisionNutritionSystemEvolution(BaseModel):
    system_component: str  # e.g., Soil testing tech, Remote sensing, Variable rate application
    advancement_or_penetration: Trend
    sophistication_level: Optional[str] = None # For decision support systems

class BiologicalProductAdvancement(BaseModel):
    advancement_area: str  # e.g., Microbial inoculant efficacy, Formulation stability, Shelf-life extension
    improvement_or_evolution: Trend
    integration_approach: Optional[str] = None # For biologicals-conventional integration

class FertilizationSystemTransformation(BaseModel):
    system_type: str  # e.g., Fertigation, Foliar application, Root zone sensing, Drone-based application
    adoption_curve_or_scaling: Trend
    integration_type: Optional[str] = None # e.g., Robotics integration

class CropSpecificSolutionDevelopment(BaseModel):
    crop_category: str  # e.g., Row crop, Specialty crop, Greenhouse, Perennial, Urban/vertical farming
    nutrition_system_evolution_or_innovation: Trend

class ProductEvolutionAndAgronomicInnovation(BaseModel):
    product_portfolio_transformation: List[PortfolioTransformation]
    precision_nutrition_system_evolution: List[PrecisionNutritionSystemEvolution]
    biological_product_advancement: List[BiologicalProductAdvancement]
    fertilization_system_transformation: List[FertilizationSystemTransformation]
    crop_specific_solution_development: List[CropSpecificSolutionDevelopment] 