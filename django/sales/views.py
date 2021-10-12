from database.database import Database
from django.shortcuts import render
from django.http import HttpResponse
from bson.json_util import dumps

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class SalesView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        db = Database('sample_supplies')
        print(db)
        response = db.connection.sales.find()
        return HttpResponse(dumps((response)))