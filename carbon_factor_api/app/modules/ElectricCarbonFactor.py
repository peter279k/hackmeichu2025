import pymongo


class ElectronicCarbonFactor:
    def __init__(self):
        self.db_name = 'electric_carbon_factor'
        self.collection = 'electric_carbon_factor_collection'
        self.mongo_client = pymongo.MongoClient(
            host='mongodb',
            port=27017,
            username='admin',
            password='admin'
        )

    def get_electric_carbon_factor(self):
        db = self.mongo_client[self.db_name]
        ele_carbon_factor_collection = db[self.collection]

        result = ele_carbon_factor_collection.find_one()
        del result['_id']

        return result
