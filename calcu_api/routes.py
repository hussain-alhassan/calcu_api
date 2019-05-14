from flask import render_template, jsonify, request
from calcu_api.forms import CalculationForm
from calcu_api import app
from calcu_api.classes.calculation import Calculation
from calcu_api.classes.report import OperationsReports


calc_obj = Calculation()


@app.route('/')
def home():
    form = CalculationForm()
    return render_template('home.html', form=form)


@app.route('/calculate')
def calculate():
    form = CalculationForm()
    return render_template('calculate.html', form=form, title='Calculate')


@app.route('/api/add', methods=['GET'])
def add():
    first_number = request.args.get('first_number')
    second_number = request.args.get('second_number')
    response = calc_obj.add(first_number, second_number)

    return jsonify(response)


@app.route('/api/subtract', methods=['GET'])
def subtract():
    first_number = request.args.get('first_number')
    second_number = request.args.get('second_number')
    response = calc_obj.subtract(first_number, second_number)

    return jsonify(response)


@app.route('/api/multiply', methods=['GET'])
def multiply():
    first_number = request.args.get('first_number')
    second_number = request.args.get('second_number')
    response = calc_obj.multiply(first_number, second_number)

    return jsonify(response)


@app.route('/api/divide', methods=['GET'])
def divide():
    first_number = request.args.get('first_number')
    second_number = request.args.get('second_number')
    response = calc_obj.divide(first_number, second_number)

    return jsonify(response)


@app.route('/api/square-root', methods=['GET'])
def square_root():
    sqrt_number = request.args.get('sqrt_number')
    response = calc_obj.square_root(sqrt_number)

    return jsonify(response)


@app.route('/api/cube-root', methods=['GET'])
def cube_root():
    cube_number = request.args.get('cube_number')
    response = calc_obj.cube_root(cube_number)

    return jsonify(response)


@app.route('/api/power', methods=['GET'])
def power():
    base_number = request.args.get('base_number')
    exponent_number = request.args.get('exponent_number')
    response = calc_obj.power(base_number, exponent_number)

    return jsonify(response)


@app.route('/api/factorial', methods=['GET'])
def factorial():
    factorial_number = request.args.get('factorial_number')
    response = calc_obj.factorial(factorial_number)

    return jsonify(response)


# Reports section
@app.route('/api/report/daily', methods=['GET'])
def daily():
    report_obj = OperationsReports()

    response = report_obj.daily()

    return jsonify(response)


@app.route('/api/report/weekly', methods=['GET'])
def weekly():
    report_obj = OperationsReports()

    response = report_obj.weekly()

    return jsonify(response)


@app.route('/api/report/monthly', methods=['GET'])
def monthly():
    report_obj = OperationsReports()

    response = report_obj.monthly()

    return jsonify(response)
