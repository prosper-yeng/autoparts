from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('service-booking/', views.service_booking, name='service-booking'),
]
