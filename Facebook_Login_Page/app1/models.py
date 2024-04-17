from django.db import models

# Create your models here.

class Login_Details(models.Model):
    email=models.CharField(max_length=50)
    password=models.CharField(max_length=100)
    
    def __str__(self):
        return self.email