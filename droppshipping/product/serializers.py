from rest_framework import serializers
from product.models import Product

class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ['product_id', 'product_name', 'product_desc', 'product_price']