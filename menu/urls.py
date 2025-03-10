from django.urls import path

from . import views

app_name = 'menu'

urlpatterns = [
    path('', views.menu_list, name='menu_list'),
    path('<int:item_id>/', views.menu_item_detail, name='menu_item_detail'),
    path('add/', views.menu_item_add, name='menu_item_add'),
]