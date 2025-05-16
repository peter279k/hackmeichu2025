from pydantic import BaseModel


class ElectricCarbonEmissionData(BaseModel):
    activity_data: float
    factor: float
