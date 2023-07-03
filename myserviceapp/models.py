from django.contrib.auth.models import User
from django.db import models

class Service(models.Model):
    title = models.CharField(max_length=200)
    price = models.FloatField()
    description = models.TextField()
    users_old = models.ManyToManyField(User,related_name = 'services_old')
    users = models.ManyToManyField(User, through='Rent',related_name = 'services')
    category = models.CharField(max_length=100)
    amount = models.IntegerField(null=True, blank=True)

class Rent(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    amount = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)