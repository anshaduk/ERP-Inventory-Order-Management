from rest_framework import serializers
from . models import Product,Stock,Supplier

class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = '__all__'

class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = ['quantity','reorder_level','last_restock_date']

class ProductSerializer(serializers.ModelSerializer):
    stock = StockSerializer(read_only = True)

    class Meta:
        model = Product
        fields = ['id','name','description','sku','price','supplier','stock','created_at','updated_at']

    def create(self, validated_data):
        initial_stock = validated_data.pop('initial_stock')
        product = Product.objects.create(**validated_data)
        Stock.objects.create(product=product,quantity=initial_stock)
        return product