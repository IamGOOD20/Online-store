from django.urls import path
from . import views
from .views import RegisterUser


urlpatterns = [
    path('registration/', RegisterUser.as_view(), name='registration'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
]
