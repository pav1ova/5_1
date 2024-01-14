from django.shortcuts import render
from .models import People, Company, House
# Create your views here.
def index(request):
    data = {'title': 'Главная страница',
            'values': ['Some', 'Hello', '123']}
    return render(request, 'main/index.html', data)

def about(request):
    return render(request, 'main/about.html')

def company(response):
    data = People.objects.all()
    return render(response, 'main/company.html', {"data": data})

def main(response):
    data = Company.objects.all()
    return render(response, 'main/main.html', {"companies": data})