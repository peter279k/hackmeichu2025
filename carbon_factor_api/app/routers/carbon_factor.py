from fastapi.requests import Request
from fastapi.responses import JSONResponse

from carbon_factor_api.app.modules import ElectricCarbonFactor


async def electric_carbon_factor(request: Request):
    status_code = 200

    try:
        ele_carbon_factor = ElectricCarbonFactor.ElectronicCarbonFactor()
        ele_carbon_factor_list = ele_carbon_factor.get_electric_carbon_factor()
    except Exception as e:
        status_code = 500

        return JSONResponse(
            {
                'status': status_code,
                'message': str(e),
                'data': [],
            },
            status_code=status_code
        )


    return JSONResponse(
        {
            'status': status_code,
            'message': 'Calculating electric carbon emission value is done.',
            'data': ele_carbon_factor_list,
        },
        status_code=status_code
    )
