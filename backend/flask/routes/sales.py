from flask.blueprints import Blueprint
from flask import request, Response
from bson.json_util import dumps, loads
from src.database import Database
from bson.objectid import ObjectId
from datetime import datetime

sales = Blueprint('sales', __name__)


@sales.route("/sales", methods=['POST'])
def post():

    try:
        db = Database('sample_supplies')
    except Exception:
        return Response({"Error": "Failed in connecting to the database. Try again later"}, status=500)

    if request.json is None:
        ret = Response(dumps(db.connection.sales.find()))
    
    elif 'type' not in request.json:
        ret = Response({}, status=400)

    elif request.json['type'] == 'query':
        ret = query(db, request.json)

    else:
        #Other types not implemented
        ret = Response({}, status=400)

    return ret

def query(db, request):

    try:
        if request is None:
            request = {}

        if not 'data' in request:
            request['data'] = {}

        data = request['data']

        if 'saleDate' in data:
            date = datetime.strptime(data['saleDate'], '%Y-%m-%d')
            data['saleDate'] = {
                "$gte": datetime(date.year, date.month, date.day, 0, 0, 0),
                "$lt": datetime(date.year, date.month, date.day, 23, 59, 59)
            }

        if '_id' in data:
            data['_id'] = ObjectId(data['_id'])

        if 'params' in request:
            if 'limit' not in request['params']:
                request['params']['limit'] = 0
        else:
            request['params'] = {}
            request['params']['limit'] = 0

    except Exception as e:
        return Response(e, status=400)

    try:
        response = dumps(db.connection.sales.find(data).limit(request['params']['limit']))

        if response == '[]':
            raise StopIteration

        return Response(response, status=200)

    except StopIteration:
        return Response({"Warning": "The requested document was not found in database"}, status=204)
