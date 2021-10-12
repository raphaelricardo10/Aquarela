from flask import Flask
from routes.sales import sales

app = Flask(__name__)
app.register_blueprint(sales)