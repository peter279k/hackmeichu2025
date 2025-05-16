from app.item_models.carbon_data import *
from app.modules import CalculatorService, ElectronicCalculator

from fastapi.requests import Request
from fastapi.responses import JSONResponse


async def calculate_electric_carbon_emission(request: Request, item: ElectricCarbonEmissionData):
    status_code = 200
    item_dict = item.model_dump()
    activity_data = item_dict['activity_data']
    factor = item_dict['factor']

    try:
        calculator_service = CalculatorService.CalculatorService(ElectronicCalculator.ElectronicCalculator())
        calculated_result = calculator_service.calculate(activity_data, factor)
    except Exception as e:
        status_code = 500

        return JSONResponse(
            {
                'status': status_code,
                'message': str(e),
                'data': item_dict,
            },
            status_code=status_code
        )


    return JSONResponse(
        {
            'status': status_code,
            'message': 'Calculating electric carbon emission value is done.',
            'data': calculated_result,
        },
        status_code=status_code
    )
