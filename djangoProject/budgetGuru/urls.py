# Import Libraries for Routing
from django.urls import path
from . import views

# Routing Links to View
urlpatterns = [
    path('', view=views.MainPage, name="Main Page"),
    path('Home', view=views.HomePage, name="Home Page"),
]
