from django.http import HttpResponse
from django.shortcuts import render

from menu.models import FoodItem


def menu_list(request):
    items = FoodItem.objects.all()
    context = {'items': items}

    return render(request, 'menu/menu_list.html', context)


def menu_item_detail(request, item_id):
    try:
        item = FoodItem.objects.get(pk=item_id)
        return render(request, 'menu/menu_item_detail.html', {'item': item})
    except FoodItem.DoesNotExist:
        return HttpResponse("Failed: Item not found")
