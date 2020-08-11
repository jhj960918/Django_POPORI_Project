from django.shortcuts import render,redirect
from django.contrib.auth import login, authenticate,logout
from .models import CustomUser
from django.http import HttpResponse
# Create your views here.
def signup(request):
    pass

def signout(request):
    logout(request)
    return redirect('index')

def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        login_user = authenticate(username = username, password = password)
        if login_user is not None:
            login(request, login_user)
            return redirect('index')
        else:
            return HttpResponse('로그인안됨 슈퍼유저 만들고 다시시도해봐')
    