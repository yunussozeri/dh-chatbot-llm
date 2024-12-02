import requests as r
from django.http import HttpResponse, JsonResponse
#from .llm_query_engine import LLMQueryEngine
from django.shortcuts import render

#engine = LLMQueryEngine()

def hello(request):
    
    #name = request.GET.get('name')
    
    #message = f'Wilkommen  endlich ! '

    #return render(request, 'app/hello.html')
    data = {'message': 'Welcome to My Website!', 'status': 'success'}
    return JsonResponse(data) 
    
    #return HttpResponse(message)


def llm_engine(request):
    
    #return HttpResponse(content="hi" )
    '''query = request.GET.get('q', '')
    if not query:
        return JsonResponse({'error': 'Query parameter is missing'}, status=400)
    
    #response = engine.submit_query(query)
    
    return JsonResponse(query)'''
    return JsonResponse({'response': 'hi'})