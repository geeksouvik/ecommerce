from django import forms
from django.contrib.auth import get_user_model

User= get_user_model()

class ContactForm(forms.Form):
	name= 	forms.CharField(widget= forms.TextInput(attrs= {"class":"form-control", "placeholder":"name"}))
	email=	forms.EmailField(widget= forms.EmailInput(attrs= {"class":"form-control", "placeholder":"email"}))
	mobile=	forms.DecimalField()
	website=forms.CharField(widget= forms.TextInput(attrs= {"class":"form-control", "placeholder":"website"}))

	def clean_email(self):
		email= self.cleaned_data.get('email')

		if not "gmail.com" in email:
			raise forms.ValidationError("Emails shoul be gmail only")
		return email

class LoginForm(forms.Form):
	username=	forms.CharField(widget= forms.TextInput(attrs= {"class":"form-control", "placeholder":"name"}))
	password=	forms.CharField(widget= forms.PasswordInput(attrs= {"class":"form-control", "placeholder":"password"}))


class RegisterForm(forms.Form):
	username=	forms.CharField(widget= forms.TextInput(attrs= {"class":"form-control", "placeholder":"name"}))
	email=		forms.EmailField(widget= forms.TextInput(attrs= {"class":"form-control", "placeholder":"name"}))
	password=	forms.CharField(widget= forms.PasswordInput(attrs= {"class":"form-control", "placeholder":"password"}))
	password2=	forms.CharField(widget= forms.PasswordInput(attrs= {"class":"form-control", "placeholder":"confirm password"}))

	def clean(self):
		data 		= self.cleaned_data
		password 	= self.cleaned_data.get("password")
		password2 	= self.cleaned_data.get("password2")
		
		if password!=password2:
			raise forms.ValidationError("passwords must be same")
		return data

	def clean_username(self):
		username 	= self.cleaned_data.get("username")
		qs			= User.objects.filter(username=username)
		if qs.exists():
			raise forms.ValidationError("Username already exists")
		return username	

	def clean_email(self):
		email 	= self.cleaned_data.get("email")
		qs 		= User.objects.filter(email=email)
		if qs.exists():
			raise forms.ValidationError("Email already exists")
		return email


