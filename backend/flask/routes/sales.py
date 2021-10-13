from flask.blueprints import Blueprint
from flask import request, Response
from bson.json_util import dumps, loads
from src.database import Database
from bson.objectid import ObjectId
from datetime import datetime

sales = Blueprint('sales', __name__)
@sales.route("/sales", methods=['POST'])
def get():
    if request.method == 'POST':
        r = request.json

        try:
            db = Database('sample_supplies')
        except Exception:
            return Response({"Error": "Failed in connecting to the database. Try again later"}, status=500)

        try:
            if r is None:
                r = {}

            if not 'data' in r:
                r['data'] = {}


            data = r['data']

            if 'saleDate' in data:
                date = datetime.strptime(data['saleDate'], '%Y-%m-%d')
                data['saleDate'] = {
                        "$gte": datetime(date.year, date.month, date.day, 0, 0, 0),
                        "$lt": datetime(date.year, date.month, date.day, 23, 59, 59)
                    }

            if '_id' in data:
                data['_id'] = ObjectId(data['_id'])

            if 'params' in r:
                if 'limit' not in r['params']:
                    r['params']['limit'] = 0
            else:
                r['params'] = {}
                r['params']['limit'] = 0

        except Exception as e:
            return Response(e, status=400)

        try:
            response = dumps(db.connection.sales.find(data).limit(r['params']['limit']))

            if response == '[]':
                raise StopIteration

            return Response(response, status=200)

        except StopIteration:
            return Response({"Warning": "The requested document was not found in database"}, status=204)