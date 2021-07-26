
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('',include('my_to_do_app.urls')), # urls.py 에서 할 일은 사용자가 ''에 접근했을때 my_to_do_app 이라는 app의 urls.py 파일로 처리를 넘겨주는 부분
    path('admin/', admin.site.urls),
]
