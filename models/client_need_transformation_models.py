from pydantic import Field
from typing import List, Optional
from .base_model import Trend, SerializableModel

class ClientPriorityEvolution(SerializableModel):
    priority_area: str  # e.g., Sustainability transformation, Digital integration, Regulatory compliance
    evolution_trend: Trend  # How this priority evolves over time
    notes: Optional[str] = None  # e.g., Production efficiency, Portfolio recalibration

class DecisionMakerProfileShift(SerializableModel):
    profile_aspect: str  # e.g., Sustainability leadership influence, Digital strategy leadership
    shift_trend: Trend  # How the influence or emergence of this profile shifts
    notes: Optional[str] = None  # e.g., Technical vs. commercial weight, Procurement sophistication, Board-level governance

class ProblemFramingEvolution(SerializableModel):
    framing_aspect: str  # e.g., Strategic vs. tactical, Long-term vs. short-term orientation
    evolution_trend: Trend  # How the problem framing evolves
    notes: Optional[str] = None  # e.g., Integrated vs. siloed, Performance metrics redefinition, Value creation model

class BudgetAllocationShift(SerializableModel):
    budget_area: str  # e.g., Sustainability initiatives, Digital transformation funding, OpEx pressure
    shift_trend: Trend  # How budget allocation in this area shifts
    notes: Optional[str] = None  # e.g., CapEx to low-carbon assets, R&D prioritization

class SectorBoundaryBlurring(SerializableModel):
    converging_sector: str  # e.g., Agtech, Carbon market, Circular economy industry
    blurring_trend: Trend  # How the boundaries with this sector are blurring
    notes: Optional[str] = None  # e.g., Renewable energy overlap, Food industry upstream integration

class ClientNeedTransformation(SerializableModel):
    client_priority_evolution: List[ClientPriorityEvolution]
    decision_maker_profile_shifts: List[DecisionMakerProfileShift]
    problem_framing_evolution: List[ProblemFramingEvolution]
    budget_allocation_shifts: List[BudgetAllocationShift]
    sector_boundary_blurring: List[SectorBoundaryBlurring]