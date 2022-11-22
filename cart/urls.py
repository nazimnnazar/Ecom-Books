from django.urls import path
from .import views
urlpatterns = [
    path('Cart_Deta_il', views.cartdetails, name='Cart_Deta_il'),
    path('add/<int:product_id>/',views.add_cart,name='addcart'),
    path('min/<int:product_id>/', views.min_cart, name='mincart'),
    path('remove/<int:product_id>/', views.remove, name='remove'),
    
]