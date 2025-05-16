"""
Visualization utilities for simulation results with enhanced charts and interactivity.
"""

from pathlib import Path
from typing import Dict, Any, Optional, List, Tuple, Union
import json
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from plotly.colors import qualitative

# Color scheme for consistent styling
COLOR_SCHEME = {
    'primary': '#2c3e50',
    'secondary': '#3498db',
    'success': '#2ecc71',
    'danger': '#e74c3c',
    'warning': '#f39c12',
    'info': '#1abc9c',
    'light': '#ecf0f1',
    'dark': '#2c3e50',
}

# Chart configuration
CHART_CONFIG = {
    'displayModeBar': True,
    'responsive': True,
    'displaylogo': False,
    'modeBarButtonsToAdd': ['select2d', 'lasso2d', 'zoomIn', 'zoomOut', 'resetScale2d'],
    'toImageButtonOptions': {
        'format': 'png',
        'filename': 'chart_export',
        'height': 600,
        'width': 1000,
        'scale': 2
    }
}


def plot_simulation_results(results: Dict[str, Any], output_dir: str) -> Dict[str, go.Figure]:
    """Generate and save visualizations for simulation results.
    
    Args:
        results: Dictionary containing simulation results
        output_dir: Directory to save the generated plots
        
    Returns:
        Dictionary mapping figure names to Plotly figure objects
    """
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)
    
    figures = {}
    
    # Create summary metrics dashboard
    summary_fig = _create_summary_dashboard(results, output_path)
    if summary_fig:
        figures["summary"] = summary_fig
    
    # Create detailed visualizations for each component
    if "sustainability" in results:
        sustainability_figs = _plot_sustainability_metrics(results["sustainability"], output_path)
        figures.update(sustainability_figs)
    
    if "production_tech" in results:
        tech_figs = _plot_production_tech_metrics(results["production_tech"], output_path)
        figures.update(tech_figs)
    
    if "client_needs" in results:
        client_figs = _plot_client_needs_metrics(results["client_needs"], output_path)
        figures.update(client_figs)
    
    # Save all figures as HTML for interactive viewing
    for name, fig in figures.items():
        if fig is not None:
            fig.write_html(str(output_path / f"{name}.html"), config=CHART_CONFIG)
    
    return figures


def _create_summary_dashboard(results: Dict[str, Any], output_dir: Path) -> Optional[go.Figure]:
    """Create a summary dashboard with key metrics.
    
    Returns:
        Plotly figure object or None if no metrics available
    """
    if "summary_metrics" not in results or not results["summary_metrics"]:
        return None
    
    metrics = results["summary_metrics"]
    
    # Create a dashboard with multiple visualizations
    fig = make_subplots(
        rows=2, 
        cols=2,
        subplot_titles=(
            "Key Performance Indicators",
            "Sustainability Score",
            "Market Trends",
            "Cost Breakdown"
        ),
        specs=[[{"type": "bar"}, {"type": "indicator"}],
              [{"type": "scatter"}, {"type": "pie"}]]
    )
    
    # 1. Bar chart for key metrics
    metric_names = [name.replace('_', ' ').title() for name in metrics.keys()]
    metric_values = list(metrics.values())
    
    # Categorize metrics
    performance_metrics = {}
    for name, value in metrics.items():
        if any(term in name.lower() for term in ['growth', 'efficiency', 'savings']):
            performance_metrics[name] = value
    
    if performance_metrics:
        fig.add_trace(
            go.Bar(
                x=list(performance_metrics.keys()),
                y=list(performance_metrics.values()),
                marker_color=COLOR_SCHEME['secondary'],
                name="Performance Metrics"
            ),
            row=1, col=1
        )
    
    # 2. Gauge for overall score
    if 'sustainability_score' in metrics:
        fig.add_trace(
            go.Indicator(
                mode="gauge+number+delta",
                value=metrics.get('sustainability_score', 0),
                title={'text': "Sustainability Score"},
                gauge={
                    'axis': {'range': [0, 100], 'tickwidth': 1, 'tickcolor': COLOR_SCHEME['dark']},
                    'bar': {'color': COLOR_SCHEME['success']},
                    'steps': [
                        {'range': [0, 33], 'color': COLOR_SCHEME['danger']},
                        {'range': [33, 66], 'color': COLOR_SCHEME['warning']},
                        {'range': [66, 100], 'color': COLOR_SCHEME['success']},
                    ],
                }
            ),
            row=1, col=2
        )
    
    # 3. Time series for market trends (if available)
    if "market_trends" in results.get("additional_metrics", {}):
        df = pd.DataFrame(results["additional_metrics"]["market_trends"])
        for col in df.columns[1:]:  # Skip date column
            fig.add_trace(
                go.Scatter(
                    x=df[df.columns[0]],
                    y=df[col],
                    mode='lines+markers',
                    name=col.replace('_', ' ').title(),
                    line=dict(width=2)
                ),
                row=2, col=1
            )
    
    # 4. Pie chart for cost breakdown (if available)
    if "cost_breakdown" in results.get("additional_metrics", {}):
        cost_data = results["additional_metrics"]["cost_breakdown"]
        labels = list(cost_data.keys())
        values = list(cost_data.values())
        
        fig.add_trace(
            go.Pie(
                labels=labels,
                values=values,
                textinfo='percent+label',
                hole=.4,
                marker_colors=px.colors.sequential.Viridis
            ),
            row=2, col=2
        )
    
    # Update layout
    fig.update_layout(
        height=800,
        showlegend=True,
        title_text="Fertilizer Industry Simulation Dashboard",
        template="plotly_white",
        margin=dict(t=100, b=50, l=50, r=50)
    )
    
    return fig
    
    # Save the figure
    fig.write_html(str(output_dir / "summary_dashboard.html"))
    fig.write_image(str(output_dir / "summary_dashboard.png"), scale=2)


