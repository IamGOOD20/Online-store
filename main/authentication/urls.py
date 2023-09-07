from django.urls import path
from . import views
# from .views import RegisterUser


urlpatterns = [
    # path('registration/', RegisterUser.as_view(), name='register'),
    path('authentication/', views.login_user, name='authentication'),
    path('logout/', views.logout, name='logout'),
]
