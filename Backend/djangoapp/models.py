from django.db import models

class CO2Measurement(models.Model):
    sensor_name = models.CharField(max_length=100)
    co2_level = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.sensor_name} - {self.co2_level} ppm"
