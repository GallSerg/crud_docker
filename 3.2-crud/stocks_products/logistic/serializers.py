from rest_framework import serializers
from .models import Product, StockProduct, Stock


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title', 'description']


class ProductPositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockProduct
        fields = ['product', 'quantity', 'price']


class StockSerializer(serializers.ModelSerializer):
    positions = ProductPositionSerializer(many=True)

    class Meta:
        model = Stock
        fields = ['id','address', 'positions']

    def create(self, validated_data):
        positions = validated_data.pop('positions')
        stock_ = super().create(validated_data)
        stock_.save()
        for position in positions:
            new_ = StockProduct(
                stock=stock_,
                product=position['product'],
                quantity=position['quantity'],
                price=position['price']
            )
            new_.save()

        return stock_

    def update(self, instance, validated_data):
        positions = validated_data.pop('positions')
        stock = super().update(instance, validated_data)
        stock.save()
        for position in positions:
            StockProduct.objects.update_or_create(
                stock=stock,
                product=position['product'],
                defaults={
                    'price': position['price'],
                    'quantity': position['quantity']
                }
            )
        return stock
