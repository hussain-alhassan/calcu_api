# coding=utf-8
"""
Calculation class does the actual calculation and returns the JSON response.
"""
import math


class Calculation:

    @staticmethod
    def add(first_number, second_number):
        store_report('add', first_number, second_number)

        result = float(first_number) + float(second_number)
        response = {
            'operator': '+',
            'first_number': first_number,
            'second_number': second_number,
            'result': result
        }

        return response

    @staticmethod
    def subtract(first_number, second_number):
        store_report('subtract', first_number, second_number)

        result = float(first_number) - float(second_number)
        response = {
            'operator': '-',
            'first_number': first_number,
            'second_number': second_number,
            'result': result
        }

        return response

    @staticmethod
    def multiply(first_number, second_number):
        store_report('multiply', first_number, second_number)

        result = float(first_number) * float(second_number)
        response = {
            'operator': '*',
            'first_number': first_number,
            'second_number': second_number,
            'result': result
        }

        return response

    @staticmethod
    def divide(first_number, second_number):
        store_report('divide', first_number, second_number)

        result = float(first_number) / float(second_number)
        response = {
            'operator': '/',
            'first_number': first_number,
            'second_number': second_number,
            'result': float("%.2f" % result)
        }

        return response

    @staticmethod
    def square_root(sqrt_number):
        store_report('square_root', sqrt_number)

        result = math.sqrt(float(sqrt_number))
        response = {
            'operator': '√',
            'square_root_number': sqrt_number,
            'result': float("%.2f" % result)
        }

        return response

    @staticmethod
    def cube_root(cube_root_number):
        store_report('cube_root', cube_root_number)

        result = math.pow(float(cube_root_number), 1/3)
        response = {
            'operator': '∛',
            'cube_root_number': cube_root_number,
            'result': float("%.2f" % result)
        }

        return response

    @staticmethod
    def power(base_number, exponent_number):
        store_report('power', base_number, exponent_number)

        result = math.pow(float(base_number), float(exponent_number))
        response = {
            'operator': '^',
            'base_number': base_number,
            'exponent_number': exponent_number,
            'result': float("%.2f" % result)
        }

        return response

    @staticmethod
    def factorial(factorial_number):
        store_report('factorial', factorial_number)

        result = math.factorial(float(factorial_number))
        response = {
            'operator': '!',
            'factorial_number': factorial_number,
            'result': float("%.2f" % result)
        }

        return response


def store_report(function_name, first_number, second_number=None):
    from calcu_api.models import Report

    rprt_obj = Report()
    rprt_obj.save(function_name, first_number, second_number)
