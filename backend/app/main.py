from app.routers import *

from fastapi import FastAPI


description = '''
Carbon Emission Generator is used to calculate carbon emission result
'''
app = FastAPI(
    title='Carbon Calculator',
    description=description,
    version='1.0',
    contact={
        'name': 'Peter',
        'email': 'peter279k@gmail.com',
    }
)

app.include_router(carbon_factor_router)
app.include_router(carbon_calculator_router)
