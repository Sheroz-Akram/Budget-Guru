from django.db import models

# Create your models here.
class AppUser(models.Model):
    private_key = models.CharField(max_length=100)
    email_address = models.EmailField(max_length=254, unique=True)
    password = models.CharField(max_length=50)