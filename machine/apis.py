from rest_framework import routers

from .api_views import CurrencyViewset, ProductViewset, TransactionHistoryViewset

router = routers.DefaultRouter()
router.register(r'currency', CurrencyViewset)
router.register(r'products', ProductViewset)