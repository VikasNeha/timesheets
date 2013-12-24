from django.shortcuts import render

def index(request):
    context = {'Hi': 'Hello World'}
    return render(request, 'myTimesheet/index.html', context)
