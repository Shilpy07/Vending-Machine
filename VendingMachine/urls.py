"""VendingMachine URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from machine.api_views import TransactionHistoryViewset
from machine.views import transactionCollection
from machine import apis


from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static

urlpatterns = [
    path('', transactionCollection, name="transactionCollection"),
    path('admin/', admin.site.urls),
    path('api/v1/', include(apis.router.urls)),
    path('api/v1/transactions', TransactionHistoryViewset.as_view(), name='transaction')
]

urlpatterns += staticfiles_urlpatterns()
