from django.db import models
from django.contrib.auth.models import User

class Brand(models.Model):
    company = models.CharField(max_length=50, primary_key=True)

    def __str__(self):
        return self.company
    

class Bike(models.Model):
    company = models.ForeignKey(Brand, on_delete=models.CASCADE)
    bike_name = models.CharField(max_length=50)
    desc = models.CharField(max_length=300)
    photo = models.ImageField(upload_to='bike_photos')

    def __str__(self):
        return self.bike_name


class Booking(models.Model):
    booking_id = models.IntegerField(primary_key=True)
    bike_name = models.ForeignKey(Bike, on_delete=models.CASCADE)
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    pickup_date = models.DateField(auto_now=False, auto_now_add=False)
    pickup_time = models.TimeField(auto_now=False, auto_now_add=False)
    drop_date = models.DateField(auto_now=False, auto_now_add=False)
    drop_time = models.TimeField(auto_now=False, auto_now_add=False)