from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('service-booking/', views.service_booking, name='service-booking'),
    path('shop/', views.shop, name='shop'),
    path('shop_detail/', views.shop_detail, name='shop_detail'),
    path('promotion/', views.promotion, name='promotion'),
    path('testimonial/', views.testimonial, name='testimonial'),
    path('blog/', views.blog, name='blog'),
    path('blog_detail/', views.blog_detail, name='blog_detail'),
]