from app.modules.BaseCalculator import BaseCalculator


class ElectronicCalculator(BaseCalculator):
    def calculate(self, activity_value: float, factor: float):
        return round(activity_value * factor / 1000, 2)
