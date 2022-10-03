from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from .forms import NewUserForm



def homepage(request):
  return render(request, "home.html")

def register(request):
  if request.method == "POST":
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      username = form.cleaned_data.get('username')
      messages.success(request, f"New account created: {username}")
      login(request, user, backend='django.contrib.auth.backends.ModelBackend')
    else:
      messages.error(request,"Account creation failed")

    return redirect("main:homepage")

  form = UserCreationForm()
  return render(request,"register.html", {"form": form})

def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("main:homepage")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="register.html", context={"register_form":form})




