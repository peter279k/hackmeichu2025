from app.modules.BaseCalculator import BaseCalculator


class CalculatorService:
    def __init__(self, calculator: BaseCalculator):
        self.calculator = calculator

    def calculating(self, activity_value: float, factor: float):
        return self.calculator.calculate(activity_value, factor)
