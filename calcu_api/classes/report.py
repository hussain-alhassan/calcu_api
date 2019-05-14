# coding=utf-8
"""
Report class shows the operations that have
been performed during a period of time (daily, weekly, or monthly). Then returns the JSON response.
"""
from calcu_api.models import Report
from datetime import datetime, timedelta
from calcu_api import db


class OperationsReports:

    @staticmethod
    def daily():
        last_24h = datetime.now() - timedelta(days=1)
        reports = Report.query.filter(Report.date > last_24h)

        operation_count = get_operation_count(reports)
        response = prepare_respnse('daily', operation_count)

        return response

    @staticmethod
    def weekly():
        last_week = datetime.now() - timedelta(days=7)
        reports = Report.query.filter(Report.date > last_week)

        operation_count = get_operation_count(reports)
        response = prepare_respnse('weekly', operation_count)

        return response

    @staticmethod
    def monthly():
        last_month = datetime.now() - timedelta(days=30)
        reports = Report.query.filter(Report.date > last_month)

        operation_count = get_operation_count(reports)
        response = prepare_respnse('weekly', operation_count)

        return response


def get_operation_count(reports):
    operation_count = {
        'add_operation_count': 0,
        'subtract_operation_count': 0,
        'multiply_operation_count': 0,
        'divide_operation_count': 0,
        'square_root_operation_count': 0,
        'cube_root_operation_count': 0,
        'power_operation_count': 0,
        'factorial_operation_count': 0,

    }

    for report in reports:
        if report.function == 'add':
            operation_count['add_operation_count'] += 1
        elif report.function == 'subtract':
            operation_count['subtract_operation_count'] += 1
        elif report.function == 'multiply':
            operation_count['multiply_operation_count'] += 1
        elif report.function == 'divide':
            operation_count['divide_operation_count'] += 1
        elif report.function == 'square_root':
            operation_count['square_root_operation_count'] += 1
        elif report.function == 'cube_root':
            operation_count['cube_root_operation_count'] += 1
        elif report.function == 'power':
            operation_count['power_operation_count'] += 1
        elif report.function == 'factorial':
            operation_count['factorial_operation_count'] += 1

    return operation_count


def prepare_respnse(report_period, operation_count):

    response = {
        'report_period': report_period,
        'add_operation_count': operation_count['add_operation_count'],
        'subtract_operation_count': operation_count['subtract_operation_count'],
        'multiply_operation_count': operation_count['multiply_operation_count'],
        'divide_operation_count': operation_count['divide_operation_count'],
        'square_root_operation_count': operation_count['square_root_operation_count'],
        'cube_root_operation_count': operation_count['cube_root_operation_count'],
        'power_operation_count': operation_count['power_operation_count'],
        'factorial_operation_count': operation_count['factorial_operation_count'],
    }

    return response