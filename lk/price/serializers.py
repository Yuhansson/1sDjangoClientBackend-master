from rest_framework import serializers
from .models import Prices


class PricesSerializer(serializers.ModelSerializer):
    title = serializers.CharField(source='product.full_name', read_only=True)

    class Meta:
        model = Prices
        fields = ['id', 'product', 'title', 'price']
