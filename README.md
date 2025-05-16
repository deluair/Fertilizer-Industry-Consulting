# Fertilizer Industry Consulting Simulation Framework

A comprehensive simulation and analysis framework for modeling the evolution of the fertilizer industry (2025-2040), with a focus on sustainability transitions, production technology innovations, and market transformations.

## 🚀 Key Features

- **Sustainability Transition Modeling**: Track adoption of sustainable practices and regulatory impacts
- **Production Technology Simulation**: Model technological innovations and their adoption curves
- **Market Analysis**: Analyze regional market divergences and competitive landscapes
- **Scenario Planning**: Test different strategic scenarios and their outcomes
- **Interactive Reporting**: Generate comprehensive HTML reports with visualizations
- **Data Visualization**: Interactive dashboards for exploring simulation results

## 📊 Latest Updates

- **Enhanced Reporting**: New HTML report generator with interactive visualizations
- **Improved Data Serialization**: Better handling of complex data structures
- **User Interface**: Streamlined command-line interface
- **Documentation**: Comprehensive API and usage documentation

## 🛠️ Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/deluair/Fertilizer-Industry-Consulting.git
   cd Fertilizer-Industry-Consulting
   ```

2. Create and activate a virtual environment:

   ```bash
   # Windows
   python -m venv venv
   venv\Scripts\activate
   
   # macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   pip install -r requirements-dev.txt  # For development
   ```

4. Install Kaleido for static image export (required for some visualizations):

   ```bash
   pip install -U kaleido
   ```

## 🏗️ Project Structure

```text
.
├── analysis/              # Data analysis and visualization tools
│   ├── visualization.py    # Core visualization functions
│   └── report_generator.py # HTML report generation
├── config/                # Configuration files
├── data/                  # Data storage
│   ├── raw/               # Raw data files
│   └── processed/         # Processed data files
├── models/                # Core simulation models
│   ├── base_model.py      # Base model definitions
│   └── ...                # Domain-specific models
├── simulations/           # Simulation scenarios
│   └── scenarios/         # YAML scenario definitions
├── tests/                 # Test suite
├── main.py                # Main entry point
├── requirements.txt       # Production dependencies
└── README.md              # This file
```

## 🚦 Getting Started

### Running a Simulation

1. List available scenarios:

   ```bash
   python main.py list-scenarios
   ```

2. Run a simulation with the demo scenario:

   ```bash
   python main.py run-simulation demo
   ```

3. Run with custom output directory:

   ```bash
   python main.py run-simulation demo --output-dir ./reports
   ```

### Generating Reports

After running a simulation, an interactive HTML report will be automatically generated in the `reports/html` directory. The report includes:

- Executive summary with key metrics
- Interactive visualizations
- Detailed analysis of simulation results
- Export options for further analysis

### Example Report

![Example Report](https://via.placeholder.com/800x600?text=Fertilizer+Industry+Simulation+Report)

## 📈 Example Scenario

```yaml
# simulations/scenarios/demo.yaml
name: demo
description: Baseline scenario with moderate growth and technology adoption
parameters:
  start_year: 2025
  end_year: 2040
  regions: ["North America", "Europe", "Asia"]
  
sustainability:
  # Configuration for sustainability models
  
production_tech:
  # Configuration for production technology models

client_needs:
  # Configuration for client needs models
```

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📧 Contact

For questions or support, please open an issue on GitHub.
