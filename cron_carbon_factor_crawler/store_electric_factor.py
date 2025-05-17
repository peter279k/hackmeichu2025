import os
import sys
import csv
import pymongo


path = '/gwp-factors/datasets/electric_co2e.csv'
if os.path.isfile(path) is False:
    print(f'{path} is not found.')
    sys.exit(1)

electric_factor_dict = {'data': []}
with open(path, 'r') as f:
    reader = csv.reader(f)
    for row in reader[1:]:
        electric_factor_dict['data'] += {
            'year': row[0],
            'co2e': row[1],
        },


mongo_client = pymongo.MongoClient(
    host='mongodb',
    port=27017,
    username='admin',
    password='admin'
)

db = mongo_client['electric_carbon_factor']
electric_carbon_factor_collection = db['electric_carbon_factor_collection']

deleted_result = electric_carbon_factor_collection.delete_one(electric_factor_dict)
print(f'deleted_result: {deleted_result.deleted_count}')

inserted_result = electric_carbon_factor_collection.insert_one(electric_factor_dict)
print(f'inserted_result: {inserted_result.inserted_id}')
