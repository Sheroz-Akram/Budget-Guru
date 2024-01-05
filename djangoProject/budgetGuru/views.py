from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect

# Main Page
def MainPage(request):
    return HttpResponseRedirect("/Home")

# Home Page
def HomePage(request):
    return render(request=request, template_name="Home.html")

# Account Page (Login/Registration)
def AccountPage(request):
    return render(request=request, template_name="Account.html")

# Registration API (registor a new User in the database)
def registrationAPI(request):
    return HttpResponse("Got a Request. Okay")

# Login API (login a already registored user from the database)
def loginAPI(request):
    return HttpResponse("Got a Request. Okay")