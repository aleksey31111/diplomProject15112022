from django import forms
from .models import Crafts


class CraftForm(forms.ModelForm):
    class Meta:
        model = Crafts
        fields = ['title', 'description', 'image', 'url']
        labels = {'title': 'Title', 'description': 'Descripton', 'image': 'Image', 'url': 'Url', }
