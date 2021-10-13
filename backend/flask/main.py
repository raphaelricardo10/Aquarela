from flask import Flask
from routes.sales import sales
from routes.errors import errors

app = Flask(__name__)
app.register_blueprint(sales)
app.register_blueprint(errors)