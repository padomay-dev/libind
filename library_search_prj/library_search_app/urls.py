from django.urls import path, include
from library_search_app.views import *

urlpatterns = [
    path('', main_page, name = 'main'),
    path('intoduce', introduce_page, name='introduce'),
    path('login/', login_page, name = 'login'),
    path('search/', search_page, name='search'),

]