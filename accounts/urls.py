
from django.urls import path

from . import views

urlpatterns = [
    path('register/', views.SignUp.as_view(), name="signup"), # views.SignUp.as_view (classe do django) 
]

    