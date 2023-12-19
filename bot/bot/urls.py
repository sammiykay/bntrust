"""bot URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib.auth import views as auth_views
from django.contrib import admin
from django.urls import path,include
from bn.views import *
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('balance_list', BalanceList, basename='articles')
router.register('bybit_list', BybitList, basename='dwd')

router.register('popip', PopIpUser, basename='pop33')
router.register('popemail', PopUsers, basename='pop')
urlpatterns = [
    path('admin/', admin.site.urls),
    path('donna/', donna_users),
    path('mohammed/', mohammed_users),
    path('guest/', guest_users),
    path('bentley/', create_m),
    path('guest_create/', create_g),
    path('donna_create/', create_d),
    path('delete_guest/', delete_g),
    path('delete_g/', delete_d),
    path('create-key/', create_email),
    path('create-license/', create_key),
    path('login-license/', login_page),
    path('delete/<str:id>/', delete_email),
    path('delete-license/<str:id>/', delete_key),
    path('api/', include(router.urls)),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name ='login'),
]

