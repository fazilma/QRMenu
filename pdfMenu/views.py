from http.client import HTTPResponse
from django.views import View
from django.shortcuts import render
# Create your views here.


class MenuView(View):
    template_name = 'pdfMenu/menu.html'

    def get(self, request):
        return render(request, self.template_name)
