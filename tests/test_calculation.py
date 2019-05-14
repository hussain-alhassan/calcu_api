from unittest import TestCase

from calcu_api.classes.calculation import Calculation

calc_obj = Calculation()


class TestCalculation(TestCase):

    def test_add(self):
        self.assertEqual(calc_obj.add(1, 2)["result"], 3)
        self.assertEqual(calc_obj.add(-1, 1)["result"], 0)
        self.assertEqual(calc_obj.add(-1, -50)["result"], -51)
        self.assertEqual(calc_obj.add(0, -100000)["result"], -100000)

        # if entries != numbers
        self.assertEqual(calc_obj.add('a', 5)["error"], "Something went wrong!")
        self.assertEqual(calc_obj.add(3, 'b')["error"], "Something went wrong!")
        self.assertEqual(calc_obj.add('x', 'y')["error"], "Something went wrong!")

    def test_subtract(self):
        self.assertEqual(calc_obj.subtract(10, 5)["result"], 5)
        self.assertEqual(calc_obj.subtract(-1, 1)["result"], -2)
        self.assertEqual(calc_obj.subtract(-1, -50)["result"], 49)
        self.assertEqual(calc_obj.subtract(0, -100000)["result"], 100000)

        # if entries != numbers
        self.assertEqual(calc_obj.subtract('a', 5)["error"], "Something went wrong!")
        self.assertEqual(calc_obj.subtract(3, 'b')["error"], "Something went wrong!")
        self.assertEqual(calc_obj.subtract('x', 'y')["error"], "Something went wrong!")

    def test_multiply(self):
        self.assertEqual(calc_obj.multiply(1, 2)["result"], 2)
        self.assertEqual(calc_obj.multiply(-1, 1)["result"], -1)
        self.assertEqual(calc_obj.multiply(-1, -50)["result"], 50)
        self.assertEqual(calc_obj.multiply(0, -100000)["result"], 0)

        # if entries != numbers
        self.assertEqual(calc_obj.multiply('a', 5)["error"], "Something went wrong!")
        self.assertEqual(calc_obj.multiply(3, 'b')["error"], "Something went wrong!")
        self.assertEqual(calc_obj.multiply('x', 'y')["error"], "Something went wrong!")

    def test_divide(self):
        self.assertEqual(calc_obj.divide(9, 2)["result"], 4.5)
        self.assertEqual(calc_obj.divide(-1, 1)["result"], -1)
        self.assertEqual(calc_obj.divide(-1, -50)["result"], 0.02)
        self.assertEqual(calc_obj.divide(0, -100000)["result"], 0)

        # if entries != numbers
        self.assertEqual(calc_obj.divide('a', 5)["error"], "Something went wrong!")
        self.assertEqual(calc_obj.divide(3, 'b')["error"], "Something went wrong!")
        self.assertEqual(calc_obj.divide('x', 'y')["error"], "Something went wrong!")

        # # if dividing by zero
        # with self.assertRaises(ZeroDivisionError):
        #     calc_obj.divide(10, 0)
        self.assertEqual(calc_obj.divide(10, 0)["error"], "Divide can not divide by zero!")

    def test_square_root(self):
        self.assertEqual(calc_obj.square_root(16)["result"], 4)
        self.assertEqual(calc_obj.square_root(29)["result"], 5.39)

        self.assertEqual(calc_obj.square_root('fun')["error"], 'Something went wrong!')

    def test_cube_root(self):
        self.assertEqual(calc_obj.cube_root(27)["result"], 3)
        self.assertEqual(calc_obj.cube_root(16)["result"], 2.52)

        self.assertEqual(calc_obj.cube_root('fun')["error"], 'Something went wrong!')

    def test_power(self):
        self.assertEqual(calc_obj.power(1, 2)["result"], 1)
        self.assertEqual(calc_obj.power(5, 3)["result"], 125)
        self.assertEqual(calc_obj.power(-5, 3)["result"], -125)
        self.assertEqual(calc_obj.power(-36, -2)["result"], 0)

        # if entries != numbers
        self.assertEqual(calc_obj.power('a', 5)["error"], "Something went wrong!")
        self.assertEqual(calc_obj.power(3, 'b')["error"], "Something went wrong!")
        self.assertEqual(calc_obj.power('x', 'y')["error"], "Something went wrong!")

    def test_factorial(self):
        self.assertEqual(calc_obj.factorial(3)["result"], 6)
        self.assertEqual(calc_obj.factorial(9)["result"], 362880)

        self.assertEqual(calc_obj.factorial('fun')["error"], 'Something went wrong!')
        self.assertEqual(calc_obj.factorial(-9)["error"], 'Something went wrong!')
