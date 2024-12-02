import requests as r
from django.http import HttpResponse, JsonResponse
from .llm_query_engine import LLMQueryEngine

engine = LLMQueryEngine()

def hello(request):
    
    #name = request.GET.get('name')
    
    message = f'Wilkommen  endlich ! '
    
    return HttpResponse(message)


def llm_engine(request):
    
    return HttpResponse(content="hi" )
    '''query = request.GET.get('q', '')
    if not query:
        return JsonResponse({'error': 'Query parameter is missing'}, status=400)
    
    #response = engine.submit_query(query)
    
    return JsonResponse(query)'''
    # return JsonResponse({'response': response.answer}, status=200)