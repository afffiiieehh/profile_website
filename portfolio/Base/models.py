from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=40)
    contant=models.TextField(max_length=500)
    number=models.CharField(max_length=13)
