from django.http import HttpResponseRedirect
from django.contrib import auth 
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse
from django.http.response import HttpResponseRedirect
from ordersystem.models import Customer
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView # 오브젝트를 생성하는 뷰 (form 혹은 model과 연결되서 새로운 데이터를 넣을 때 CreateView - generic view를 사용)
# from django.contrib.auth.forms import UserCreationForm  >>  장고의 기본 회원가입 폼 (ID, PW만 확인한다 - 뒤에서 이메일 추가 커스터미아징 예정)
#from .forms import CreateUserForm # 장고의 기본 회원가입 폼을 커스터마이징 한 폼
from django.urls import reverse_lazy # generic view에서는 reverse_lazy를 사용한다.

def index(request):
    return render(request,'index.html')

def signup(request):
    if request.method=="POST":
        userform = UserCreationForm(request.POST)
        if userform.is_valid():
            userform.save() 
            return HttpResponseRedirect(
                    reverse("signup_done")
                )
    elif request.method=="GET": 
        userform = UserCreationForm()
    
    return render(request,"registration/signup.html",{
            "userform":userform,
        })   

class RegisteredView(TemplateView): # generic view중에 TemplateView를 상속받는다.
    template_name = 'registration/signup_done.html' # 템플릿은?
    