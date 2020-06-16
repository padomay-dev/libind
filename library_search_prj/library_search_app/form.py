from django import forms
from django.contrib import admin
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from library_search_app.models import Boards


class PostAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget(), label='')

    class Meta:
        model = Boards

# class PostAdmin(admin.ModelAdmin):
#     form = PostAdminForm


# admin.site.register(Post, PostAdmin)
