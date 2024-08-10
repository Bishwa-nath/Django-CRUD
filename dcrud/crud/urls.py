from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('customer/<int:pk>', views.customer, name='customer'),
    path('update_customer/<int:pk>', views.update_customer, name='update_customer'),
    path('delete_customer/<int:pk>', views.delete_customer, name='delete_customer'),
    path('add_customer/', views.add_customer, name='add_customer'),
]
