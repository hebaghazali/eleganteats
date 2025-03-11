from django.http import HttpResponse
from django.shortcuts import redirect, render

from .forms import FoodItemForm
from .models import FoodItem
from django.contrib import messages

from django.http import HttpResponse


def menu_list(request):
    items = FoodItem.objects.all()
    context = {'items': items}

    return render(request, 'menu/menu_list.html', context)


def menu_item_detail(request, item_id):
    try:
        item = FoodItem.objects.get(pk=item_id)
        return render(request, 'menu/menu_item_detail.html', {'item': item})
    except FoodItem.DoesNotExist:
        return HttpResponse('Failed: Item not found')


def menu_item_add(request):
    form = FoodItemForm(request.POST or None)

    if form.is_valid():
        form.save()
        messages.success(request, 'show_modal_success')
        return redirect('menu:menu_item_add')

    return render(request, 'menu/menu_item_add.html', {'form': form})


def menu_item_update(request, id):
    item = FoodItem.objects.get(pk=id)
    form = FoodItemForm(request.POST or None, instance=item)

    print(request.method)

    if form.is_valid():
        form.save()
        messages.success(request, 'show_modal_success')
        return redirect('menu:menu_list')

    return render(request, 'menu/menu_item_update.html', {'form': form, 'item': item})
