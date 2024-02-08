from django.urls import path

from .views import (index, about_page, BlogLoginView, profile, BlogLogoutView, ChangeUserInfoView,
                    BlogPasswordChangeView, RegisterUserView, DeleteUserView, rubric, by_rubric,
                    detail, detail_index)


app_name = 'main'
urlpatterns = [
    path('accounts/logout/', BlogLogoutView.as_view(), name='logout'),
    path('accounts/password/change/', BlogPasswordChangeView.as_view(), name='password_change'),
    path('accounts/profile/delete/', DeleteUserView.as_view(), name='profile_delete'),
    path('accounts/profile/change/', ChangeUserInfoView.as_view(), name='profile_change'),
    path('accounts/profile/', profile, name='profile'),
    path('accounts/register/', RegisterUserView.as_view(), name='register'),
    path('accounts/login/', BlogLoginView.as_view(), name='login'),
    path('', index, name='index'),
    path('index/<int:pk>/', detail_index, name='detail_index'),
    path('rubric/', rubric, name='rubric'),
    path('<int:rubric_pk>/<int:pk>/', detail, name='detail'),
    path('<int:pk>/', by_rubric, name='by_rubric'),
    path('about/', about_page, name='about')
]