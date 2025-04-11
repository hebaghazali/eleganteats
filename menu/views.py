from django.http import HttpResponse
from django.shortcuts import redirect, render

from .forms import FoodItemForm
from .models import FoodItem
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from django.http import HttpResponse


def menu_list(request):
    items = FoodItem.objects.all()
    context = {'items': items}

    return render(request, 'menu_list.html', context)


def menu_item_detail(request, item_id):
    try:
        item = FoodItem.objects.get(pk=item_id)
        return render(request, 'menu_item_detail.html', {'item': item})
    except FoodItem.DoesNotExist:
        return HttpResponse('Failed: Item not found')


@login_required
def menu_item_add(request):
    form = FoodItemForm(request.POST or None)

    if form.is_valid():
        form.save()
        messages.success(request, 'The item has been added successfully.')
        return redirect('menu:menu_item_add')

    return render(request, 'menu_item_add.html', {'form': form})

@login_required
def menu_item_update(request, id):
    item = FoodItem.objects.get(pk=id)
    form = FoodItemForm(request.POST or None, instance=item)

    if form.is_valid():
        form.save()
        messages.success(request, 'The item has been updated successfully.')
        return redirect('menu:menu_list')

    return render(request, 'menu_item_update.html', {'form': form, 'item': item})


@login_required
def menu_item_delete(request, id):
    item = FoodItem.objects.get(pk=id)

    if request.method == 'POST':
        item.delete()
        messages.success(request, 'The item has been deleted successfully.')
        return redirect('menu:menu_list')

    return render(request, 'menu_item_delete.html', {'item': item})
