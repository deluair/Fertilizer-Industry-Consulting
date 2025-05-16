"""Simulation runner for the fertilizer industry model."""

from typing import Dict, Any, List, Optional
import numpy as np
import pandas as pd
from datetime import datetime
from pathlib import Path
import yaml

from models.base_model import SimulationPeriod
from models.sustainability_transition_models import SustainabilityTransition
from models.production_technology_models import ProductionTechnologyAndProcessInnovation
from models.client_need_transformation_models import ClientNeedTransformation


class SimulationRunner:
    """Orchestrates the execution of fertilizer industry simulations."""
    
    def __init__(self, config: Dict[str, Any]):
        """Initialize the simulation with a configuration dictionary.
        
        Args:
            config: Dictionary containing simulation configuration
        """
        self.config = config
        self.simulation_period = SimulationPeriod(
            start_year=config.get("start_year", 2025),
            end_year=config.get("end_year", 2040)
        )
        self.results = {}
        
    def initialize_models(self) -> None:
        """Initialize all the simulation models based on the configuration."""
        # Initialize sustainability transition model
        self.sustainability = SustainabilityTransition(
            **self.config.get("sustainability", {})
        )
        
        # Initialize production technology model
        self.production_tech = ProductionTechnologyAndProcessInnovation(
            **self.config.get("production_technology", {})
        )
        
        # Initialize client needs model
        self.client_needs = ClientNeedTransformation(
            **self.config.get("client_needs", {})
        )
    
    def run(self) -> Dict[str, Any]:
        """Run the simulation and return results.
        
        Returns:
            Dictionary containing simulation results
        """
        print("🚀 Initializing simulation models...")
        self.initialize_models()
        
        print("🔍 Running simulation...")
        
        # Run each component of the simulation
        self.results["sustainability"] = self._run_sustainability_simulation()
        self.results["production_tech"] = self._run_production_tech_simulation()
        self.results["client_needs"] = self._run_client_needs_simulation()
        
        # Combine and process results
        self._process_results()
        
        print("✅ Simulation completed successfully!")
        return self.results
    
    def _run_sustainability_simulation(self) -> Dict[str, Any]:
        """Run the sustainability transition simulation."""
        # This is a simplified example - in a real implementation, this would 
        # run complex simulations for sustainability transitions
        return {
            "fertilizer_adoption": self.sustainability.fertilizer_adoption_curves,
            "technology_penetration": self.sustainability.controlled_release_tech_penetration,
            "metrics": {
                "carbon_footprint_reduction": np.random.uniform(0.1, 0.5),
                "sustainable_share": np.random.uniform(0.2, 0.8)
            }
        }
    
    def _run_production_tech_simulation(self) -> Dict[str, Any]:
        """Run the production technology simulation."""
        return {
            "technology_evolution": [
                tech.model_dump() for tech in self.production_tech.production_technology_evolution
            ],
            "metrics": {
                "efficiency_gain": np.random.uniform(0.05, 0.3),
                "cost_reduction": np.random.uniform(0.1, 0.4)
            }
        }
    
    def _run_client_needs_simulation(self) -> Dict[str, Any]:
        """Run the client needs transformation simulation."""
        return {
            "priority_evolution": [
                priority.model_dump() for priority in self.client_needs.client_priority_evolution
            ],
            "metrics": {
                "sustainability_demand": np.random.uniform(0.6, 0.9),
                "digital_tool_adoption": np.random.uniform(0.3, 0.8)
            }
        }
    
    def _process_results(self) -> None:
        """Process and aggregate simulation results."""
        # Add timestamp and metadata
        self.results["metadata"] = {
            "simulation_timestamp": datetime.now().isoformat(),
            "simulation_period": {
                "start_year": self.simulation_period.start_year,
                "end_year": self.simulation_period.end_year
            },
            "version": "1.0.0"
        }
        
        # Calculate aggregate metrics
        self.results["summary_metrics"] = {
            "overall_sustainability_score": (
                self.results["sustainability"]["metrics"]["sustainable_share"] * 100
            ),
            "production_efficiency_gain": (
                self.results["production_tech"]["metrics"]["efficiency_gain"] * 100
            ),
            "client_sustainability_demand": (
                self.results["client_needs"]["metrics"]["sustainability_demand"] * 100
            )
        }


def load_scenario(scenario_name: str) -> Dict[str, Any]:
    """Load a simulation scenario from a YAML file.
    
    Args:
        scenario_name: Name of the scenario to load (without .yaml extension)
        
    Returns:
        Dictionary containing the scenario configuration
    """
    scenario_path = Path(f"simulations/scenarios/{scenario_name}.yaml")
    
    if not scenario_path.exists():
        raise FileNotFoundError(f"Scenario file not found: {scenario_path}")
    
    with open(scenario_path, 'r') as f:
        return yaml.safe_load(f)
