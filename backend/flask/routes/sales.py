from flask.blueprints import Blueprint
from flask import request, Response
from bson.json_util import dumps, loads
from src.database import Database
from bson.objectid import ObjectId
from datetime import datetime

sales = Blueprint('sales', __name__)

@sales.route("/sales", methods=['POST'])
def post():

    #initialize and connect to database
    db = Database('sample_supplies')

    #The default response is to query all documents
    if request.json is None or request.json == {}:
        return Response(dumps(db.connection.sales.find()))

    #Handle each operation in database (CRUD)
    if request.json['type'] == 'query':
        return query(db, request.json)
    else:
        #Other types not implemented
        raise ValueError("ERROR: Unsupported request type")

def query(db: Database, request: request) -> Response:

    try:
        data = request['data']

        #Convert the query from a date string format to datetime
        if 'saleDate' in data:
            date = datetime.strptime(data['saleDate'], '%Y-%m-%d')
            data['saleDate'] = {
                "$gte": datetime(date.year, date.month, date.day, 0, 0, 0),
                "$lt": datetime(date.year, date.month, date.day, 23, 59, 59)
            }

        #Convert id string to ObjectId
        if '_id' in data:
            data['_id'] = ObjectId(data['_id'])

        #Handle each parameter sent by the client
        for param in request['params']:
            #Define the limit of documents to query
            if param == 'limit':
                request['params']['limit'] = int(request['params']['limit'])

            #Do not accept a unrecognized parameter
            else:
                raise ValueError("ERROR: Unsupported parameter")

        #If there is no limit, query all documents
        if 'limit' not in request['params']:
            request['params']['limit'] = 0

        #Execute query
        response = dumps(db.connection.sales.find(data).limit(request['params']['limit']))

        #Raise a warning if nothing was found
        if response == '[]':
            raise StopIteration

        #Return response with ok status
        return Response(response, status=200)

    except KeyError as e:
        raise KeyError("Unsupported key in JSON input")

    except Exception as e:
        raise
