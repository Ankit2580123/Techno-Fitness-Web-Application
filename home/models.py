from django.db import models
from datetime import datetime  
# from phonenumber_fields.formfields import PhoneNumberField

# Create your models here.

class Enquiry(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=60)
    phone_no=models.CharField(max_length=12)
    message=models.TextField(max_length=200)
    date = models.DateTimeField(auto_now_add=True, blank=True)

    class meta:
        ordering=['name']
        verbose_name="Enquiries"

class Plans(models.Model):
    plan_name=models.CharField(max_length=30)

    def __str__(self) -> str:
        return self.plan_name
    


class HeroBanner(models.Model):
    photo=models.ImageField(upload_to='hero_images')

class Programs(models.Model):
    photo=models.ImageField(upload_to="images")
    men_or_women=models.CharField(max_length=30)
    training_type=models.CharField(max_length=30)

    def __str__(self) -> str:
        return f'{self.men_or_women} {self.training_type}'

class Gallery(models.Model):
    photo=models.ImageField(upload_to='gallery')

class Reviews(models.Model):
    name=models.CharField(max_length=25)
    stars=models.IntegerField(default=1)
    message=models.TextField(max_length=100, default="NA")
    date=models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f'{self.name} {self.stars}'


class OnlineBookings(models.Model):
    name=models.CharField(max_length=50)
    age=models.IntegerField(default=18)
    phone_no=models.CharField(max_length=12)
    email=models.EmailField(max_length=254)
    plan=models.CharField(max_length=100)
    date=models.DateTimeField(auto_now_add=True)
    

    def __str__(self) -> str:
        return f'{self.name} {self.phone_no} {self.email}'
    

class TotalMember(models.Model):
    name=models.CharField(max_length=50)
    fathers_name=models.CharField(max_length=50)
    phone_no=models.CharField(max_length=12)
    age=models.IntegerField(default=18)
    plan=models.CharField(max_length=100)
    address=models.TextField(max_length=300)
    date_of_admissions=models.DateField(null=True, blank=True)

    def __str__(self) -> str:
      
      return f'{self.name} {self.phone_no} {self.age} {self.plan} {self.address} {self.date_of_admissions}'
    
    class meta:
        ordering=['name']
        verbose_name="Total Members"


class Equipments(models.Model):
    name = models.CharField(max_length=150, null=True)
    price = models.CharField(max_length=100, null=True)
    unit = models.CharField(max_length=50, null=True)
    purchase_date = models.DateField(null=True)
    description = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name