from django.urls import path
from .views import store,cart,updateQuantity,paymenthandler,checkout


urlpatterns = [
    path('',store,name='storepage'),
    path('cart',cart,name='cartpage'),
    path('paymenthandler/', paymenthandler, name='paymenthandler'),
    path('update_quantity/<int:itemId>/',updateQuantity,name='updateQuantity'),
    path('cart/checkout/',checkout,name='checkout'),

    
]
