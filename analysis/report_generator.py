"""Generate comprehensive HTML reports for simulation results."""

from pathlib import Path
from typing import Dict, Any, List, Tuple
import json
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from datetime import datetime
import webbrowser

class ReportGenerator:
    """Generate comprehensive HTML reports for simulation results."""
    
    def __init__(self, results: Dict[str, Any], output_dir: Path) -> None:
        """Initialize with simulation results and output directory."""
        self.results = results
        self.output_dir = output_dir
        self.output_dir.mkdir(parents=True, exist_ok=True)
        self.figures: List[Tuple[str, go.Figure]] = []
    
    def generate_report(self) -> Path:
        """Generate and save the HTML report.
        
        Returns:
            Path to the generated report file
        """
        # Create all visualizations
        self._create_summary_visualizations()
        self._create_sustainability_visualizations()
        self._create_production_tech_visualizations()
        self._create_client_needs_visualizations()
        
        # Generate HTML content
        html_content = self._generate_html()
        
        # Save the report
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        report_path = self.output_dir / f"simulation_report_{timestamp}.html"
        
        with open(report_path, 'w', encoding='utf-8') as file:
            file.write(html_content)
            
        return report_path
    
    def _create_summary_visualizations(self) -> None:
        """Create summary visualizations."""
        if "summary_metrics" not in self.results:
            return
            
        metrics = self.results["summary_metrics"]
        
        # Create a bar chart of key metrics
        figure = px.bar(
            x=list(metrics.keys()),
            y=list(metrics.values()),
            title="Key Performance Indicators",
            labels={"x": "Metric", "y": "Value"}
        )
        figure.update_layout(showlegend=False)
        self.figures.append(("summary_metrics", figure))
    
    def _create_sustainability_visualizations(self) -> None:
        """Create sustainability-related visualizations."""
        if "sustainability" not in self.results:
            return
            
        sustainability = self.results["sustainability"]
        
        # Example: Plot adoption curves
        if "fertilizer_adoption_curves" in sustainability:
            data_frame = pd.DataFrame(sustainability["fertilizer_adoption_curves"])
            figure = px.line(
                data_frame, 
                x="year", 
                y="adoption_rate", 
                color="fertilizer_type",
                title="Fertilizer Adoption Over Time"
            )
            self.figures.append(("fertilizer_adoption", figure))
    
    def _create_production_tech_visualizations(self) -> None:
        """Create production technology visualizations."""
        # Implementation for production technology visualizations
        pass
    
    def _create_client_needs_visualizations(self) -> None:
        """Create client needs visualizations."""
        # Implementation for client needs visualizations
        pass
    
    def _generate_html(self) -> str:
        """Generate the complete HTML report.
        
        Returns:
            str: The complete HTML content
        """
        # HTML header with embedded CSS
        html_template = """
<!DOCTYPE html>
<html>
<head>
    <title>Fertilizer Industry Simulation Report</title>
    <script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
    <style>
        body {{ 
            font-family: Arial, sans-serif; 
            margin: 0; 
            padding: 20px; 
            line-height: 1.6;
        }}
        .header {{ 
            background-color: #2c3e50; 
            color: white; 
            padding: 20px; 
            margin-bottom: 20px; 
            border-radius: 5px;
        }}
        .section {{ 
            margin-bottom: 40px; 
            padding: 20px;
            background-color: #fff;
            border-radius: 5px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }}
        .plot {{ 
            margin: 20px 0; 
            border: 1px solid #eee;
            border-radius: 5px;
            padding: 15px;
        }}
        .metric-card {{
            border-left: 4px solid #3498db;
            background-color: #f8f9fa;
            border-radius: 4px;
            padding: 15px;
            margin: 10px 0;
            box-shadow: 0 1px 3px rgba(0,0,0,0.1);
        }}
        .metric-card h3 {{
            margin-top: 0;
            color: #2c3e50;
        }}
        .metrics-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
            gap: 15px;
            margin: 20px 0;
        }}
        h1, h2 {{
            color: #2c3e50;
        }}
        h2 {{
            border-bottom: 2px solid #eee;
            padding-bottom: 10px;
            margin-top: 30px;
        }}
    </style>
</head>
<body>
    <div class="header">
        <h1>Fertilizer Industry Simulation Report</h1>
        <p>Generated on {date}</p>
    </div>
    
    <div class="section">
        <h2>Summary Metrics</h2>
        <div class="metrics-grid">
            {summary_metrics}
        </div>
    </div>
    
    {visualizations}
    
    <script>
        // Plotly figures will be rendered here
        {plotly_js}
    </script>
</body>
</html>
""".format(
            date=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            summary_metrics=self._generate_summary_metrics(),
            visualizations=self._generate_visualizations(),
            plotly_js=self._generate_plotly_js()
        )
        
        return html_template
        
    def _generate_summary_metrics(self) -> str:
        """Generate HTML for summary metrics."""
        summary_metrics = ""
        if "summary_metrics" in self.results:
            for metric, value in self.results["summary_metrics"].items():
                summary_metrics += (
                    f'<div class="metric-card">'
                    f'<h3>{metric.replace("_", " ").title()}</h3>'
                    f'<p>{value}</p>'
                    f'</div>'
                )
        return summary_metrics or "<p>No summary metrics available</p>"
        
    def _generate_visualizations(self) -> str:
        """Generate HTML for visualizations."""
        plot_divs = []
        for i, (name, _) in enumerate(self.figures):
            plot_divs.append(
                f'<div class="section">'
                f'<h2>{name.replace("_", " ").title()}</h2>'
                f'<div id="plot-{i}" class="plot"></div>'
                f'</div>'
            )
        return "\n".join(plot_divs) or "<p>No visualizations available</p>"
        
    def _generate_plotly_js(self) -> str:
        """Generate JavaScript for Plotly visualizations."""
        plot_js = []
        for i, (_, figure) in enumerate(self.figures):
            plot_config = {
                'data': figure.to_dict(),
                'layout': figure.layout.to_plotly_json()
            }
            plot_js.append(
                f'Plotly.newPlot('  # noqa: E501
                f'"plot-{i}", '  # noqa: E131
                f'{plot_config["data"]}, '  # noqa: E131
                f'{plot_config["layout"]});'  # noqa: E131
            )
        return "\n".join(plot_js) or "// No plots to display"


def generate_report(results: Dict[str, Any], output_dir: Path) -> Path:
    """Generate a comprehensive HTML report for the simulation results.
    
    Args:
        results: Dictionary containing simulation results
        output_dir: Directory to save the report
        
    Returns:
        Path to the generated HTML report
    """
    generator = ReportGenerator(results, output_dir)
    return generator.generate_report()
