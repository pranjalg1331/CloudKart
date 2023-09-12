from django.urls import path
from .views import store,cart


urlpatterns = [
    path('',store,name='storepage'),
    path('cart',cart,name='cartpage')
]