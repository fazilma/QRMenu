from http.client import HTTPResponse
from django.views import View
from django.shortcuts import render
# Create your views here.


class MenuView(View):
    template_name = 'pdf_menu/menu.html'

    def get(self, request, rest):
        ctx={}
        ctx['rest']=rest
        return render(request, self.template_name, context= ctx)
