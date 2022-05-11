from rest_framework import serializers

from .models import Currency, Product, TransactionHistory


class CurrencySerializer(serializers.ModelSerializer):
    """
    Currency model serializer
    """

    class Meta:
        model = Currency
        fields = ('id', 'value')


class ProductSerializer(serializers.ModelSerializer):
    """
    Product model serializer
    """

    class Meta:
        model = Product
        fields = ('id', 'name', 'price', 'quantity')


class TransactionHistorySerializer(serializers.ModelSerializer):
    """
    Transaction History model serializer
    """

    class Meta:
        model = TransactionHistory
        fields = ('id', 'product', 'currency')
