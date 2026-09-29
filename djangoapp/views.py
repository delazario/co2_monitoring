from django.shortcuts import render
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client['co2db']
enterprises_collection = db['enterprises']

def dashboard(request):
    return render(request, 'dashboard.html')

def enterprise_list(request):
    enterprises = list(enterprises_collection.find())
    return render(request, 'enterprises.html', {'enterprises': enterprises})

def mqtt_dashboard(request):
    return render(request, 'mqtt_dashboard.html')

def forecasting(request):
    return render(request, 'forecasting.html')