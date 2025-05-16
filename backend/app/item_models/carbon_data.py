from pydantic import BaseModel, field_validator


class ElectricCarbonEmissionData(BaseModel):
    activity_data: float
    factor: float


    @field_validator('activity_data')
    def activity_data_must_be_positive(cls, value):
        if value < 0:
            raise ValueError("activity_data must be positive float.")
        return value

    @field_validator('factor')
    def factor_must_be_positive(cls, value):
        if value < 0:
            raise ValueError("factor must be positive float.")
        return value

