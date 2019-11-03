from django import forms
from app2.models import formpage

class signupform(forms.ModelForm):
    class Meta():
        model = formpage
        fields = '__all__'
