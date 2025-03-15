from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib import messages

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("index")
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
    if request.method == "GET":
        form = AuthenticationForm(request, data=request.GET)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=username, password=password)
            if user is not None: 
                login(request,user)
                return redirect("index")
            else: 
                messages.error(request, message= "Mistake when trying to log in")
    else: 
        form = AuthenticationForm()
    return render(
        request, 
        template_name="auth_system/login.html",
        context={'form': form},
    )
