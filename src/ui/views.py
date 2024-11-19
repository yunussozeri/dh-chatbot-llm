import requests as r
import json as jj
from django.http import HttpResponse

def hello(request):
    
    name = request.GET.get('name')
    message = f'Hosgeldin {name} ! '
    return HttpResponse(message)