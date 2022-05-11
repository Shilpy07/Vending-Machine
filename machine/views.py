from django.http import JsonResponse
from django.shortcuts import render
from machine.forms import TransactionHistoryForm

def transactionCollection(request):
    """
    Collection transaction from UI
    """
    response_data = {'trans_form': TransactionHistoryForm}
    return render(request, 'index.html', response_data)


