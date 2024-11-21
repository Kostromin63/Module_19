from django.db import models


class Buyer(models.Model):
    name = models.CharField(max_length=30)# username
    balance = models.DecimalField(decimal_places=2, max_digits=9)
    age = models.IntegerField()

    def __str__(self):
        return self.name


class Game(models.Model):
    title = models.CharField(max_length=200)
    cost = models.DecimalField(max_digits=7, decimal_places=2) # в рублях с копейками
    size = models.DecimalField(max_digits=7, decimal_places=1) # в мегабайтах
    description = models.TextField()
    age_limited = models.BooleanField(default=False)
    buyer = models.ManyToManyField(Buyer, related_name='buyers')