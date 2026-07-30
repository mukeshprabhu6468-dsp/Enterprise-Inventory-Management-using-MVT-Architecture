from django.urls import path
from .views import *

urlpatterns = [
    path('', LoginForm, name= 'login'),
    path('logout/', Logout, name= 'logout'),
    path('signup/', Signup, name= 'signup'),
    
]