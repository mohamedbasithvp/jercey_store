from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from customers import views

urlpatterns = [
    path('account', views.show_account, name='account'),
    path('sign_out', views.sign_out, name='sign_out')
]