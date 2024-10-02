import numbers
from custom_exceptions.custom_exception import CustomException
from interface.calculator import Calculator


class CalculatorImp(Calculator):
    def addition(self, num1: int, num2: int) -> int:
        if isinstance(num1, numbers.Number) and isinstance(num2, numbers.Number): # this checked to make sure the input is of the numeric type
            result = num1 + num2
            return result
        else:
            raise CustomException("One or more entries were not numeric") # we want this message to match the test

    def subtraction(self, num1: int, num2: int) -> int:
        if isinstance(num1, numbers.Number) and isinstance(num2, numbers.Number):# this checked to make sure the input is of the numeric type
            result = num1 - num2
            return result
        else:
            raise CustomException("One or more entries were not numeric")# we want this message to match the test

    def rounding(self, result: float) -> int:
        if isinstance(result, numbers.Number):# this checked to make sure the input is of the numeric type
            return round(result) # the round method takes in a second value that determines to what decimal place you want the number rounded
        else:
            raise CustomException("Could not round the value")# we want this message to match the test