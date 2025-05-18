from .carbon_factor import *
from .carbon_calculator import *

from fastapi import APIRouter


carbon_calculator_router = APIRouter(tags=['Calculate Carbon Value'], prefix='/api/v1')
carbon_calculator_router.add_api_route('/calculate_electric', calculate_electric_carbon_emission, methods=['POST'], description='Calculate Electric Carbon Emission Value')

carbon_factor_router = APIRouter(tags=['Carbon Factor Value'], prefix='/api/v1')
carbon_factor_router.add_api_route('/electric_carbon_factor', get_electric_carbon_factor, methods=['GET'], description='Retrieve Electric Carbon Factor Value')
