# Import Libraries for Routing
from django.urls import path
from . import views

# Routing Links to View
urlpatterns = [
    path('', view=views.MainPage, name="Main Page"),
    path('Home', view=views.HomePage, name="Home Page"),
    path("Account", view=views.AccountPage, name="Account Page"),
    path("Registor", view=views.registrationAPI, name="Registor User"),
    path("Login", view=views.loginAPI, name="Login User"),
    path("Dashboard", view=views.DashboardPage, name="Dashboard Page"),
    path("ProfileSettings", view=views.ProfileSettings, name="Profile Settings")
]
