from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request,'my_to_do_app/index.html')
    #return HttpResponse("my_to_do_app first page") 단순한 인자로 받은 문자열을 사용자의 화면에 보여 주도록 하는 함수이다.
