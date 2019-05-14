import click
from classes.calculation import Calculation

import sys
import os
sys.path.append(os.path.abspath(".."))


@click.command()
@click.option('--function_name', '-function', help='Name of the function to be called', required=True)
@click.option('--first_number', '-first', type=float, help='First or the number will be calculated', required=True)
@click.option('--second_number', '-second', type=float, help='Second number will be calculated')
def main(function_name, first_number, second_number):
    calc_obj = Calculation()


    # call the right function and pass the parameters from the command
    if function_name == 'add':
        response = calc_obj.add(first_number, second_number)
        print(response)
    elif function_name == 'subtract':
        response = calc_obj.subtract(first_number, second_number)
        print(response)
    elif function_name == 'multiply':
        response = calc_obj.multiply(first_number, second_number)
        print(response)
    elif function_name == 'divide':
        response = calc_obj.divide(first_number, second_number)
        print(response)
    elif function_name == 'square_root':
        response = calc_obj.square_root(first_number)
        print(response)
    elif function_name == 'cube_root':
        response = calc_obj.cube_root(first_number)
        print(response)
    elif function_name == 'power':
        response = calc_obj.power(first_number, second_number)
        print(response)
    elif function_name == 'factorial':
        response = calc_obj.factorial(first_number)
        print(response)


if __name__ == '__main__':
    main()
