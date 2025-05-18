import httpx

from fastapi.requests import Request
from fastapi.responses import JSONResponse

async def get_electric_carbon_factor(request: Request):
    status_code = 200
    req_url = 'http://carbon-factor-api:8000/api/v1/electric_carbon_factor'
    headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}

    try:
        response = httpx.get(req_url, headers=headers)
    except Exception as e:
        status_code = 500

        return JSONResponse(
            {
                'status': status_code,
                'message': str(e),
                'data': response.json(),
            },
            status_code=status_code
        )


    return JSONResponse(
        {
            'status': status_code,
            'message': 'Calculating electric carbon emission value is done.',
            'data': response.json(),
        },
        status_code=status_code
    )
