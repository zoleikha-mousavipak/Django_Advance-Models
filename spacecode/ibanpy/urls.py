from django.urls import path
from .views import *

app_name = "iban"

urlpatterns = [
    path('', index, name="index")
]