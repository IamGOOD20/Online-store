from django.shortcuts import render

def index(requests):
    data = {'title': 'Home'}
    return render(requests, 'main/index.html', context=data)

def about(requests):
    data = {'title': 'about'}
    return render(requests, 'main/about.html', context=data)

def services(requests):
    data = {'title': 'services'}
    return render(requests, 'main/services.html', context=data)

def products(requests):
    data = {'title': 'products'}
    return render(requests, 'main/products.html', context=data)

def blog(requests):
    data = {'title': 'blog'}
    return render(requests, 'main/blog.html', context=data)

def contacts(requests):
    data = {'title': 'contacts'}
    return render(requests, 'main/contacts.html', context=data)
