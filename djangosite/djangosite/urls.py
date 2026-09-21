from django.contrib import admin
from django.urls import path
from djangoapp.views import MeasurementList

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', MeasurementList.as_view(), name='measurement_list'),
]
