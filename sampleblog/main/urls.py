from django.urls import path

from .views import index, about_page


app_name = 'main'
urlpatterns = [
    path('', index, name='index'),
    path('about/', about_page, name='about')
]