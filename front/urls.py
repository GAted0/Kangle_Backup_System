from django.urls import path, include
from . import views

app_name = 'user'

urlpatterns = [
    path('', views.index),
    path('index/', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('add_user/', views.add_user, name='add_user'),
    path('del_user/', views.del_user, name='del_user'),
    path('download/', views.download, name='download'),
    path('unzip/', views.unzip, name='unzip'),
]
