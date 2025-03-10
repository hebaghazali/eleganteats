from django import forms
from .models import FoodItem


class FoodItemForm(forms.ModelForm):
    class Meta:
        model = FoodItem
        fields = ['name', 'description', 'price', 'image_url', 'chef']
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'id': 'item-name',
                    'placeholder': 'Enter item name',
                    'required': True,
                }
            ),
            'description': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'id': 'description',
                    'placeholder': 'Enter description',
                    'rows': 3,
                    'required': True,
                }
            ),
            'price': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'id': 'price',
                    'step': '0.01',
                    'placeholder': 'Enter price',
                    'required': True,
                }
            ),
            'chef': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'id': 'chef',
                    'placeholder': 'Enter chef name',
                }
            ),
            'image_url': forms.URLInput(
                attrs={
                    'class': 'form-control',
                    'id': 'image',
                    'placeholder': 'Enter image URL',
                }
            ),
        }

    def __init__(self, *args, **kwargs):
        super(FoodItemForm, self).__init__(*args, **kwargs)
        self.fields['image_url'].initial = None
        
    def clean_image_url(self):
        image_url = self.cleaned_data.get('image_url')
        if not image_url: 
            return 'https://t3.ftcdn.net/jpg/02/48/42/64/360_F_248426448_NVKLywWqArG2ADUxDq6QprtIzsF82dMF.jpg'
        return image_url
