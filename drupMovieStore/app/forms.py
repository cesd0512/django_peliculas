from django import forms
from app.models import Movie


class FormMovie(forms.ModelForm):  
    class Meta:  
        model = Movie  
        fields = "__all__"
        
    