from typing import Optional

from pydantic import BaseModel


class StrategicPlanningBase(BaseModel):
    mission: Optional[str]
    vision: Optional[str]
    values: Optional[str]
    strategic_objectives: Optional[str]
    immediate_objectives: Optional[str]
    strengths: Optional[str]
    weaknesses: Optional[str]
    opportunities: Optional[str]
    threats: Optional[str]


class StrategicPlanningCreate(StrategicPlanningBase):
    pass


class StrategicPlanningUpdate(StrategicPlanningBase):
    pass


class StrategicPlanningInDBBase(StrategicPlanningBase):
    id: int
    race_id: int
    user_id: int

    class Config:
        from_attributes = True


class StrategicPlanning(StrategicPlanningInDBBase):
    pass


class StrategicPlanningInDB(StrategicPlanningInDBBase):
    pass
