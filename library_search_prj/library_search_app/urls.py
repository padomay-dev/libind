from django.urls import path, include
from library_search_app.views import *

urlpatterns = [
    path('', main_page, name = 'main'),
]