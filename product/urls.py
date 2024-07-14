from django.urls import path
from . import views

urlpatterns = [
    path('lists', views.product_list, name='product_list'),
    path('home', views.home, name='home'),
    path('<int:product_id>/', views.product_detail, name='product_detail'),  
]