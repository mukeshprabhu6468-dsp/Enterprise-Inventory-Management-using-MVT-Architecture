from django.urls import path, include
from .views import *

urlpatterns = [
    path('customers/', All_Customer, name='all_customers'),
    path('customers/add/', Add_Customer, name='add_customer'),
    path('customers/edit/<int:id>', Edit_Customer, name='edit_customer'),
    path('customers/delete/<int:id>', Delete_Customer, name='delete_customer'),

    path('all_orders/', All_Orders, name='all_orders'),
    path('add_order/', Add_Order, name='add_order'),
    path('edit_order/<int:id>', Edit_Order, name='edit_order'),
    path('delete_order/<int:id>', Delete_Order, name='delete_order'),
]