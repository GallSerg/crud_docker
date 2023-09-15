from rest_framework import serializers
from .models import Product, StockProduct, Stock


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['title', 'description']


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
        print(positions)

        stock_ = super().create(validated_data)
        stock_.save()
        print(stock_)

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
        stock_products = stock.positions.all()

        for position in positions:
            product = stock_products.filter(product_id=position['product'])
            product = product[0]
            if product:
                product.quantity = position['quantity']
                product.price = position['price']
                product.save()

        return stock
