from django.http import HttpResponse
from django.shortcuts import render


def homepage(request):
    return render(request, 'home.html')


def about(request):
    # return HttpResponse("This is the about page of the project authentication system.")
    return render(request, 'about.html')
