

from django.urls import path
from . import views

app_name = 'pdf_menu'
urlpatterns = [
    path('', views.MenuView.as_view(), name='menu'),
    path('<slug:rest>', views.MenuView.as_view(), name='pdf')

]
