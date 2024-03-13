from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, JsonResponse
from django.core import serializers
import json
from bson.json_util import dumps
from django.middleware.csrf import get_token


import pymongo

client = pymongo.MongoClient('mongodb+srv://admin:admin@cluster-for-learning.seyjy8r.mongodb.net/')

dbname = client['meteorite_landings_db']

collection = dbname['meteorite_landings']

def index(request):
    return HttpResponse("<h1>Hello and welcome to my first <u>Django App</u> project!</h1>")

'''

meteorite_1 = {
    "name": "Apophis",
    "year": "2029"
}
collection.insert_one(meteorite_1)

meteorite_details = collection.find({})

for i in meteorite_details:
    print(str(i['name']))

'''

def TheModelView(request):
    if (request.method == "GET"):
        
        cursor = collection.find().limit(10)
        json_data = dumps(cursor)
        print("nJsON data:", json_data)
        return JsonResponse(json_data, safe=False)
    
    if (request.method == "POST"):
        body = json.loads(request.body.decode("utf-8"))
        newrecord = {
            "name": body['name'],
            "year": body['year']
        }
        result = collection.insert_one(newrecord)
        data = {
            "inserted_id": result.inserted_id
        }
        json_data = dumps(result.inserted_id)
        return JsonResponse(json_data, safe=False)

def get_csrf_token(request):
    csrf_token = get_token(request)
    return JsonResponse({'csrf_token': csrf_token})