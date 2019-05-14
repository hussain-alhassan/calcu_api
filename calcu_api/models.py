from datetime import datetime
from calcu_api import db


class Report(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    function = db.Column(db.String(20), nullable=False)
    first_number = db.Column(db.Integer, nullable=False)
    second_number = db.Column(db.Integer)
    api_type = db.Column(db.String(20 ), nullable=False)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    @staticmethod
    def save(function_name, first_number, second_number):
        operation_record = Report(function=function_name, first_number=first_number, second_number=second_number,
                                  api_type='web', date=datetime.now())

        db.session.add(operation_record)
        db.session.commit()
