from django.http import Http404
from django.shortcuts import render

from menus.models import MenuItem


def index(request):
    return render(request, "menus/index.html")

def item_section(request, item_name: str):
    menu_item_list = MenuItem.objects.filter(name=item_name)
    
    try:
        menu_item = menu_item_list[0]
    except IndexError:
        return Http404
    
    return render(request, "menus/item.html", {"item": menu_item})
