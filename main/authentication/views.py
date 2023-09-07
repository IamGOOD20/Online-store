from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from . forms import LoginForm


def login_user(requests):
    data = {'title': 'login', 'login_form': LoginForm()}
    if requests.method == 'POST':
        login_form = LoginForm(requests.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(requests, user)
                return redirect('index')

    return render(requests, 'main/login.html', context=data)

# def registration(requests):
#     data = {'title': 'registration'}
#     return render(requests, 'main/register.html', context=data)

def logout_user(requests):
    logout(requests)
    return redirect('index')


# class RegisterUser(CreateView):
#     form_class = UserCreationForm
#     template_name = 'main/login.html'
#     success_url = reverse_lazy('index')

