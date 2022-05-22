
# Create your models here.
from django.db import models

# Create your models here.

# this is to get the information from the users and their exprience about this platform

class Feedback(models.Model) :
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    subject = models.CharField(max_length=200)
    message = models.CharField(max_length=200)
    def _str_(self):
        return self.name

class Donate(models.Model) :
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    organization = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    phonenumber = models.CharField(max_length=100)
    address1 = models.CharField(max_length=254)
    address2 = models.CharField(max_length=254)
    city=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    amount = models.IntegerField()
    comments = models.CharField(max_length=500)
    def __str__(self):
        return self.fname

class Total_Donate(models.Model):
    amount=models.IntegerField(default=0)
    def __str__(self):
        return self.name

class Fund(models.Model) :
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    address = models.CharField(max_length=254)
    phn = models.CharField(max_length=100)
    pro = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state  = models.CharField(max_length=100)
    zp = models.CharField(max_length=100)
    def __str__(self):
            return self.name


class Don(models.Model) :
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    address = models.CharField(max_length=254)
    phn = models.CharField(max_length=100)
    pro = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state  = models.CharField(max_length=100)
    zp = models.CharField(max_length=100)
    def __str__(self):
            return self.name
