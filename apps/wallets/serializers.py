from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import serializers
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Wallet  

Wallet = Wallet
class WalletCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wallet
        fields = ('id', 'user', 'address', 'balance', 'created_at')
        read_only_fields = ('id', 'user', 'address', 'balance', 'created_at')