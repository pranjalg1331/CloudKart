from django.urls import path
from .views import store,cart,updateQuantity


urlpatterns = [
    path('',store,name='storepage'),
    path('cart',cart,name='cartpage'),
    path('update_quantity/<int:itemId>/',updateQuantity,name='updateQuantity'),

    
]
