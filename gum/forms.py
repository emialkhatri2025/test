from django import forms
from gum.models import movies

class movie_forms(forms.ModelForm):
    class Meta:
        model = movies
        fields = ['movie_name','movie_actor','movies_actress','movie_released']
