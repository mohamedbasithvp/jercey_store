from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from products import views

urlpatterns = [
    path('', views.index, name='home'),
    path('product_list', views.list_products, name='list_product'),
    path('product_detail/<pk>', views.detail_products, name='detail_product'),
]