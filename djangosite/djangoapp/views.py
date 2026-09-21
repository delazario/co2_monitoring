import os
from django.views import generic
from django.conf import settings
from djangoapp.models import CO2Measurement

class MeasurementList(generic.ListView):
    model = CO2Measurement
    context_object_name = 'measurements'
    template_name = 'measurement_list.html'

    def get(self, request, *args, **kwargs):
        try:
            file_path = os.path.join(settings.BASE_DIR, 'test_data')
            with open(file_path, 'r') as measurement_file:
                for value in measurement_file:
                    co2_val = float(value.strip())
                    CO2Measurement.objects.get_or_create(
                        sensor_name="Test-Sensor",
                        co2_level=co2_val
                    )
        except (IOError, ValueError):
            pass
        return super(MeasurementList, self).get(request, *args, **kwargs)
