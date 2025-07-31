
from django.urls import path

from . import views
from django.template.context_processors import request

app_name = 'users'


urlpatterns = [
    path('', views.user_list, name="list"),
    path('register/', views.register_view, name="register"),
    path('login/', views.login_view, name="login"),
    path('logout/', views.logout_view, name="logout")
]
