from app.modules.BaseCalculator import BaseCalculator


class CalculatorService:
    def __init__(self, calculator: BaseCalculator):
        self.calculator = calculator

    def calculate(self, activity_data: float, factor: float):
        return self.calculator.calculate(activity_data, factor)
