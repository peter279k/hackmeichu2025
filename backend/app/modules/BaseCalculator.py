from abc import ABC, abstractmethod


class BaseCalculator(ABC):
    @abstractmethod
    def calculate(self, activity_value: float, factor: float):
        pass
