"""Utility functions for the fertilizer industry simulation."""

from pathlib import Path
from typing import Any, Dict, List, Optional, Union
import json
import yaml
import numpy as np
import pandas as pd


def ensure_directory_exists(directory: Union[str, Path]) -> Path:
    """Ensure a directory exists, creating it if necessary.
    
    Args:
        directory: Path to the directory
        
    Returns:
        Path object for the directory
    """
    path = Path(directory)
    path.mkdir(parents=True, exist_ok=True)
    return path


def load_yaml(file_path: Union[str, Path]) -> Dict[str, Any]:
    """Load data from a YAML file.
    
    Args:
        file_path: Path to the YAML file
        
    Returns:
        Dictionary containing the loaded data
    """
    with open(file_path, 'r') as f:
        return yaml.safe_load(f)


def save_yaml(data: Any, file_path: Union[str, Path]) -> None:
    """Save data to a YAML file.
    
    Args:
        data: Data to save (should be YAML-serializable)
        file_path: Path to save the YAML file to
    """
    with open(file_path, 'w') as f:
        yaml.dump(data, f, default_flow_style=False)


def load_json(file_path: Union[str, Path]) -> Dict[str, Any]:
    """Load data from a JSON file.
    
    Args:
        file_path: Path to the JSON file
        
    Returns:
        Dictionary containing the loaded data
    """
    with open(file_path, 'r') as f:
        return json.load(f)


def save_json(data: Any, file_path: Union[str, Path], indent: int = 2) -> None:
    """Save data to a JSON file.
    
    Args:
        data: Data to save (should be JSON-serializable)
        file_path: Path to save the JSON file to
        indent: Indentation level for the output file
    """
    with open(file_path, 'w') as f:
        json.dump(data, f, indent=indent)


def calculate_compound_growth_rate(
    start_value: float, 
    end_value: float, 
    periods: int
) -> float:
    """Calculate the compound annual growth rate (CAGR).
    
    Args:
        start_value: Starting value
        end_value: Ending value
        periods: Number of periods
        
    Returns:
        The compound growth rate as a decimal
    """
    if start_value == 0:
        return 0.0
    return (end_value / start_value) ** (1.0 / periods) - 1


def interpolate_values(
    start_value: float, 
    end_value: float, 
    num_points: int
) -> List[float]:
    """Generate a list of linearly interpolated values between start and end.
    
    Args:
        start_value: Starting value
        end_value: Ending value
        num_points: Number of points to generate
        
    Returns:
        List of interpolated values
    """
    if num_points <= 0:
        return []
    if num_points == 1:
        return [start_value]
    return [start_value + (end_value - start_value) * i / (num_points - 1) 
            for i in range(num_points)]


def format_percentage(value: float, decimals: int = 1) -> str:
    """Format a decimal as a percentage string.
    
    Args:
        value: Value to format (e.g., 0.123 for 12.3%)
        decimals: Number of decimal places to show
        
    Returns:
        Formatted percentage string
    """
    return f"{value * 100:.{decimals}f}%"


def safe_divide(numerator: float, denominator: float, default: float = 0.0) -> float:
    """Safely divide two numbers, returning a default value if denominator is zero.
    
    Args:
        numerator: The numerator
        denominator: The denominator
        default: Value to return if denominator is zero
        
    Returns:
        Result of division or default value
    """
    return numerator / denominator if denominator != 0 else default


def generate_timeline(start_year: int, end_year: int, interval: int = 1) -> List[int]:
    """Generate a list of years from start_year to end_year (inclusive).
    
    Args:
        start_year: Starting year
        end_year: Ending year (inclusive)
        interval: Interval between years
        
    Returns:
        List of years
    """
    return list(range(start_year, end_year + 1, interval))


def calculate_moving_average(values: List[float], window: int = 3) -> List[float]:
    """Calculate a simple moving average of a list of values.
    
    Args:
        values: List of numerical values
        window: Size of the moving window
        
    Returns:
        List of moving average values
    """
    if not values or window <= 0:
        return []
    
    window = min(window, len(values))
    return [
        sum(values[max(0, i - window + 1):i + 1]) / min(window, i + 1)
        for i in range(len(values))
    ]


def normalize_values(
    values: List[float], 
    min_val: Optional[float] = None, 
    max_val: Optional[float] = None
) -> List[float]:
    """Normalize values to the range [0, 1].
    
    Args:
        values: List of values to normalize
        min_val: Minimum value for normalization (defaults to min of values)
        max_val: Maximum value for normalization (defaults to max of values)
        
    Returns:
        List of normalized values
    """
    if not values:
        return []
    
    min_val = min(values) if min_val is None else min_val
    max_val = max(values) if max_val is None else max_val
    
    if min_val == max_val:
        return [0.5] * len(values)  # All values are the same
    
    return [(x - min_val) / (max_val - min_val) for x in values]
