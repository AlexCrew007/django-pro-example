from django.urls import path,include
from app_5 import views


app_name='basic_app'


urlpatterns=[
    path('index',views.index,name='index'),
    path('user_login',views.user_login,name='user_login'),
    path('register',views.register,name="register")
]
