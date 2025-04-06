from rest_framework import serializers
from . models import Order,OrderItem
from inventory.models import Product,Stock
from django.db import transaction
import uuid

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['product','quantity','unit_price','total_price']
        read_only_fields = ['unit_price','total_price']


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = ['id','order_number','customer_name','customer_email','status','total_amount','items','created_at']
        read_only_fields = ['order_number','total_amount']

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        total_amount = 0

        ## Generate a unique order number ##
        validated_data['order_number'] = f"ORD-{uuid.uuid4().hex[:8].upper()}"

        with transaction.atomic():
            order = Order.objects.create(**validated_data,total_amount=total_amount)

            for item_data in items_data:
                product = item_data['product']
                quantity = item_data['quantity']

                unit_price = product.price
                total_price = unit_price * quantity
                total_amount += total_price

                try:
                    stock = Stock.objects.get(product=product)
                    if stock.quantity < quantity:
                        raise serializers.ValidationError(f"Not enough stock for {product.name}. Available: {stock.quantity}")
                    
                    stock.quantity -= quantity
                    stock.save()
                
                except Stock.DoesNotExist:
                    raise serializers.ValidationError(f"No stock information found for product {product.name}")
                

                OrderItem.objects.create(
                    order=order,
                    product=product,
                    quantity=quantity,
                    unit_price=unit_price,
                    total_price=total_price
                )
            
            order.total_amount = total_amount
            order.save()
            return order

