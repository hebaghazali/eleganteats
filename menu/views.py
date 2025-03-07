from django.http import HttpResponse
from django.shortcuts import render

from menu.models import FoodItem


def index(request):
    item_list = FoodItem.objects.all()
    context = {'item_list': item_list}

    return render(request, 'menu/index.html', context)


def item_detail(request, item_id):
    try:
        item = FoodItem.objects.get(pk=item_id)
        if not item:
            return HttpResponse("Item not found")
        return HttpResponse(f"Item: {item.name} - {item.description} - ${item.price}")
    except FoodItem.DoesNotExist:
        return HttpResponse("Failed: Item not found")
