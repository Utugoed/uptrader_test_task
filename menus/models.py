from django.db import models
from django.urls import reverse


# Create your models here.
class MenuItem(models.Model):
    caption = models.CharField(max_length=150)
    name = models.CharField(max_length=150, unique=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    menu_name = models.CharField(max_length=150)

    def get_absolute_url(self):
        return reverse("menu_item", kwargs={"item_name": self.name})
