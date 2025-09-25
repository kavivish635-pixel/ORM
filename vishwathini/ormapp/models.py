from django.db import models
from django.contrib import admin

class Car(models.Model):
    car_id = models.CharField(max_length=20, help_text="Car ID")
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    price = models.IntegerField()
    year = models.IntegerField()
    owner_email = models.EmailField()

class CarAdmin(admin.ModelAdmin):
    list_display = ('car_id', 'brand', 'model', 'price', 'year', 'owner_email')
