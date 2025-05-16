import json
import typer
from pathlib import Path
from typing import Optional, List, Dict, Any
import pandas as pd
import plotly.express as px
from datetime import datetime
import webbrowser

# Core models
from models.base_model import Trend, PercentageRange, SimulationPeriod
from models.sustainability_transition_models import SustainabilityTransition
from models.production_technology_models import ProductionTechnologyAndProcessInnovation
from models.client_need_transformation_models import ClientNeedTransformation
from models.manufacturing_supply_chain_models import ManufacturingAndSupplyChainReconfiguration

# Simulation components
from simulation.runner import SimulationRunner
from simulation.scenarios import load_scenario
from analysis.visualization import plot_simulation_results
from analysis.report_generator import generate_report
from config import settings

app = typer.Typer(help="Fertilizer Industry Simulation Framework")


def setup_directories() -> None:
    """Ensure all required directories exist."""
    dirs = [
        "data/raw",
        "data/processed",
        "data/simulations",
        "reports/figures",
        "reports/results"
    ]
    for dir_path in dirs:
        Path(dir_path).mkdir(parents=True, exist_ok=True)


@app.command()
def run_simulation(
    scenario: str = typer.Argument("baseline", help="Name of scenario to run"),
    output_dir: str = typer.Option("reports/results", help="Directory to save results"),
    visualize: bool = typer.Option(True, help="Generate visualizations"),
    save_results: bool = typer.Option(True, help="Save simulation results")
) -> None:
    """Run a simulation with the specified scenario."""
    print(f"🚀 Starting simulation for scenario: {scenario}")
    
    try:
        # Load scenario configuration
        scenario_config = load_scenario(scenario)
        
        # Initialize and run simulation
        runner = SimulationRunner(scenario_config)
        print("🚀 Initializing simulation models...")
        runner.initialize_models()
        
        print("🔍 Running simulation...")
        results = runner.run()
        print("✅ Simulation completed successfully!")
        
        # Convert results to serializable format
        def convert_to_serializable(obj):
            if hasattr(obj, 'dict'):
                return obj.dict()
            elif isinstance(obj, (list, tuple)):
                return [convert_to_serializable(item) for item in obj]
            elif isinstance(obj, dict):
                return {key: convert_to_serializable(value) for key, value in obj.items()}
            elif hasattr(obj, '__dict__'):
                return {key: convert_to_serializable(value) for key, value in obj.__dict__.items()}
            return obj
        
        serializable_results = convert_to_serializable(results)
        
        # Save results if requested
        if save_results:
            output_path = Path(output_dir) / f"{scenario}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
            output_path.parent.mkdir(parents=True, exist_ok=True)
            with open(output_path, 'w', encoding='utf-8') as f:
                json.dump(serializable_results, f, indent=2, ensure_ascii=False)
            print(f"💾 Results saved to {output_path}")
        
        # Generate visualizations if requested
        if visualize:
            try:
                print("📊 Generating comprehensive report...")
                report_dir = Path("reports") / "html"
                report_path = generate_report(serializable_results, report_dir)
                print(f"📄 Report generated at: {report_path}")
                
                # Open the report in the default web browser
                try:
                    webbrowser.open(f"file://{report_path.absolute()}")
                except Exception as e:
                    print(f"⚠️ Could not open report in browser: {str(e)}")
                    print(f"   You can open it manually at: {report_path.absolute()}")
                    
            except Exception as e:
                print(f"⚠️ Failed to generate report: {str(e)}")
                import traceback
                traceback.print_exc()
        
        return serializable_results
        
    except Exception as e:
        print(f"❌ Error running simulation: {str(e)}")
        raise typer.Exit(1)


@app.command()
def list_scenarios() -> None:
    """List all available simulation scenarios."""
    scenarios_dir = Path("simulations/scenarios")
    if not scenarios_dir.exists():
        print("No scenarios found.")
        return
        
    print("\nAvailable scenarios:")
    for scenario_file in scenarios_dir.glob("*.yaml"):
        print(f"- {scenario_file.stem}")


@app.command()
def show_config() -> None:
    """Show the current configuration."""
    print("\nCurrent configuration:")
    print(json.dumps(settings.model_dump(), indent=2))


@app.command()
def demo() -> None:
    """Run a demo simulation with example data."""
    print("Running demo simulation...")
    # Run with a simple demo scenario
    run_simulation("demo", visualize=True, save_results=True)


if __name__ == "__main__":
    # Setup required directories
    setup_directories()
    
    # Run the CLI
    app()