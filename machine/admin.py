from django.contrib import admin
from .models import Currency, Product, TransactionHistory

class CurrencyAdmin(admin.ModelAdmin):
    """
    Admin representation for model Currency
    """

    list_display = ('id', 'value')

class ProductAdmin(admin.ModelAdmin):
    """
    Admin representation for model Product
    """

    list_display = ('id', 'name', 'price', 'quantity')


class TransactionHistoryAdmin(admin.ModelAdmin):
    """
    Admin representation for model TransactionHistory
    """

    list_display = ('id', 'product', 'transaction_date', 'total_amount', 'refunded_amount')


admin.site.register(Currency, CurrencyAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(TransactionHistory, TransactionHistoryAdmin)
