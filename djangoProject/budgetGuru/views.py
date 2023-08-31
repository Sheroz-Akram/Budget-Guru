from django.shortcuts import render
from django.http import HttpResponse

# Home Page
def HomePage(request):
    return render(request=request, template_name="Home.html")
