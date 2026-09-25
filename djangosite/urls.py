from django.contrib import admin
from django.urls import path
from djangoapp.views import MeasurementList, MeasurementCreate

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', MeasurementList.as_view(), name='measurement_list'),
    path('create/', MeasurementCreate.as_view(), name='create_measurement'),
]