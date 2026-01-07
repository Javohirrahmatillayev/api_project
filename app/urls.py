from django.urls import path
from .views import *

urlpatterns = [
    path('fbv/cars/', car_list_create),
    path('fbv/cars/<int:pk>/', car_detail),
    
    
    path('cbv/cars/', CarListCreateAPIView.as_view()),
    path('cbv/cars/<int:pk>/', CarRetrieveUpdateDestroyAPIView.as_view()),
]