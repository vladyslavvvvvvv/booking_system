from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import authenticate
from django.contrib.auth import login as dg_login
from django.contrib import messages

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            dg_login(request, user)
            return redirect("apartment-list")
        else: 
            messages.error(request, message="Error, try again later")
    else:
        form = UserCreationForm()
    return render(
        request,
        template_name="auth_system/register.html",
        context = {'form': form},

        )

def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=username, password=password)
            if user is not None: 
                dg_login(request,user)
                return redirect("apartment-list")
            else: 
                messages.error(request, message= "Mistake when trying to log in")
    else: 
        form = AuthenticationForm()
    return render(
        request, 
        template_name="auth_system/login.html",
        context={'form': form},
    )
