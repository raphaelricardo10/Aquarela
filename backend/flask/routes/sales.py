from flask.blueprints import Blueprint

sales = Blueprint('sales', __name__)
@sales.route("/sales")
def show():
    return "<p>Hello, World!</p>"