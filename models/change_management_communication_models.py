from pydantic import BaseModel, Field
from typing import List, Optional

class StakeholderEngagementStrategyElement(BaseModel):
    stakeholder_group: str  # e.g., Leadership, Team, Clients, Partners
    engagement_approach: str # e.g., Alignment approach, Engagement methodology, Communication framework
    description: Optional[str] = None

class CommunicationCampaignElement(BaseModel):
    element_name: str  # e.g., Key message development, Channel selection optimization
    description: Optional[str] = None
    # Specific activities or metrics can be detailed here

class ChangeManagementAndCommunication(BaseModel):
    stakeholder_engagement_strategy: List[StakeholderEngagementStrategyElement]
    communication_campaign_design: List[CommunicationCampaignElement] 