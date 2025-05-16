from app.modules.BaseCalculator import BaseCalculator


class ElectronicCalculator(BaseCalculator):
    def calculate(self, activity_data: float, factor: float):
        return round(activity_data * factor / 1000, 2)
