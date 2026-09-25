from django.contrib import admin
from django.urls import path
from djangoapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.dashboard, name='dashboard'),
    path('enterprises/', views.enterprise_list, name='enterprises'),
    path('mqtt/', views.mqtt_dashboard, name='mqtt'),
    path('forecasting/', views.forecasting, name='forecasting'),
]