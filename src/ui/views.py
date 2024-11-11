# views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render
import requests

def home_view(request):
    data = {"message": "Hello, World!"}
    return Response(data, status=status.HTTP_200_OK)

@api_view(['GET'])
def example_view(request):
    data = {"message": "Hello, World!"}
    return Response(data, status=status.HTTP_200_OK)
