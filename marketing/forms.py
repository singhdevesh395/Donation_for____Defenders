from django import forms
from.models import Signup

class EmailSignupForm(forms.ModelForm):
    email=forms.EmailField(widget=forms.TextInput(attrs={
    "type":"email",
    "class":"form-control text1" ,
    "placeholder":"Your E-mail here",
    "name":"email" }),label="")
    class Meta:
        model=Signup
        fields=('email',)
