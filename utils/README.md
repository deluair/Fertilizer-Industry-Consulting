# Utils Module

This module provides utility functions used throughout the fertilizer industry simulation project.

## Functions

### File I/O
- `ensure_directory_exists(directory)`: Ensures a directory exists, creating it if necessary
- `load_yaml(file_path)`: Loads data from a YAML file
- `save_yaml(data, file_path)`: Saves data to a YAML file
- `load_json(file_path)`: Loads data from a JSON file
- `save_json(data, file_path, indent=2)`: Saves data to a JSON file

### Mathematical Operations
- `calculate_compound_growth_rate(start_value, end_value, periods)`: Calculates the compound annual growth rate
- `interpolate_values(start_value, end_value, num_points)`: Generates linearly interpolated values
- `safe_divide(numerator, denominator, default=0.0)`: Safely divides two numbers with a default for zero division
- `calculate_moving_average(values, window=3)`: Calculates a simple moving average
- `normalize_values(values, min_val=None, max_val=None)`: Normalizes values to [0, 1] range

### Formatting
- `format_percentage(value, decimals=1)`: Formats a decimal as a percentage string
- `generate_timeline(start_year, end_year, interval=1)`: Generates a list of years

## Usage

```python
from utils import load_yaml, save_json, calculate_compound_growth_rate

# Load a YAML configuration file
config = load_yaml("config/simulation.yaml")

# Calculate compound growth rate
growth_rate = calculate_compound_growth_rate(100, 200, 5)  # 14.87% growth

# Save results to JSON
results = {"growth_rate": growth_rate}
save_json(results, "output/results.json")
```

## Dependencies
- Python 3.8+
- PyYAML
- NumPy (for some functions)
