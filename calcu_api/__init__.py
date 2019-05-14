from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'  # might use later

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///calcu_api_DB.db'
db = SQLAlchemy(app)

from calcu_api import routes
from calcu_api.models import Report