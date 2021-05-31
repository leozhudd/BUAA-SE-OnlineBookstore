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

        # todo 判断用户是否存在





def logout(request):
    return HttpResponse("logout")
