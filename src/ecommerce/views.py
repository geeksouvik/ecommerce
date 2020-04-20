from django.contrib.auth import authenticate, login, get_user_model
#from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import ContactForm,LoginForm, RegisterForm
from products.models import Product

def home_page(request):
	queryset	= Product.objects.all()
	context={
		"title": "This is just a random page",
		'object_list': queryset
	}
	return render(request,"home.html", context)

def about_page(request):
	return render(request,"about.html", {})

def contact_page(request):
	contact_form= ContactForm(request.POST or None)
	context={
		"form": contact_form
	}
	if contact_form.is_valid():
		print(contact_form.cleaned_data)

#	if request.method=="POST":
#		print(request.POST.get('name'))
#		print(request.POST.get('email'))
#		print(request.POST.get('mobile'))

	return render(request,"contact/view.html", context)


def login_page(request):
	login_form= LoginForm(request.POST or None)
	print(request.user.is_authenticated)
	context={
		"form": login_form
	}
	if login_form.is_valid():
			print(login_form.cleaned_data)
			context['form']= LoginForm()
			username= login_form.cleaned_data.get("username")
			password= login_form.cleaned_data.get("password")
			print(request.user.is_authenticated)
			user = authenticate(request, username=username, password=password)
			print(user)
			if user is not None:
				print(request.user.is_authenticated)
				login(request, user)
		      	#context['form']= LoginForm()
				return redirect("/home")
			else:
				print("Error")

	return render(request,"auth/login.html", context)

User= get_user_model()
		
def register_page(request):
	register_form= RegisterForm(request.POST or None)
	context={
		"form": register_form
	}
	if register_form.is_valid():
		print(register_form.cleaned_data)
		username	= register_form.cleaned_data.get("username")
		email		= register_form.cleaned_data.get("email")
		password	= register_form.cleaned_data.get("password")
		new_user	= User.objects.create_user(username,email,password)
		print(new_user)

	return render(request,"auth/register.html",context)