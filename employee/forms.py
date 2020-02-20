from django import forms
from employee.models import Demployee

class employee_forms(forms.ModelForm):
    class Meta:
        model = Demployee
        fields = ['name','department','role','salary']
