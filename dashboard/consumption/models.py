# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class User(models.Model):
    UserId = models.IntegerField()
    area = models.CharField(max_length=3)
    tariff = models.CharField(max_length=3)

class Consumption(models.Model):
    date_time = models.DateTimeField()
    user_consumption = models.FloatField()

