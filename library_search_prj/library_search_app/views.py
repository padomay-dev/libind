import math

from django.shortcuts import render, redirect
from django.db.models import Count
from django.template.context_processors import csrf
from django.core.paginator import Paginator
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.http import HttpResponse, JsonResponse
from django.views.generic import DetailView
from datetime import datetime
from library_search_app.models import *

def main_page(request):
    args = {}
    return render(request, 'main.html', args)

def introduce_page(request):
    return render(request, 'introduce.html')

def login_page(request):
    args = {}
    return render(request, 'login.html', args)

def search_page(request):
    args = {}
    return render(request, 'search.html', args)