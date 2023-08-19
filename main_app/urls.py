from django.urls import path 
from . import views

urlpatterns = [
    path('user/<int:user_id>/', views.user_profile, name='user_profile'),
    path('product/<int:product_id>/', views.product_details, name='product_details'),
    path('products/<int:product_id>/', views.product_page, name='product_page'),
    path('productsp/<int:product_id>/update_price/<int:new_price>/', views.update_product_price, name='update_product_price'),
]
