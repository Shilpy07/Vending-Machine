from django.db import models


class Currency(models.Model):
    """
    Model representation for accepted currencies
    """

    value = models.IntegerField()

    class Meta:
        """
        meta data for model Currency
        """

        verbose_name_plural = 'Currencies'

    def __str__(self):
        """
        returns the value of currency
        """

        return str(self.value)


class Product(models.Model):
    """
    Model representation for available products
    """

    name = models.CharField(max_length=15)
    price = models.IntegerField()
    quantity = models.IntegerField(null=True, blank=True)

    class Meta:
        """
        meta data for model Product
        """

        verbose_name_plural = 'Products'

    def __str__(self):
        """
        returns the name of the product
        """

        return self.name


class TransactionHistory(models.Model):
    """
    Model representation for maintaining transaction history
    """

    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING) # 50
    currency = models.ManyToManyField(Currency) # 60
    transaction_date = models.DateField(auto_now_add=True)
    total_amount = models.IntegerField(null=True) # 60  -> calculation by program
    refunded_amount = models.IntegerField(null=True) # 60-50 = 10 -> calculation by program


    class Meta:
        """
        meta data for model Transaction History
        """

        verbose_name_plural = 'Transaction History'

    def __str__(self):
        """
        returns the name of the product
        """

        return str(self.product.name)