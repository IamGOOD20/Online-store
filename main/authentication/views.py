from django.shortcuts import render

# data = {
#     '1': 'login',
#     '2': 'registration'
# }


def login(requests):
    data = {'title': 'login'}
    return render(requests, 'main/login.html', context=data)

def registration(requests):
    data = {'title': 'registration'}
    return render(requests, 'main.registration.html', context=data)

def logout(requests):
    pass