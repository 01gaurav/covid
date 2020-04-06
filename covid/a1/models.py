from django.db import models

class shpkprSU(models.Model):
    first_name=models.CharField(max_length=200)
    last_name=models.CharField(max_length=200)
    email=models.EmailField(max_length=200,unique=True)
    location=models.CharField(max_length=400)
    mobile_no=models.IntegerField(max_length=10)
