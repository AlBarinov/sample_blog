from django.urls import path

from .views import index, about_page, BlogLoginView, profile


app_name = 'main'
urlpatterns = [
    path('accounts/profile/', profile, name='profile'),
    path('accounts/login/', BlogLoginView.as_view(), name='login'),
    path('', index, name='index'),
    path('about/', about_page, name='about')
]