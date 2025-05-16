"""Core simulation package for the fertilizer industry model."""

from pathlib import Path
from typing import Dict, Any, List, Optional

# Ensure the simulation directory exists
Path(__file__).parent.mkdir(exist_ok=True)

__all__ = ["SimulationRunner", "load_scenario"]

from .runner import SimulationRunner, load_scenario
