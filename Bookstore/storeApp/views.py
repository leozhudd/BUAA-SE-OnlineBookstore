from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'index.html')


def login(request):
    return HttpResponse("login!")


def register(request):
    # 如果用户提交了注册表单：
    if request.method == 'POST':
        new_username = request.POST.get('username')
        new_password1 = request.POST.get('password1')
        new_password2 = request.POST.get('password2')

        # 如果用户已经存在
        if User.objects.filter(username=new_username):
            return render(request, 'register.html', {'message': '用户已存在！'})
        if new_password1 != new_password2:
            return render(request, 'register.html', {'message' '两次密码不一致！'})
        else:
            new_user = User()
            new_user.username = new_username
            new_user.password = new_password1
            new_user.sava()
            return render(request, 'index.html', {'message': '注册成功！'})
    else:
        return render(request, 'register.html', {})


def login(request):
    


def logout(request):
    return HttpResponse("logout")

