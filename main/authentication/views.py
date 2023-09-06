from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

# data = {
#     '1': 'login',
#     '2': 'registration'
# }



def login(requests):
    data = {'title': 'login'}
    return render(requests, 'main/login.html', context=data)

# def registration(requests):
#     data = {'title': 'registration'}
#     return render(requests, 'main/register.html', context=data)

# def logout_user(requests):
#     logout(requests)
#     return redirect('main/index.html')


class RegisterUser(CreateView):
    form_class = UserCreationForm
    template_name = 'main/login.html'
    success_url = reverse_lazy('login')