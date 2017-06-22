# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Manufacturer(models.Model):
    name = models.CharField(max_length=20)
    year_foundede = models.IntegerField()

class Car(models.Model):
    number_plate = models.CharField(max_length=10)
    owner = models.CharField(max_length=20)
    last_inspection = models.DateField()
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
