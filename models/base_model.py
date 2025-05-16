from pydantic import BaseModel, Field
from typing import List, Optional, Tuple, Dict, Any, Union, TypeVar, Type, Callable
import json
from datetime import datetime, date, time
from decimal import Decimal
from enum import Enum
from uuid import UUID

T = TypeVar('T')

def model_to_dict(model: Any) -> Any:
    """Recursively convert a model to a dictionary."""
    if isinstance(model, (str, int, float, bool, type(None))):
        return model
    if isinstance(model, (datetime, date, time)):
        return model.isoformat()
    if isinstance(model, Decimal):
        return float(model)
    if isinstance(model, (list, tuple)):
        return [model_to_dict(item) for item in model]
    if isinstance(model, dict):
        return {key: model_to_dict(value) for key, value in model.items()}
    if hasattr(model, 'model_dump'):
        return model_to_dict(model.model_dump())
    if hasattr(model, 'dict'):
        return model_to_dict(model.dict())
    if hasattr(model, '__dict__'):
        return model_to_dict(model.__dict__)
    return str(model)

class SerializableModel(BaseModel):
    """Base model with enhanced JSON serialization support."""
    
    def dict(self, *args, **kwargs) -> Dict[str, Any]:
        """Convert model to dictionary with proper handling of nested models."""
        if hasattr(super(), 'model_dump'):
            # Pydantic v2
            result = super().model_dump(*args, **{**kwargs, 'exclude_none': True})
        else:
            # Pydantic v1
            result = super().dict(*args, **{**kwargs, 'exclude_none': True})
        return model_to_dict(result)
    
    def json(self, *args, **kwargs) -> str:
        """Convert model to JSON string with support for nested models and custom types."""
        if 'default' not in kwargs:
            kwargs['default'] = lambda o: model_to_dict(o)
        if 'cls' not in kwargs:
            kwargs['cls'] = json.JSONEncoder
        return json.dumps(self.dict(), **{k: v for k, v in kwargs.items() if k in ['default', 'cls', 'indent', 'separators', 'sort_keys']})

class SimulationPeriod(SerializableModel):
    start_year: int = 2025
    end_year: int = 2040

class PercentageRange(SerializableModel):
    min_percentage: float = Field(..., ge=0, le=100)
    max_percentage: float = Field(..., ge=0, le=100)

class Trend(SerializableModel):
    name: str
    description: Optional[str] = None
    # Example: [(year, value), (year, value)]
    trajectory: Optional[List[Tuple[int, float]]] = None