from django import forms
from .models import Gallery


class GalleryForm(forms.ModelForm):
    class Meta:
        model = Gallery
        fields = ['description']
        widgets = {
            'description': forms.TextInput(attrs={'class': 'description', 'placeholder': 'Description...'}),
        }