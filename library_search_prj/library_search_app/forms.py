from django import forms
from django.contrib import admin
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from library_search_app.models import Boards


class BoardsForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget(), label='')

    class Meta:
        model = Boards
        fields = ['content']


# class BoardsAdmin(admin.ModelAdmin):
#     form = BoardsForm


# admin.site.register(BoardsForm, BoardsAdmin)

# class PostAdminForm(forms.ModelForm):
#     content = forms.CharField(widget=CKEditorUploadingWidget(), label='')

#     class Meta:
#         model = Boards

# # class PostAdmin(admin.ModelAdmin):
# #     form = PostAdminForm


# # admin.site.register(Post, PostAdmin)
