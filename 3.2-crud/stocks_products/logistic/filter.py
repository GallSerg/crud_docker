from django_filters import rest_framework as filters
from .models import Stock


class StockFilter(filters.FilterSet):
    product = filters.NumberFilter(field_name='products__id')

    class Meta:
        model = Stock
        fields = ['products']
