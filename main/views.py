from django.shortcuts import render


def index(request):
    return render(request, 'main/index.html')


def picture(request):
    return render(request, 'main/picture.html')