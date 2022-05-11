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
    # Transaction History model serializer
    # """
    # amount = serializers.IntegerField()
    # refund = serializers.I

    # def get_amount(self, obj):
    #     amount = 0
    #     print(obj.currency.all())
    #     for currency in obj.currency.all():
    #         amount = amount + currency.value
    #     return amount
    #
    # def get_refund(self,obj):
    #     if obj.total_amount:
    #         product_price = obj.product.price
    #         refund = obj.total_amount - product_price
    #         return refund
    #     else:
    #         return 0

    class Meta:
        model = TransactionHistory
        fields = ('id', 'product', 'currency')
