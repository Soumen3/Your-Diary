from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User

class CustomUserCreationForm(UserCreationForm):
	date_of_birth = forms.DateField(widget=forms.DateInput(attrs={'type': 'date', 'range': '1900-01-01, 2021-12-31'}))
	class Meta:
		model = User
		fields = ('email', 'first_name', 'last_name', 'date_of_birth')

class CustomUserChangeForm(UserChangeForm):
	date_of_birth = forms.DateField(widget=forms.DateInput(attrs={'type': 'date', 'range': '1900-01-01, 2021-12-31'}))
	class Meta:
		model = User
		fields = ('email', 'first_name', 'last_name', 'date_of_birth')

class LoginForm(forms.Form):
	email = forms.EmailField()
	password = forms.CharField(widget=forms.PasswordInput)