from django.db import models
# Create your models here.
class Users(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_fname = models.CharField(max_length=100)
    user_lname = models.CharField(max_length=100)
    user_email = models.EmailField(max_length=100)
    user_password = models.CharField(max_length=100)
    user_address=models.CharField(max_length=100)
    user_vechicle_type = models.CharField(max_length=100)
    user_vechicle_number=models.CharField(max_length=100)
    user_created_date=models.DateTimeField(auto_now_add=True)
    user_modified_date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user_email

class Clients(models.Model):
    client_id = models.AutoField(primary_key=True)
    client_fname = models.CharField(max_length=100)
    client_lname = models.CharField(max_length=100)
    client_email = models.EmailField(max_length=100)
    client_password = models.CharField(max_length=100)
    client_address = models.CharField(max_length=100)
    client_vehicle_capacity = models.IntegerField()
    client_available_vehicle_capacity = models.IntegerField()
    client_parking_Price = models.IntegerField()
    client_latitude = models.FloatField()
    client_longitude = models.FloatField()
    client_landmark = models.CharField(max_length=100)
    client_created_date=models.DateTimeField(auto_now_add=True)
    client_modified_date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.client_email



