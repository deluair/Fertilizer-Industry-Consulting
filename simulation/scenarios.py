"""Module for loading and managing simulation scenarios."""

import yaml
from pathlib import Path
from typing import Dict, Any, Optional


def load_scenario(scenario_name: str) -> Dict[str, Any]:
    """Load a scenario from the scenarios directory.
    
    Args:
        scenario_name: Name of the scenario to load (without .yaml extension)
        
    Returns:
        Dictionary containing the scenario data
        
    Raises:
        FileNotFoundError: If the scenario file does not exist
        yaml.YAMLError: If there is an error parsing the YAML file
    """
    # Construct the path to the scenario file
    scenario_dir = Path(__file__).parent.parent / "simulations" / "scenarios"
    scenario_file = scenario_dir / f"{scenario_name}.yaml"
    
    if not scenario_file.exists():
        raise FileNotFoundError(f"Scenario file not found: {scenario_file}")
    
    # Load and return the scenario
    with open(scenario_file, 'r') as f:
        return yaml.safe_load(f)


def list_scenarios() -> list[str]:
    """List all available scenarios in the scenarios directory.
    
    Returns:
        List of scenario names (without .yaml extension)
    """
    scenario_dir = Path(__file__).parent.parent / "simulations" / "scenarios"
    
    if not scenario_dir.exists():
        return []
    
    return [f.stem for f in scenario_dir.glob("*.yaml") if f.is_file()]
