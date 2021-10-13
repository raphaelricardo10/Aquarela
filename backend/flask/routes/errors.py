from flask.blueprints import Blueprint
from flask import Response
from werkzeug.exceptions import HTTPException
from flask import json

errors = Blueprint('errors', __name__)

@errors.app_errorhandler(Exception)
def handle_exception(e):
    # pass through HTTP errors
    if isinstance(e, HTTPException):
        return e

    return Response("Internal server error!!! Try again later.", status=500)

@errors.app_errorhandler(ValueError)
@errors.app_errorhandler(KeyError)
def handle_input_error(e):
    return str(e), 400

@errors.app_errorhandler(ConnectionError)
def handle_conn_error(e):
    return Response(str(e), status=500)

@errors.app_errorhandler(StopIteration)
def handle_empty_warning(e):
    return Response(str(e), status=204)

