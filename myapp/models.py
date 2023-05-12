from django.db import models

# Create your models here.
class User(models.Model):
    f_name = models.CharField(max_length=50)
    l_name = models.CharField(max_length=50)
    email_id = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=200)
    created_date = models.DateTimeField(auto_now_add=True)