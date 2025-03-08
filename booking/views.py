from django.shortcuts import redirect, render
from django.urls import reverse
from .models import Apartment
from django.http import HttpResponse, HttpRequest

def apartment_list(request: HttpRequest):
    apartments_list = Apartment.objects.all()
    context = {
        "apartments_list": apartments_list
    }
    return render(request, "booking/apartment_list.html", context= context)

def create_apartment(request: HttpRequest):
    if request.method == "GET":
        return render(request, "booking/create_apartment.html")
    if request.method == "POST":
        apartment_location = request.POST.get("location")
        apartment_price = request.POST.get("price")
        apartment_available = request.POST.get("available", False)

        return redirect(reverse("apartments-list"))
