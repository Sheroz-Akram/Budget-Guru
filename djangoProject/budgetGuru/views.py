from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import *
from .Modules.helper import *

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

    
    try:
        # Get the Information of the User
        signup_email_address = request.POST['email']
        signup_password = request.POST['password']

        try:

            # Create a unique private key
            privatekey = generateRandomeString(100)

            # Check if the user already exists or not
            newUser = AppUser(
                private_key=privatekey,
                email_address=signup_email_address,
                password=signup_password,
            )

            # Store the Newly created User
            newUser.save()

            # Return the User to the Registration Page
            return render(request=request, template_name="Account.html", context={
                "status": "success",
                "message":"Account is create successfully"
            })

        # User Already exists with same email address
        except Exception as e:
            return render(request=request, template_name="Account.html", context={
                "status": "error",
                "message":"Account with same email address already exists"
            })

    # An Error in the Request
    except Exception as e:
        return render(request=request, template_name="Account.html", context={
                "status": "error",
                "message":"An invalid request by the user"
            })

# Login API (login a already registored user from the database)
def loginAPI(request):
    return HttpResponse("Got a Request. Okay")

# Dashboard Page that is Shown to the User
def DashboardPage(request):
    return render(request=request, template_name="Dashboard.html")

# Page to Adjust Acccount Settings
def ProfileSettings(request):
    return render(request=request, template_name="ProfileSettings.html")