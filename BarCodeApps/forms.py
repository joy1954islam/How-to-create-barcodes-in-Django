
from django import forms
from BarCodeApps.models import BarCode


class BarCodeForm(forms.ModelForm):
    class Meta:
        model = BarCode
        fields = ['SiteName','country_id','manufacturer_id','SiteName_id']
