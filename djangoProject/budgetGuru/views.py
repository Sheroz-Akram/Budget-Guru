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

    # Check if User is already Login or Not
    if request.session.get('loginStatus', False) == True:
        return HttpResponseRedirect('/Dashboard')

    try:
        # Get the Information of the User
        login_email_address = request.POST['loginEmail']
        login_password = request.POST['loginPassword']

        try:

            # Create a unique private key
            privatekey = generateRandomeString(100)

            # Check if the user already exists or not
            user = AppUser.objects.get(
                email_address=login_email_address,
            )

            # Check if Entered Password is correct or not
            if user.password != login_password:
                return render(request=request, template_name="Account.html", context={
                    "status": "error",
                    "message":"Entered password is not correct."
                })

            # Store the Private Key to the User Account
            user.private_key = privatekey
            user.save()

            # Store the User Data into New Session
            request.session['loginStatus'] = True
            request.session['emailAddress'] = login_email_address
            request.session['privateKey'] = privatekey

            # Return the User to the Dashboard Page
            return HttpResponseRedirect('/Dashboard')

        # User of the application does not found
        except Exception as e:
            return render(request=request, template_name="Account.html", context={
                "status": "error",
                "message":"User does not found. Please enter correct details."
            })

    # An Error in the Request
    except Exception as e:
        return render(request=request, template_name="Account.html", context={
                "status": "error",
                "message":"An invalid request by the user"
            })

# Dashboard Page that is Shown to the User
def DashboardPage(request):
    return render(request=request, template_name="Dashboard.html")

# Page to Adjust Acccount Settings
def ProfileSettings(request):
    return render(request=request, template_name="ProfileSettings.html")