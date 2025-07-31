from django import forms
from . import models
import bleach
from ckeditor.widgets import CKEditorWidget
from django_bleach.forms import BleachField   # keeps widget but adds cleaning
from django.http import HttpRequest


class CreatePost(forms.ModelForm):
    # content = BleachRichTextField()  # Using our custom field
    content = BleachField(widget=CKEditorWidget())

    class Meta:
        model = models.Post
        fields = ['title', 'content', 'slug', 'banner']

        # widgets = {
        #     'content': CKEditorWidget()
        # }
