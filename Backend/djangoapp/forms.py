from django import forms
from djangoapp.models import CO2Measurement

class MeasurementForm(forms.ModelForm):
    class Meta:
        model = CO2Measurement
        fields = '__all__'