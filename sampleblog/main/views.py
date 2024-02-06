from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required

class BlogLoginView(LoginView):
    template_name = 'main/login.html'

def index(request):
    return render(request, 'main/index.html')

def about_page(request):
    return render(request, 'main/about_page.html')

@login_required
def profile(request):
    return render(request, 'main/profile.html')
