import requests as r
import json
from django.http import HttpResponse, JsonResponse

LLM_URL = "http://benedikt-home-server.duckdns.org:11434"

def hello(request):
    
    name = request.GET.get('name')
    message = f'Hosgeldin {name} ! '
    return HttpResponse(message)

def merhaba(request):
    # Make sure you're reading the raw body if you're sending JSON
    try:
        data = json.loads(request.body)  # Parse the incoming JSON body
        name = data.get('query', '')  # Get the query parameter

        # You can log or inspect the data if needed
        f = open("output.txt", "w")
        return_message = ""
        for k, v in data.items():
            return_message += f"{k} --> {v}\n"
            f.write(f"{k} --> {v}\n")
        f.close()

        # Return the response message
        message = f'Hosgeldin {name} !'
        return HttpResponse({"message": message, "details": return_message})
    except json.JSONDecodeError:
        return JsonResponse({"error": "Invalid JSON"}, status=400)
    
    