from django.shortcuts import render
from student.models import *


def home(request):
    username = ''
    if request.session.get('username'):
        username = request.session['username']
    message = 'lab3!!!'
    return render(request, 'home.html', {'username': username, 'message': message})


def register(request):
    if request.method == 'POST':
        new_username = request.POST.get('username')
        new_password1 = request.POST.get('password1')
        new_password2 = request.POST.get('password2')
        if new_password2 != new_password1:
            return render(request, 'register.html', {'message': '两次密码不一致'})
        else:
            new_student = Student()
            new_student.name = new_username
            new_student.password = new_password1
            new_student.save()
            return render(request, 'home.html', {'message': '注册成功！'})
    else:
        return render(request, 'register.html', {})


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = Student.objects.get(name=username)
        if user.password == password:
            request.session['username'] = username
            return render(request, 'home.html', {'username': username, 'message': '登陆成功'})
        else:
            return render(request, 'login.html', {'message': '密码错误'})
    else:
        return render(request, 'login.html', {'message': '请登录'})


def logout(request):
    request.session.flush()
    return render(request, 'home.html', {'message': '注销成功'})
