from django.db import models

# Create your models here.
class People(models.Model):
    name = models.CharField(max_length = 200)
    surname = models.CharField(max_length = 200)
    email = models.CharField(max_length = 200)
    telephone = models.IntegerField()

    class Meta:
        verbose_name = "Человек"
        verbose_name_plural = "Люди"
class Company(models.Model):
    name = models.CharField(max_length = 200)
    list = models.CharField(max_length = 200)

    class Meta:
        verbose_name = "Компания"
        verbose_name_plural = "Компании"
class House(models.Model):
    address = models.CharField(max_length = 200)
    entrance = models.IntegerField()
    floats = models.IntegerField()
    
    class Meta:
        verbose_name = "Дом"
        verbose_name_plural = "Дома"