def _plot_sustainability_metrics(sustainability_data: Dict[str, Any], output_dir: Path) -> Dict[str, go.Figure]:
    """Create visualizations for sustainability metrics.
    
    Args:
        sustainability_data: Dictionary containing sustainability metrics
        output_dir: Directory to save the generated plots
        
    Returns:
        Dictionary mapping figure names to Plotly figure objects
    """
    figures = {}
    
    # Carbon footprint over time
    if "carbon_footprint" in sustainability_data:
        df = pd.DataFrame(sustainability_data["carbon_footprint"])
        
        # Create a line chart with area fill
        fig = go.Figure()
        
        # Add the main line
        fig.add_trace(go.Scatter(
            x=df['year'],
            y=df['value'],
            mode='lines+markers',
            name='CO2 Emissions',
            line=dict(width=3, color=COLOR_SCHEME['danger']),
            marker=dict(size=8),
            hovertemplate='%{x}<br>Emissions: %{y:,.0f} tons<extra></extra>'
        ))
        
        # Add filled area
        fig.add_trace(go.Scatter(
            x=pd.concat([df['year'], df['year'][::-1]]),
            y=pd.concat([df['value'], pd.Series([0] * len(df))]),
            fill='tozeroy',
            mode='none',
            showlegend=False,
            hoverinfo='skip',
            fillcolor=f"rgba(231, 76, 60, 0.2)"  # Semi-transparent red
        ))
        
        # Update layout
        fig.update_layout(
            title=dict(
                text='<b>Carbon Footprint Over Time</b>',
                x=0.5,
                xanchor='center',
                font=dict(size=20)
            ),
            xaxis_title='Year',
            yaxis_title='CO₂ Emissions (tons)',
            template='plotly_white',
            height=500,
            margin=dict(t=80, b=80, l=80, r=40),
            hovermode='x unified',
            xaxis=dict(
                showgrid=True,
                gridwidth=1,
                gridcolor='#f0f0f0',
                tickmode='linear',
                dtick=1
            ),
            yaxis=dict(
                gridcolor='#f0f0f0',
                gridwidth=1
            ),
            plot_bgcolor='rgba(0,0,0,0)'
        )
        
        # Add annotation for reduction percentage if multiple years
        if len(df) > 1:
            reduction = ((df['value'].iloc[-1] - df['value'].iloc[0]) / df['value'].iloc[0]) * 100
            fig.add_annotation(
                x=df['year'].iloc[-1],
                y=df['value'].iloc[-1],
                text=f"{reduction:+.1f}% change",
                showarrow=True,
                arrowhead=1,
                ax=0,
                ay=-40,
                bgcolor='white',
                bordercolor=COLOR_SCHEME['dark']
            )
        
        figures["carbon_footprint"] = fig
    
    # Energy mix visualization
    if "energy_mix" in sustainability_data:
        df = pd.DataFrame(sustainability_data["energy_mix"])
        
        # Sort by percentage for better visualization
        df = df.sort_values('percentage', ascending=False)
        
        # Create a donut chart
        fig = go.Figure()
        
        fig.add_trace(go.Pie(
            labels=df['source'],
            values=df['percentage'],
            hole=0.6,
            textinfo='percent+label',
            textposition='inside',
            marker=dict(colors=px.colors.sequential.Viridis),
            hovertemplate='%{label}<br>%{percent:.1%}<extra></extra>',
            sort=False
        ))
        
        # Update layout
        fig.update_layout(
            title=dict(
                text='<b>Energy Mix Distribution</b>',
                x=0.5,
                xanchor='center',
                font=dict(size=20)
            ),
            showlegend=False,
            height=500,
            margin=dict(t=80, b=80, l=40, r=40),
            annotations=[
                dict(
                    text='Energy<br>Sources',
                    x=0.5, y=0.5,
                    font_size=16,
                    showarrow=False
                )
            ]
        )
        
        figures["energy_mix"] = fig
    
    # Water usage visualization if available
    if "water_usage" in sustainability_data:
        df = pd.DataFrame(sustainability_data["water_usage"])
        
        # Create a bar chart with line for target
        fig = go.Figure()
        
        fig.add_trace(go.Bar(
            x=df['year'],
            y=df['value'],
            name='Water Usage',
            marker_color=COLOR_SCHEME['info'],
            text=df['value'].round(1),
            textposition='auto',
            hovertemplate='%{x}<br>Usage: %{y:,.0f} m³/ton<extra></extra>'
        ))
        
        # Add target line if available
        if 'target' in df.columns:
            fig.add_trace(go.Scatter(
                x=df['year'],
                y=df['target'],
                mode='lines+markers',
                name='Target',
                line=dict(dash='dash', color=COLOR_SCHEME['warning'], width=2),
                hovertemplate='%{x}<br>Target: %{y:,.0f} m³/ton<extra></extra>'
            ))
        
        # Update layout
        fig.update_layout(
            title=dict(
                text='<b>Water Usage per Ton of Product</b>',
                x=0.5,
                xanchor='center',
                font=dict(size=20)
            ),
            xaxis_title='Year',
            yaxis_title='Water Usage (m³/ton)',
            template='plotly_white',
            height=500,
            margin=dict(t=80, b=80, l=80, r=40),
            hovermode='x unified',
            legend=dict(
                orientation='h',
                yanchor='bottom',
                y=1.02,
                xanchor='right',
                x=1
            )
        )
        
        figures["water_usage"] = fig
    
    return figures
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
    
