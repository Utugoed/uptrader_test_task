from django.urls import path

from menus import views


urlpatterns = [
    path('', views.index, name='index'),
    path('<str:item_name>', views.item_section, name="menu_item"),
]