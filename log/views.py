from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'index.html')


def sup(request):
    return render(request, 'hell/sign_up.html')


def home(request):
    return render(request, 'hell/home.html')
