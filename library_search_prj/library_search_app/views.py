import math
from django.contrib import auth
from django.shortcuts import render, redirect
from django.db.models import Count
from django.template.context_processors import csrf
from django.contrib.auth.hashers import check_password
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
            args.update({"msg": "가입하지 않은 아이디이거나, 잘못된 패스워드입니다."})
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
    args = {}

    # 프로필 출력시 생년월일여부 체크 및 년월일로 나누어 변환
    if user.date_of_birth != None:
        date_birth = datetime.strptime(str(user.date_of_birth)[:-6], '%Y-%m-%d %H:%M:%S')
        args.update({"birth_year": date_birth.year})
        args.update({"birth_month": date_birth.month})
        args.update({"birth_day": date_birth.day})

    return render(request, 'profil.html', args)

@login_required
def password_change(request):
    args = {}
    if request.method == "POST":
        current_password = request.POST["old_password"]
        user = request.user

        # 현재 패스워드 일치여부 체크
        if check_password(current_password, user.password):
            new_password = request.POST.get("new_password1")
            password_confirm = request.POST.get("new_password2")

            # 새로운패스워드 길이 체크
            print(len(new_password))
            if len(new_password) < 8:
                args.update({"new_password_result" : "패스워드길이는 8글자 이상입니다."})
            else:
                # 새로운 패스워드 바르게 입력했는지 체크
                if new_password == password_confirm:
                    user.set_password(new_password)
                    user.save()
                    auth.login(request, user)
                    url = "/"
                    resp_body = '<script>alert("패스워드 변경이 완료되었습니다.");window.location="%s"</script>' % url
                    return HttpResponse(resp_body)
                else:
                    args.update({"new_password_result" : "패스워드가 일치하지 않습니다."})
        else:
            args.update({'old_password_result':"현재 패스워드가 일치하지 않습니다."})
    return render(request, "password_change.html", args)

def error(request):
    return render(request, 'error.html')
