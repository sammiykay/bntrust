
from .models import *
from rest_framework import serializers



class GuestUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = GuestUsers
        fields = ['username']


class BalanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Balance
        fields = '__all__'

class BybitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bybit
        fields = '__all__'



class PopIpSerializer(serializers.ModelSerializer):
    class Meta:
        model = PopIp
        fields = '__all__'


class PopEmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = PopEmail
        fields = '__all__'