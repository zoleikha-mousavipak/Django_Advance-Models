from django.shortcuts import render
from .models import *


def index(request):
    myibans = MyIBANModel.objects.all()

    return render(request, 'ibanpy/index.html', {'myibans': myibans})
