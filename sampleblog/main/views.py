from django.shortcuts import render

def index(request):
    return render(request, 'main/index.html')

def about_page(request):
    return render(request, 'main/about_page.html')
