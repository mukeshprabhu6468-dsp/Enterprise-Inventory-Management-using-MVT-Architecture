from django.urls import path
from .views import *

urlpatterns = [
    path('', AllProducts, name='index_products'),
    path('products/',AllProducts,name='all_products'),
    path('products/add/',AddProduct,name='add_product'),
    path('products/edit/<int:id>',UpdateProduct,name='edit_product'),
    path('products/delete/<int:id>',DeleteProduct,name='delete_product'),
]