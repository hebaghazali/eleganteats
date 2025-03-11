from django.urls import path

from . import views

app_name = 'menu'

urlpatterns = [
    path('', views.menu_list, name='menu_list'),
    path('<int:item_id>/', views.menu_item_detail, name='menu_item_detail'),
    path('add/', views.menu_item_add, name='menu_item_add'),
    path('update/<int:id>/', views.menu_item_update, name='menu_item_update'),
    path('delete/<int:id>/', views.menu_item_delete, name='menu_item_delete'),
]
