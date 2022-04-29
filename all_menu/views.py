from django.shortcuts import render
from django.views import View
from django.views import generic
from pdf_menu.models import Menu

class AllMenus(View):
    template_name = 'all_menu/home.html'

    def get(self, request):
        return render(request, self.template_name)

class PopularMenus(generic.ListView):
    model = Menu