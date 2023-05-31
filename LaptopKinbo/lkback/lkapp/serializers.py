from rest_framework import serializers
from lkapp.models import Laptop

class LaptopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Laptop
        fields = ['name','price']