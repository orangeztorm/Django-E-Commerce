from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    university = 'lasu'
    name = 'taiwo'
    context = {
        'university': university,
        'name': name
    }
    return render(request, 'index.html', context)
