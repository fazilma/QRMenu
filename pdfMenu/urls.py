

from django.urls import path
from . import views

app_name = 'pdfmenu'
urlpatterns = [
    path('', views.MenuView.as_view(), name='menu')
]
