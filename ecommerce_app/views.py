from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def service(request):
    return render(request, 'service.html')

def contact(request):
    return render(request, 'contact.html')

def reviews(request):
    return render(request, 'reviews.html')

def shop(request):
    return render(request, 'shop.html')