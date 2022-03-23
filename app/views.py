from random import randint
import time

from django.shortcuts import render


def index(request):
    if request.user.is_authenticated:
        context = {'item': randint(1, 10 ** 6)}
        return render(request, 'index.html', context)
    return render(request, 'index.html')




