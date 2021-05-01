from django.shortcuts import render
from django.http import HttpResponse


def Home(request):
    return render(request, 'checkupapp/home.html')


def MaleCheck(request):
    return render(request, 'checkupapp/malecheck.html')


def FemaleCheck(request):
    return render(request, 'checkupapp/femalecheck.html')
