from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('', views.dashboard, name='dashboard'),
    path('trade/add/', views.add_trade, name='add_trade'),
    path('trade/<int:id>/edit/', views.edit_trade, name='edit_trade'),
    path('trade/<int:id>/delete/', views.delete_trade, name='delete_trade'),
    path('logout/', views.logout, name='logout'),  
]
