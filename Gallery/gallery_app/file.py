from django import forms
from .models import Gallery

class FileForm(forms.ModelForm):
    class Meta:
        model = Gallery
        fields = ['image']
        widgets = {'image': forms.ClearableFileInput(attrs={'class': 'file_uploader', 'name': 'file_uploader'})}