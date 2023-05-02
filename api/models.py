from django.db import models

class PrimeNumber(models.Model):
    number = models.IntegerField(unique=True)