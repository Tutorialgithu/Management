"""
URL configuration for HotelManagement project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from . import views

urlpatterns = [
    
    path('',views.Index, name='index'),
    path('admin/', views.LogInpage, name='admin'),
    path('about', views.Aboutpage, name='about'),
    path('service', views.Servicepage, name='service'),
    path('rooms', views.Roomspage, name='rooms'),
    path('dashboard', views.Dashboardpage, name='dashboard'),
    path('booking', views.booking, name='booking'),
    path('orderlist', views.orderlist, name='orderlist'),
    path('orderlistpage', views.orderlistpage, name='orderlistpage'),
    path('billinglist', views.billinglist, name='billinglist'),
    path('query', views.Querypage, name='query'),
    path('food', views.Foodpage, name='food'),
    path('contactpage', views.contactpage, name='contactpage'),
    path('contactdata', views.contactdata, name='contactdata'),
    # path('querylist', views.querylist, name='querylist'),
    path('invoicelist', views.invoicelist, name='invoicelist'),
    path('foodlist', views.foodlist, name='foodlist'),
    path('savedata', views.savedata, name='savedata'),
    path('invoice', views.Invoicepage, name='invoice'),
    path('paymentstatus', views.paymentstatus, name='paymentstatus'),
    



 # dj_razorpay/urls.py
    # path('paymenthandler/', views.paymenthandler, name='paymenthandler'),

    # path('invoice', views.invoice, name='invoice'),
    # path('invoice/<int:id>', views.invoice, name='invoice'),
    

    # path('displayfood', views.displayfood, name='displayfood'),


    
]