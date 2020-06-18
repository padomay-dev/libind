from django import forms
from django.contrib import admin
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from library_search_app.models import Boards


class BoardsForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget(), label=False)

    class Meta:
        model = Boards
        fields = ['content']
