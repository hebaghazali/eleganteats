from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the menu index.")

def item(request, item_id):
    return HttpResponse(f"You're looking at item <strong>{item_id}</strong>.")