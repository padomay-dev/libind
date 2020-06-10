import math
from django.contrib import auth
from django.shortcuts import render, redirect
from django.db.models import Count
from django.template.context_processors import csrf

from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.http import HttpResponse, JsonResponse
from django.views.generic import DetailView
from datetime import datetime
from library_search_app.models import *

def main(request):
    return render(request, 'main.html')


def introduce(request):
    return render(request, 'introduce.html')

def login(request):
    if request.method == "POST":
        user_id = request.POST["user_id"]
        password = request.POST["password"]
        user = auth.authenticate(request, user_id=user_id, password = password)

        if user is not None:
            auth.login(request, user)
            return redirect('main')
        else:
            args = {}
            args.update({"msg": "가입하지 않은 아이디이거나, 잘못된 비밀번호입니다."})
            print(args["msg"])
            return render(request, 'login.html', args)
    return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('main')

def user_register(request):
    return render(request, 'user_register.html')

def user_register_idcheck(reuqest):
    if reuqest.method == "POST":
        user_id = reuqest.POST['user_id']
    else:
        user_id = ''

    try:
        user = User.objects.get(user_id=user_id)
    except:
        user = None
    if user is None:
        overlap = "pass"
    else:
        overlap = "fail"
    context = {'overlap': overlap}

    return JsonResponse(context)


def user_register_result(request):
    if request.method == "POST":
        user_id = request.POST['user_id']
        password = request.POST['password']
        last_name = request.POST['last_name']
        phone = request.POST['phone_number']
        email = request.POST['email']
        if request.POST['birth_year'] != '' and request.POST['birth_month'] != '' and request.POST['birth_day'] != '':
            birth_year = int(request.POST['birth_year'])
            birth_month = int(request.POST['birth_month'])
            birth_day = int(request.POST['birth_day'])

    try:
        date_of_birth = datetime(birth_year, birth_month, birth_day)
    except:
        date_of_birth = None

    try:
        if user_id and User.objects.filter(user_id=user_id).count() == 0:
            user = User.objects.create_user(
                user_id, password, last_name, email, phone, date_of_birth
            )
            auth.login(request, user)
            redirection_page = '/library_search/user_register_done/'
        else:
            redirection_page = '/library_search/error/'
    except:
        redirection_page = '/library_search/error/'

    return redirect(redirection_page)

def user_register_done(request):
    return render(request,  'user_register_done.html')

@login_required
def profil(request):
    user = request.user
    print(str(user.date_of_birth)[:-6])
    date_birth = datetime.strptime(str(user.date_of_birth)[:-6], '%Y-%m-%d %H:%M:%S')
    args = {}
    print(date_birth.year, date_birth.month, date_birth.day)
    args.update({"birth_year": date_birth.year})
    args.update({"birth_month": date_birth.month})
    args.update({"birth_day": date_birth.day})
    return render(request, 'profil.html', args)

def error(request):
    return render(request, 'error.html')
