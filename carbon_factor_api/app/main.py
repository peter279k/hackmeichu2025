from app.routers import *

from fastapi import FastAPI


description = '''
Carbon Factor Provider is used to provide carbon factors
'''
app = FastAPI(
    title='Carbon Factor Provider',
    description=description,
    version='1.0',
    contact={
        'name': 'Peter',
        'email': 'peter279k@gmail.com',
    }
)

app.include_router(carbon_factor_router)
