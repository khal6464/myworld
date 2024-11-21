from django import forms
from django.contrib.auth.models import User



class SignupForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
    password = forms.CharField(widget=forms.PasswordInput)
from .models import Equipment

class EquipmentForm(forms.ModelForm):
    class Meta:
        model = Equipment
        fields = ['name', 'category', 'price', 'condition', 'description', 'image','phone','address','pincode']