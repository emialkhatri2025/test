from django import forms
from first.models import Books
from first.models import test

class BookCreate(forms.ModelForm):
    class Meta:
        model = Books
        fields = "__all__"

class TestForm(forms.ModelForm):
    class Meta:
        model = test
        fields = ['name']
