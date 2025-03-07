from django.http import HttpResponse
from django.shortcuts import render

from menu.models import Item

# Create your views here.
def index(request):
    item_list = Item.objects.all()
    print(f"{item_list}")
    return HttpResponse(item_list)

def item(request, item_id):
    try:
        item = Item.objects.get(pk=item_id)
        if not item:
            return HttpResponse("Item not found")
        return HttpResponse(f"Item: {item.name} - {item.description} - ${item.price}")
    except Item.DoesNotExist:
        return HttpResponse("Failed: Item not found")