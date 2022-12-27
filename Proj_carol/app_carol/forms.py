from django import forms 
from .models import Person,under_person

class variety_info(forms.Modelform):
    class Meta:
        fields=("title","particular","lf","quantity","price","total")
        model = under_person
class Personregisterform(forms.Modelform):
    password =forms.CharField(widget=forms.PasswordInput)
    class Meta:
        fields=("Email","Password")
        model = Person
class Personloginform(forms.Modelform):
    password =forms.CharField(widget=forms.PasswordInput)
    class Meta:
        fields=("full_name","contact","Email","Password",)
        model = Person