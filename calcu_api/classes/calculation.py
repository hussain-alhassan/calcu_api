# coding=utf-8
"""
Calculation class does the actual calculation and returns the JSON response.
"""
import math


class Calculation:

    @staticmethod
    def add(first_number, second_number):
        store_report('add', first_number, second_number)

        response = {'error': 'Something went wrong!'}
        try:
            result = float(first_number) + float(second_number)
            response = {
                'operator': '+',
                'first_number': first_number,
                'second_number': second_number,
                'result': result
            }
        except ValueError:
            print('Add entries have to be numbers!')

        return response

    @staticmethod
    def subtract(first_number, second_number):
        store_report('subtract', first_number, second_number)

        response = {'error': 'Something went wrong!'}
        try:
            result = float(first_number) - float(second_number)
            response = {
                'operator': '-',
                'first_number': first_number,
                'second_number': second_number,
                'result': result
            }
        except ValueError:
            print('Subtract entries have to be numbers!')

        return response

    @staticmethod
    def multiply(first_number, second_number):
        store_report('multiply', first_number, second_number)

        response = {'error': 'Something went wrong!'}
        try:
            result = float(first_number) * float(second_number)
            response = {
                'operator': '*',
                'first_number': first_number,
                'second_number': second_number,
                'result': result
            }
        except ValueError:
            print('Multiply entries have to be numbers!')

        return response

    @staticmethod
    def divide(first_number, second_number):
        store_report('divide', first_number, second_number)

        response = {'error': 'Something went wrong!'}
        try:
            result = float(first_number) / float(second_number)
            response = {
                'operator': '/',
                'first_number': first_number,
                'second_number': second_number,
                'result': float("%.2f" % result)
            }
        except ValueError:
            print('Divide entries have to be numbers!')

        except ZeroDivisionError:
            response = {'error': 'Divide can not divide by zero!'}
            print('Divide can not divide by zero!')

        # # if dividing by zero
        # if float(second_number) == 0:
        #     raise ZeroDivisionError()

        return response

    @staticmethod
    def square_root(sqrt_number):
        store_report('square_root', sqrt_number)

        response = {'error': 'Something went wrong!'}
        try:
            result = math.sqrt(float(sqrt_number))
            response = {
                'operator': '√',
                'square_root_number': sqrt_number,
                'result': float("%.2f" % result)
            }
        except ValueError:
            print('Square root entry has to be a number!')

        return response

    @staticmethod
    def cube_root(cube_root_number):
        store_report('cube_root', cube_root_number)

        response = {'error': 'Something went wrong!'}
        try:
            result = math.pow(float(cube_root_number), 1/3)
            response = {
                'operator': '∛',
                'cube_root_number': cube_root_number,
                'result': float("%.2f" % result)
            }
        except ValueError:
            print('Cube root entry has to be a number!')

        return response

    @staticmethod
    def power(base_number, exponent_number):
        store_report('power', base_number, exponent_number)

        response = {'error': 'Something went wrong!'}
        try:
            result = math.pow(float(base_number), float(exponent_number))
            response = {
                'operator': '^',
                'base_number': base_number,
                'exponent_number': exponent_number,
                'result': float("%.2f" % result)
            }
        except ValueError:
            print('Power entries have to be numbers!')

        return response

    @staticmethod
    def factorial(factorial_number):
        store_report('factorial', factorial_number)

        response = {'error': 'Something went wrong!'}
        try:
            result = math.factorial(float(factorial_number))
            response = {
                'operator': '!',
                'factorial_number': factorial_number,
                'result': float("%.2f" % result)
            }
        except ValueError:
            print('Factorial entry has to be a number greater than or equal to 1!')

        return response


def store_report(function_name, first_number, second_number=None):
    from calcu_api.models import Report

    rprt_obj = Report()
    rprt_obj.save(function_name, first_number, second_number)
