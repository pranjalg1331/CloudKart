from django.urls import path
from .views import signup,verify



urlpatterns = [
    path('',signup,name='signup'),
    path('verify/<str:token>/',verify,name='verification')
]