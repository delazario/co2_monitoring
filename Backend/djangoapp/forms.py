from django import forms
from djangoapp.models import CO2Measurement

class MeasurementForm(forms.ModelForm):
    class Meta:
        model = CO2Measurement
        fields = '__all__'
        widgets = {
            'co2_level': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'For example: 450 ppm'}),
            'sensor_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Sensor Name...'}),
        }