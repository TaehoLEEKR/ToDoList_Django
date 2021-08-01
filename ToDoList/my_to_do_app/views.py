from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import *
# Create your views here.

def index(request):
    todos = Todo.objects.all() # obejcts.all() 함수를 통해 데이터베이스에 모든 데이터를 가져온다 그리고 이를 content에 딕셔너리를 만들어서 todos key에 할당 시킨후 render함수에 마지막에 content
    # 딕셔너리를 함께 전달한다.
    content = {'todos':todos}
    return render(request,'my_to_do_app/index.html',content)
    #return HttpResponse("my_to_do_app first page") 단순한 인자로 받은 문자열을 사용자의 화면에 보여 주도록 하는 함수이다.


def createTodo(request):
    data=request.POST
    user_input_str =  data['todoContent']
    new_todo =Todo(content=user_input_str)
    #models에서 데이터베이스 새로운 데이터를 추가하는 코드 이고 아래 save를 통해 저장한다.
    new_todo.save()
    return HttpResponseRedirect(reverse('index')) # reverse 함수를 통해 index 라는 이름의 url을 찾게 된다
    #return HttpResponse("Create Todo를 할거야! =>" + user_input_str) 새로운페이지에서 데이터베이스에 문자열을 그려준다


def doneTodo(request):
    data = request.GET
    done_todo_id = data['todoNum']
    print("완료한 todo의 id",done_todo_id)
    todo=Todo.objects.get(id=done_todo_id)
    todo.isDone=True
    todo.save()
    return HttpResponseRedirect(reverse('index'))