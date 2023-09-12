from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import RegisterUserForm


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'main/register.html'
    success_url = reverse_lazy('login')
    title = 'Register'


class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = 'main/login.html'
    title = 'Authorisation'

    def get_success_url(self):
        return reverse_lazy('index')


def logout_user(requests):
    logout(requests)
    return redirect('index')

