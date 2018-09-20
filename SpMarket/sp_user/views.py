from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views import View


# 注册
class RegisterView(View):
    def get(self, request):
        pass

    def post(self, request):
        pass


# 登录
class LoginView(View):
    def get(self, request):
        return render(request, 'sp_user/login.html')

    def post(self, request):
        pass


# 个人中心
class CenterView(View):
    def get(self, request):
        pass

    def post(self, request):
        pass


# 收货地址
class AddressView(View):
    def get(self, request):
        pass

    def post(self, request):
        pass


# 个人资料
class InfoView(View):
    def get(self, request):
        pass

    def post(self, request):
        pass


# 退出
class LogoutView(View):
    def get(self, request):
        pass

    def post(self, request):
        pass
