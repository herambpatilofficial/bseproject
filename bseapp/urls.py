from django.urls import path
from .views import index, stprice

urlpatterns = [
    
    path('',index),
    path('stprice',stprice)
]
