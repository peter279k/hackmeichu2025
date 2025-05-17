from .carbon_factor import *

from fastapi import APIRouter


carbon_factor_router = APIRouter(tags=['Provide Carbon Factor'], prefix='/api/v1')
carbon_factor_router.add_api_route('/electric_carbon_factor', electric_carbon_factor, methods=['GET'], description='Electric Carbon Factor')
