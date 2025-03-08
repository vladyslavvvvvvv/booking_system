from django.urls import path
from .views import apartment_list, create_apartment
urlpatterns = [
    path("apartment/list/", apartment_list, name="apartment-list"),
    path("apartment/create/", create_apartment, name="create-apartment" )
]