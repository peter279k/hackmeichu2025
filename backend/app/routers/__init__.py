from .carbon_calculator import *

from fastapi import APIRouter


carbon_calculator_router = APIRouter(tags=['Calculate Carbon Value'], prefix='/api/v1')
carbon_calculator_router.add_api_route('/calculate_electric', calculate_electric_carbon_emission(), methods=['POST'], description='Calculate Electric Carbon Emission Value')
