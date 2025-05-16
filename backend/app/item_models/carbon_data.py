from pydantic import BaseModel, validator


class ElectricCarbonEmissionData(BaseModel):
    activity_data: float
    factor: float


    @validator('activity_data')
    def activity_data_must_be_positive(cls, value):
        if value < 0:
            raise ValueError("activity_data must be positive float.")
        return value

    @validator('factor')
    def factor_must_be_positive(cls, value):
        if value < 0:
            raise ValueError("factor must be positive float.")
        return value

