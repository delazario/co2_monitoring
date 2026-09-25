from django.shortcuts import render

def dashboard(request):
    return render(request, 'dashboard.html')

def enterprise_list(request):
    return render(request, 'enterprises.html')

def mqtt_dashboard(request):
    return render(request, 'mqtt_dashboard.html')

def forecasting(request):
    return render(request, 'forecasting.html')