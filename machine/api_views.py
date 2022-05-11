from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Currency, Product, TransactionHistory
from .serializers import CurrencySerializer, ProductSerializer, TransactionHistorySerializer


class CurrencyViewset(viewsets.ModelViewSet):
    """
    Currency model Viewset
    """

    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer


class ProductViewset(viewsets.ModelViewSet):
    """
    Product model Viewset
    """

    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class TransactionHistoryViewset(APIView):
    """
    Transaction History model Viewset
    """

    # queryset = TransactionHistory.objects.all()
    # serializer_class = TransactionHistorySerializer

    def post(self, request):
        """
        used to calculate refund and total amount collected from vendor machine
        """

        try:
            serializer = TransactionHistorySerializer(data=request.data)
            if serializer.is_valid():
                product_id = serializer.data['product']
                product = Product.objects.get(id=product_id)
                product_price = product.price
                currency_list = serializer.data['currency']
                total_amount = 0
                for currency_id in currency_list:
                    total_amount += int(Currency.objects.get(id=currency_id).value)
                if total_amount >= product_price:
                    refund_amount = total_amount - product_price
                else:
                    response_data = {"message": "total amount is less than product price"}
                    return Response(response_data,
                                    status=status.HTTP_400_BAD_REQUEST)

                trans_hist_obj = TransactionHistory.objects.create(
                                    product= product,
                                    total_amount=total_amount,
                                    refunded_amount=refund_amount
                                )
                trans_hist_obj.currency.set(currency_list)
                product.quantity -= 1
                product.save()
                response_data = {'product_sold': True, 'product_name': product.name, 'refund_amount': refund_amount}
                return Response(response_data, status=status.HTTP_201_CREATED)
            else:
                response_data = {'message': 'Data Passed in serializer is incorrect'}
                return Response(response_data,
                                status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            raise Exception("something went wrong %s", e)
