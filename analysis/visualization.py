"""Visualization utilities for simulation results."""

from pathlib import Path
from typing import Dict, Any, Optional, List
import json
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots


def plot_simulation_results(results: Dict[str, Any], output_dir: str) -> None:
    """Generate and save visualizations for simulation results.
    
    Args:
        results: Dictionary containing simulation results
        output_dir: Directory to save the generated plots
    """
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)
    
    # Create summary metrics dashboard
    _create_summary_dashboard(results, output_path)
    
    # Create detailed visualizations for each component
    if "sustainability" in results:
        _plot_sustainability_metrics(results["sustainability"], output_path)
    
    if "production_tech" in results:
        _plot_production_tech_metrics(results["production_tech"], output_path)
    
    if "client_needs" in results:
        _plot_client_needs_metrics(results["client_needs"], output_path)


def _create_summary_dashboard(results: Dict[str, Any], output_dir: Path) -> None:
    """Create a summary dashboard with key metrics."""
    if "summary_metrics" not in results:
        return
    
    metrics = results["summary_metrics"]
    
    # Create a simple bar chart of key metrics
    fig = go.Figure()
    
    metric_names = list(metrics.keys())
    metric_values = [metrics[name] for name in metric_names]
    
    fig.add_trace(go.Bar(
        x=metric_names,
        y=metric_values,
        text=[f"{v:.1f}%" for v in metric_values],
        textposition='auto',
        marker_color='#2ecc71'
    ))
    
    fig.update_layout(
        title="Key Performance Indicators",
        xaxis_title="Metric",
        yaxis_title="Value (%)",
        template="plotly_white",
        height=500,
        width=800
    )
    
    # Save the figure
    fig.write_html(str(output_dir / "summary_dashboard.html"))
    fig.write_image(str(output_dir / "summary_dashboard.png"), scale=2)


def _plot_sustainability_metrics(sustainability_data: Dict[str, Any], output_dir: Path) -> None:
    """Create visualizations for sustainability metrics."""
    # Example: Plot fertilizer adoption curves
    if "fertilizer_adoption" in sustainability_data:
        fig = go.Figure()
        
        for adoption in sustainability_data["fertilizer_adoption"]:
            years = np.linspace(2025, 2040, 16)
            min_vals = [adoption.market_growth.min_percentage] * len(years)
            max_vals = [adoption.market_growth.max_percentage] * len(years)
            
            fig.add_trace(go.Scatter(
                x=list(years) + years[::-1],
                y=list(min_vals) + max_vals[::-1],
                fill='toself',
                name=f"{adoption.fertilizer_type} (Range)",
                line=dict(width=0),
                opacity=0.2
            ))
            
            # Add mean line
            mean_vals = [(min_v + max_v) / 2 for min_v, max_v in zip(min_vals, max_vals)]
            fig.add_trace(go.Scatter(
                x=years,
                y=mean_vals,
                name=f"{adoption.fertilizer_type} (Mean)",
                line=dict(width=2)
            ))
        
        fig.update_layout(
            title="Fertilizer Market Share Projection (2025-2040)",
            xaxis_title="Year",
            yaxis_title="Market Share (%)",
            template="plotly_white",
            height=600,
            width=900
        )
        
        fig.write_html(str(output_dir / "fertilizer_adoption.html"))
        fig.write_image(str(output_dir / "fertilizer_adoption.png"), scale=2)


def _plot_production_tech_metrics(tech_data: Dict[str, Any], output_dir: Path) -> None:
    """Create visualizations for production technology metrics."""
    if "technology_evolution" not in tech_data:
        return
    
    # Create a line plot for each technology evolution
    fig = go.Figure()
    
    for tech in tech_data["technology_evolution"]:
        if "trajectory_or_curve" in tech and "trajectory" in tech["trajectory_or_curve"]:
            trajectory = tech["trajectory_or_curve"]["trajectory"]
            years = [point[0] for point in trajectory]
            values = [point[1] for point in trajectory]
            
            fig.add_trace(go.Scatter(
                x=years,
                y=values,
                mode='lines+markers',
                name=tech.get("technology_name", "Unknown Technology")
            ))
    
    if len(fig.data) > 0:
        fig.update_layout(
            title="Production Technology Evolution",
            xaxis_title="Year",
            yaxis_title=tech_data["technology_evolution"][0].get("metric_type", "Value"),
            template="plotly_white",
            height=500,
            width=800
        )
        
        fig.write_html(str(output_dir / "tech_evolution.html"))
        fig.write_image(str(output_dir / "tech_evolution.png"), scale=2)


def _plot_client_needs_metrics(client_data: Dict[str, Any], output_dir: Path) -> None:
    """Create visualizations for client needs metrics."""
    if "priority_evolution" not in client_data:
        return
    
    # Create a radar chart for client priorities
    categories = []
    values = []
    
    for priority in client_data["priority_evolution"]:
        if "evolution_trend" in priority and "trajectory" in priority["evolution_trend"]:
            # Get the final value (latest year)
            trajectory = priority["evolution_trend"]["trajectory"]
            if trajectory:
                categories.append(priority.get("priority_area", "Unknown Priority"))
                values.append(trajectory[-1][1])  # Get the last value
    
    if categories and values:
        fig = go.Figure()
        
        fig.add_trace(go.Scatterpolar(
            r=values,
            theta=categories,
            fill='toself',
            name='Client Priority'
        ))
        
        fig.update_layout(
            polar=dict(
                radialaxis=dict(
                    visible=True,
                    range=[0, 10]  # Assuming 1-10 scale for priorities
                )
            ),
            showlegend=True,
            title="Client Priority Evolution",
            template="plotly_white",
            height=600,
            width=800
        )
        
        fig.write_html(str(output_dir / "client_priorities.html"))
        fig.write_image(str(output_dir / "client_priorities.png"), scale=2)
