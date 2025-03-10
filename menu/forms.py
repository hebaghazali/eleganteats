from django import forms
from .models import FoodItem


class FoodItemForm(forms.ModelForm):
    class Meta:
        model = FoodItem
        fields = ["name", "description", "price", "image_url"]
        widgets = {
            "name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "id": "item-name",
                    "placeholder": "Enter item name",
                    "required": True,
                }
            ),
            "description": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "id": "description",
                    "placeholder": "Enter description",
                    "rows": 3,
                    "required": True,
                }
            ),
            "price": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "id": "price",
                    "step": "0.01",
                    "placeholder": "Enter price",
                    "required": True,
                }
            ),
            "image_url": forms.URLInput(
                attrs={
                    "class": "form-control",
                    "id": "image",
                }
            ),
        }
