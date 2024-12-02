# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path("hello/", views.hello, name="hello"),
    path("llm-engine/", views.llm_engine, name="llm-engine")
]
