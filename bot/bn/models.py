from django.db import models
from django_cleanup import cleanup
from django.contrib.auth.models import User
# Create your models here.



class DonnaUsers(models.Model):
    username = models.CharField(max_length=100000)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.username

@cleanup.select
class MohammedUsers(models.Model):
    username = models.CharField(max_length=100000)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.username


class GuestUsers(models.Model):
    username = models.CharField(max_length=100000)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.username



class Balance(models.Model):
    symbol = models.CharField(max_length = 232323, default = 'empty')
    leverage = models.IntegerField(default = 0)
    side = models.CharField(max_length = 232323, default = 'empty')
    entry_price = models.FloatField(default = 0)
    tp1 = models.FloatField(default = 0)
    tp2 = models.FloatField(default = 0)
    tp3 = models.FloatField(default = 0)
    stop_loss = models.FloatField(default = 0)
    close_order = models.CharField(max_length = 232323, default = 'empty')
    close_position = models.CharField(max_length = 232323, default = 'empty')


    def __str__(self):
        return f'- {self.symbol}'


class Bybit(models.Model):
    symbol = models.CharField(max_length = 232323, default = 'empty')
    leverage = models.IntegerField(default = 0)
    side = models.CharField(max_length = 232323, default = 'empty')
    entry_price = models.FloatField(default = 0)
    tp1 = models.FloatField(default = 0)
    tp2 = models.FloatField(default = 0)
    tp3 = models.FloatField(default = 0)
    tp4 = models.FloatField(default = 0)
    tp5 = models.FloatField(default = 0)
    tp6 = models.FloatField(default = 0)
    stop_loss = models.FloatField(default = 0)
    close_order = models.CharField(max_length = 232323, default = 'empty')
    close_position = models.CharField(max_length = 232323, default = 'empty')


    def __str__(self):
        return f'{self.entry_price} - {self.symbol}'


class PopEmail(models.Model):
    email = models.CharField(max_length=100000)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username



class PopIp(models.Model):
    device_name = models.CharField(max_length=100000)
    created_at = models.DateTimeField(auto_now_add=True)
    expire_at = models.DateTimeField()


    def __str__(self):
        return self.username