from django.urls import path
from .import views
urlpatterns = [

   
    path('<slug:c_slug>/',views.book,name='product'),
    path('product/',views.book,name='product'),
    path('<slug:c_slug>/<slug:product_slug>', views.product_views, name='view'), 
    path('',views.frontpage,name='frontpage'),
]