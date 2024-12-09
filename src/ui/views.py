import requests as r
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

def hello(request):
    
    #name = request.GET.get('name')
    
    #message = f'Wilkommen  endlich ! '

    #return render(request, 'app/hello.html')
    data = {'message': 'Welcome to My Website!', 'status': 'success'}
    return JsonResponse(data) 
    
    #return HttpResponse(message)


def llm_engine(request):
    
    q = request.GET.get('q')
    
    
    
    
    return JsonResponse({'response': f'{q}'})