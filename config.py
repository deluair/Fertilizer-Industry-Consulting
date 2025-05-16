from pydantic_settings import BaseSettings
from typing import List, Dict, Any
from pathlib import Path

class Settings(BaseSettings):
    # Application settings
    APP_NAME: str = "Fertilizer Industry Simulation"
    DEBUG: bool = False
    VERSION: str = "0.1.0"
    
    # Path configurations
    BASE_DIR: Path = Path(__file__).parent
    DATA_DIR: Path = BASE_DIR / "data"
    RAW_DATA_DIR: Path = DATA_DIR / "raw"
    PROCESSED_DATA_DIR: Path = DATA_DIR / "processed"
    SIMULATION_DIR: Path = BASE_DIR / "simulations"
    SCENARIO_DIR: Path = SIMULATION_DIR / "scenarios"
    REPORT_DIR: Path = BASE_DIR / "reports"
    
    # Simulation defaults
    DEFAULT_START_YEAR: int = 2025
    DEFAULT_END_YEAR: int = 2040
    DEFAULT_TIME_STEP: str = "1Y"  # 1 year time steps
    
    # Model parameters
    DEFAULT_SEED: int = 42
    DEFAULT_NUM_SIMULATIONS: int = 1000
    
    # Visualization settings
    PLOT_THEME: str = "plotly_white"
    PLOT_WIDTH: int = 1200
    PLOT_HEIGHT: int = 600
    
    # External data sources
    EXTERNAL_DATA_SOURCES: Dict[str, str] = {
        "fertilizer_market_data": "https://example.com/api/fertilizer-market-data",
        "sustainability_metrics": "https://example.com/api/sustainability-metrics"
    }
    
    class Config:
        env_file = ".env"
        case_sensitive = True

# Initialize settings
settings = Settings()
