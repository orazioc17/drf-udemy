from django.shortcuts import render
from django.views.generic.base import View
from django.http import HttpResponse


# Create your views here.
class HelloWorld(View):
    def get(self, request):
        data = {
            'name': 'Orazio Cappadonna Cantor',
            'years': 28,
            'code': ['Python', 'Django', 'React']
        }
        return render(request, 'index.html', context=data)
