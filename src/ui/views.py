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
    #TODO : CONTAINERIZE QUERY ENGINE 
    from .llm_query_engine import LLMQueryEngine
    engine = LLMQueryEngine()
    
    response = engine.test_import("HELLOOOO")
    
    return JsonResponse({'response': response})