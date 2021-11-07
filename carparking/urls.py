"""carparking URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from typing import DefaultDict
from django.contrib import admin
from django.db import router
from django.urls import path,include
from rest_framework import viewsets
from rest_framework.routers import DefaultRouter

from api import views


# createing router object
router = DefaultRouter()

# Register UserModelViewset with router

#router.register('user',views.UserModelViewset,basename='user')
#router.register('client',views.ClientModelViewset,basename='client')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('userapi',views.UserAPI.as_view()),
    path('userapi/<int:pk>',views.UserAPI.as_view()),
    path('clientapi',views.ClientAPI.as_view()),
    path('clientapi/<int:pk>',views.ClientAPI.as_view()),
]
