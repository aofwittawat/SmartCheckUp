from django.urls import path, include
from .views import *

urlpatterns = [
    path('', Home),
    path('malecheck/', MaleCheck, name="malecheck"),
    path('femalecheck/', FemaleCheck, name="femalecheck"),
]
