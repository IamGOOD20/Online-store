from django.urls import path
from . import views
from .views import RegisterUser, LoginUser

urlpatterns = [
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', views.logout, name='logout'),
    path('register/', RegisterUser.as_view(), name='register'),
]
