from django import forms 
from .models import Person, under_person

class variety_info(forms.ModelForm):
    class Meta:
        fields = ("title", "particular", "lf", "price", "quantity", "total")
        model = under_person

class Personregisterform(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        fields = ("first_name","email","password")
        model = Person

class Personloginform(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        fields = ("email","password")
        model = Person