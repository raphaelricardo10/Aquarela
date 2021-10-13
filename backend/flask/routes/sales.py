from flask.blueprints import Blueprint
from flask import request, Response
from bson.json_util import dumps, loads
from src.database import Database
from bson.objectid import ObjectId
from datetime import datetime
from werkzeug.exceptions import HTTPException

sales = Blueprint('sales', __name__)

@sales.route("/sales", methods=['POST'])
def post():

    db = Database('sample_supplies')

    if request.json is None or request.json == {}:
        return Response(dumps(db.connection.sales.find()))

    if request.json['type'] == 'query':
        return query(db, request.json)
    else:
        #Other types not implemented
        raise ValueError("ERROR: Unsupported request type")

def query(db, request):

    try:
        data = request['data']

        if 'saleDate' in data:
            date = datetime.strptime(data['saleDate'], '%Y-%m-%d')
            data['saleDate'] = {
                "$gte": datetime(date.year, date.month, date.day, 0, 0, 0),
                "$lt": datetime(date.year, date.month, date.day, 23, 59, 59)
            }

        if '_id' in data:
            data['_id'] = ObjectId(data['_id'])

        for param in request['params']:
            if param == 'limit':
                request['params']['limit'] = int(request['params']['limit'])
            else:
                raise ValueError("ERROR: Unsupported parameter")

        if 'limit' not in request['params']:
            request['params']['limit'] = 0

        response = dumps(db.connection.sales.find(data).limit(request['params']['limit']))

        if response == '[]':
            raise StopIteration

        return Response(response, status=200)

    except KeyError as e:
        raise KeyError(f"Unsupported key in JSON input")

    except Exception as e:
        raise
