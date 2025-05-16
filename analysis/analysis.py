"""Analysis utilities for simulation results."""

from typing import Dict, Any, List, Optional, Tuple
import numpy as np
import pandas as pd
from pathlib import Path


def analyze_results(results: Dict[str, Any]) -> Dict[str, Any]:
    """Analyze simulation results and generate key metrics.
    
    Args:
        results: Dictionary containing simulation results
        
    Returns:
        Dictionary containing analysis results
    """
    analysis = {}
    
    # Analyze sustainability metrics
    if "sustainability" in results:
        analysis["sustainability"] = _analyze_sustainability(results["sustainability"])
    
    # Analyze production technology metrics
    if "production_tech" in results:
        analysis["production_tech"] = _analyze_production_tech(results["production_tech"])
    
    # Analyze client needs metrics
    if "client_needs" in results:
        analysis["client_needs"] = _analyze_client_needs(results["client_needs"])
    
    # Calculate overall performance metrics
    analysis["performance_metrics"] = _calculate_performance_metrics(analysis)
    
    return analysis


def _analyze_sustainability(sustainability_data: Dict[str, Any]) -> Dict[str, Any]:
    """Analyze sustainability metrics."""
    analysis = {}
    
    # Calculate average adoption rates
    if "fertilizer_adoption" in sustainability_data:
        adoption_rates = []
        for adoption in sustainability_data["fertilizer_adoption"]:
            if hasattr(adoption, 'market_growth'):
                avg_rate = (adoption.market_growth.min_percentage + 
                           adoption.market_growth.max_percentage) / 2
                adoption_rates.append({
                    "fertilizer_type": adoption.fertilizer_type,
                    "average_adoption_rate": avg_rate
                })
        analysis["adoption_rates"] = adoption_rates
    
    # Extract other metrics
    analysis["metrics"] = sustainability_data.get("metrics", {})
    
    return analysis


def _analyze_production_tech(tech_data: Dict[str, Any]) -> Dict[str, Any]:
    """Analyze production technology metrics."""
    analysis = {}
    
    # Calculate average improvement rates
    if "technology_evolution" in tech_data:
        improvements = []
        for tech in tech_data["technology_evolution"]:
            if isinstance(tech, dict) and "trajectory_or_curve" in tech:
                trajectory = tech["trajectory_or_curve"].get("trajectory", [])
                if trajectory and len(trajectory) > 1:
                    start = trajectory[0][1]
                    end = trajectory[-1][1]
                    improvement = ((end - start) / abs(start)) * 100 if start != 0 else 0
                    improvements.append({
                        "technology": tech.get("technology_name", "Unknown"),
                        "improvement_percent": improvement
                    })
        analysis["technology_improvements"] = improvements
    
    # Extract other metrics
    analysis["metrics"] = tech_data.get("metrics", {})
    
    return analysis


def _analyze_client_needs(client_data: Dict[str, Any]) -> Dict[str, Any]:
    """Analyze client needs metrics."""
    analysis = {}
    
    # Calculate priority changes
    if "priority_evolution" in client_data:
        priorities = []
        for priority in client_data["priority_evolution"]:
            if isinstance(priority, dict) and "evolution_trend" in priority:
                trajectory = priority["evolution_trend"].get("trajectory", [])
                if trajectory and len(trajectory) > 1:
                    start = trajectory[0][1]
                    end = trajectory[-1][1]
                    change = end - start
                    priorities.append({
                        "priority_area": priority.get("priority_area", "Unknown"),
                        "start_value": start,
                        "end_value": end,
                        "change": change
                    })
        analysis["priority_changes"] = priorities
    
    # Extract other metrics
    analysis["metrics"] = client_data.get("metrics", {})
    
    return analysis


def _calculate_performance_metrics(analysis: Dict[str, Any]) -> Dict[str, float]:
    """Calculate overall performance metrics from the analysis."""
    metrics = {}
    
    # Calculate overall sustainability score (0-100)
    sustainability_score = 0
    if "sustainability" in analysis:
        metrics["sustainability_score"] = analysis["sustainability"].get("metrics", {}).get("sustainable_share", 0) * 100
    
    # Calculate technology advancement score
    tech_score = 0
    if "production_tech" in analysis:
        tech_improvements = analysis["production_tech"].get("technology_improvements", [])
        if tech_improvements:
            tech_score = sum(imp["improvement_percent"] for imp in tech_improvements) / len(tech_improvements)
    metrics["technology_advancement"] = tech_score
    
    # Calculate client satisfaction score (0-10 scale)
    client_score = 0
    if "client_needs" in analysis:
        priorities = analysis["client_needs"].get("priority_changes", [])
        if priorities:
            client_score = sum(p["end_value"] for p in priorities) / len(priorities)
    metrics["client_satisfaction"] = client_score
    
    # Calculate overall score (weighted average)
    overall_score = (
        metrics.get("sustainability_score", 0) * 0.4 +
        metrics.get("technology_advancement", 0) * 0.3 +
        metrics.get("client_satisfaction", 0) * 10 * 0.3  # Scale to 0-100
    )
    metrics["overall_score"] = min(100, max(0, overall_score))  # Ensure between 0-100
    
    return metrics


def save_analysis(analysis: Dict[str, Any], output_dir: str) -> None:
    """Save analysis results to files.
    
    Args:
        analysis: Dictionary containing analysis results
        output_dir: Directory to save the analysis results
    """
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)
    
    # Save overall metrics
    if "performance_metrics" in analysis:
        metrics_df = pd.DataFrame([analysis["performance_metrics"]])
        metrics_df.to_csv(output_path / "performance_metrics.csv", index=False)
    
    # Save detailed analysis for each component
    for component in ["sustainability", "production_tech", "client_needs"]:
        if component in analysis:
            component_path = output_path / component
            component_path.mkdir(exist_ok=True)
            
            # Save metrics
            if "metrics" in analysis[component]:
                pd.DataFrame([analysis[component]["metrics"]]).to_csv(
                    component_path / "metrics.csv", index=False
                )
            
            # Save detailed data
            if component == "sustainability" and "adoption_rates" in analysis[component]:
                pd.DataFrame(analysis[component]["adoption_rates"]).to_csv(
                    component_path / "adoption_rates.csv", index=False
                )
            elif component == "production_tech" and "technology_improvements" in analysis[component]:
                pd.DataFrame(analysis[component]["technology_improvements"]).to_csv(
                    component_path / "technology_improvements.csv", index=False
                )
            elif component == "client_needs" and "priority_changes" in analysis[component]:
                pd.DataFrame(analysis[component]["priority_changes"]).to_csv(
                    component_path / "priority_changes.csv", index=False
                )
