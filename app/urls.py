from django.urls import path,include
from app import views
urlpatterns = [
    path('',views.register,name="register"),
    path('userregister',views.UserRegister,name="userregister"),
    path('login',views.login,name='login'),
    path('loginuser',views.LoginUser,name="loginuser")
]