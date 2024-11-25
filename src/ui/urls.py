# urls.py
from django.urls import path
from . import views

urlpatterns = [
    
    path("hello", views.hello, name="hi"),
    path("merhaba", views.merhaba, name="mrb"),
]
