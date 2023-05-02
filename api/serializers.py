from rest_framework import serializers
from .models import PrimeNumber

class PrimeNumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrimeNumber
        # fields = '__all__'
        exclude = ('id',) 