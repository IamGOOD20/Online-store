from django.shortcuts import render


def index(requests):
    data = {
        'title': 'Home'
    }
    return render(requests, 'main/index.html', context=data)


def about(requests):
    data = {'title': 'Home'
            }
    return render(requests, 'main/about.html', context=data) # about_us