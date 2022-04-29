from django.urls import path
from . import views

app_name = 'all_menu'
urlpatterns = [
     path('', views.AllMenus.as_view(), name='menu'),
     path('popular', views.PopularMenus.as_view(), name='popular_menus'),
]