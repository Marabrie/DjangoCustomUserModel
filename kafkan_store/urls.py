from django.urls import path
from . import views


urlpatterns = [
    path('', views.kafkan_list, name='kafkan_list'),
    path('kafkan/<int:pk>/', views.kafkan_detail, name='kafkan_detail'),
    path('kafkan/new/', views.create_kafkan, name='kafkan_new'),
    path('kafkan/new/', views.kafkan_new, name='kafkan_new'),
    path('kafkan/<int:pk>/edit/', views.kafkan_edit, name='kafkan_edit'), 
    path('kafkan/<int:pk>/delete/', views.kafkan_delete, name='kafkan_delete'), 
    
]
