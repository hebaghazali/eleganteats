from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render

from menu.forms import FoodItemForm
from menu.models import FoodItem

import json
import pprint
from django.http import HttpResponse


def menu_list(request):
    items = FoodItem.objects.all()
    context = {"items": items}

    return render(request, "menu/menu_list.html", context)


def menu_item_detail(request, item_id):
    try:
        item = FoodItem.objects.get(pk=item_id)
        return render(request, "menu/menu_item_detail.html", {"item": item})
    except FoodItem.DoesNotExist:
        return HttpResponse("Failed: Item not found")


def menu_item_add(request):
    form = FoodItemForm(request.POST or None)
    debug_request(request)
    if form.is_valid():
        form.save()
        return redirect("menu:menu_list")

    return render(request, "menu/menu_item_add.html", {"form": form})


def debug_request(request):
    request_data = {
        "Method": request.method,
        "Path": request.path,
        "Full URL": request.build_absolute_uri(),
        "GET Parameters": dict(request.GET),
        "POST Data": dict(request.POST),
        "Headers": dict(request.headers),
        "Cookies": dict(request.COOKIES),
        "User": str(request.user),
    }

    # Pretty-print output to the console
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(request_data)

    # Convert to formatted JSON for an HTTP response
    formatted_output = json.dumps(request_data, indent=4)

    return HttpResponse(f"<pre>{formatted_output}</pre>", content_type="text/html")
