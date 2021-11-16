from django.contrib.auth import logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import redirect, render

from django.contrib import auth
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

# django에 이 라이브러리들이 내장되어 있음

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            # cleaned_data: 유효성 검사를 통과한 클린한 데이터
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request=request, username=username, password=password)

            if user is not None:
                login_view(request, user)
            
            return redirect('home')
    else:
        form = AuthenticationForm()
        return render(request, 'login.html', {'form' : form})

def logout_view(request):
    logout(request)
    return redirect("home")


# 회원가입
def signup(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(
                username=request.POST['username'],
                password=request.POST['password1'],
                # email=request.POST['email'],
                )
            auth.login(request, user)
            return redirect('/')
        return render(request, 'signup.html')
    return render(request, 'signup.html')





# from django.shortcuts import render, redirect
# from django.contrib.auth.models import User
# from django.contrib import auth

# from django.views.decorators.csrf import csrf_exempt    # csrf 에러 방지

# from member.models import *


# # # 회원 가입

# @csrf_exempt            # csrf 에러 방지
# def signup(request):    # 회원가입
#     if request.method == 'POST':
#         # password와 confirm에 입력된 값이 같다면
#         # if request.POST['password'] == request.POST['confirm']:
#             # user 객체를 새로 생성
#         user = User.objects.create_user(
#             username=request.POST['cus_name'], password=request.POST['cus_pw'])
#     #     # 로그인 한다
#         auth.login(request, user)
#         # return redirect('/')
#         return render(request, 'home.html')


#     else:
#     # signup으로 GET 요청이 왔을 때, 회원가입 화면을 띄워준다.
#         return render(request, 'signup.html')

# # 로그인


# def login(request):
#     # login으로 POST 요청이 들어왔을 때, 로그인 절차를 밟는다.
#     if request.method == 'POST':
#         # login.html에서 넘어온 username과 password를 각 변수에 저장한다.
#         username = request.POST['username']
#         password = request.POST['password']

#         # 해당 username과 password와 일치하는 user 객체를 가져온다.
#         user = auth.authenticate(request, username=username, password=password)

#         # 해당 user 객체가 존재한다면
#         if user is not None:
#             # 로그인 한다
#             auth.login(request, user)
#             return redirect('/')
#         # 존재하지 않는다면
#         else:
#             # 딕셔너리에 에러메세지를 전달하고 다시 login.html 화면으로 돌아간다.
#             return render(request, 'login.html', {'error': 'username or password is incorrect.'})
#     # login으로 GET 요청이 들어왔을때, 로그인 화면을 띄워준다.
#     else:
#         return render(request, 'login.html')

# # 로그 아웃


# def logout(request):
#     # logout으로 POST 요청이 들어왔을 때, 로그아웃 절차를 밟는다.
#     if request.method == 'POST':
#         auth.logout(request)
#         return redirect('/')

#     # logout으로 GET 요청이 들어왔을 때, 로그인 화면을 띄워준다.
#     return render(request, 'login.html')


def d_mypage_orderlist(request):
    return render(request, 'member/mypage_orderlist.html')

def d_mypage(request):
    return render(request, 'member/mypage.html')