from typing import Dict, Optional

from django import template

from menus.models import MenuItem


register = template.Library()


def mark_as_chosen(item_id: int, items_dict: dict) -> Dict[str, dict]:
    items_dict[item_id].choosen = True
    if items_dict[item_id].parent_id is not None:
        return mark_as_chosen(items_dict[item_id].parent_id, items_dict)
    return items_dict


@register.inclusion_tag(filename="menus/draw_menu.html", name="draw_menu")
def get_menu_items_list(name: str, choosen_item_name: Optional[str] = None):
    items_list = list(MenuItem.objects.all().filter(menu_name=name))
    items_dict = {}
    
    for item in items_list:
        item.children = []
        item.choosen = False
        items_dict[item.pk] = item
    
    for item in items_list:
        if item.name == choosen_item_name:
            mark_as_chosen(item.pk, items_dict)
            break
    
    for item in items_list:
        if item.parent_id is not None:
            items_dict[item.parent_id].children.append(items_dict[item.pk])

    root_list = []
    for item in items_dict.values():
        if not item.parent_id:
            root_list.append(item)
    
    return {"items_list": root_list}