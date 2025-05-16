from pydantic import BaseModel, Field
from typing import List, Optional

class PartnerSelectionCriteria(BaseModel):
    partner_type: str # e.g., Agtech partner, Academic collaboration, Research organization
    selection_approach_description: str
    key_criteria: List[str]

class IntegrationFrameworkElement(BaseModel):
    element_name: str # e.g., Knowledge sharing mechanisms, Joint go-to-market approach
    description: str
    # Specific metrics or methods for this element can be added

class PartnershipAndEcosystemStrategy(BaseModel):
    description: str = "Systematic approach for developing and managing partnerships."
    partner_selection_approaches: List[PartnerSelectionCriteria]
    integration_framework_elements: List[IntegrationFrameworkElement] 