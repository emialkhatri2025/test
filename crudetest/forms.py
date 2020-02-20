from django import forms
from crudetest.models import HR

class HRForm(forms.ModelForm):
    class Meta:
        model = HR
        fields = ['empid','name','age']
