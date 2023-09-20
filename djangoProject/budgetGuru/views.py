from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect

# Main Page
def MainPage(request):
    return HttpResponseRedirect("/Home")

# Home Page
def HomePage(request):
    return render(request=request, template_name="Home.html")
