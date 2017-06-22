# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import Car # import Person
admin.site.register(Car) # register Person

from models import Manufacturer # import Manufacturer
admin.site.register(Manufacturer) # register Manufacturer

