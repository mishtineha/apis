from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url
from django.conf.urls.static import static
from rest_framework import routers
from . import views
from app.views import *
"""
router = routers.DefaultRouter()
router.register('',ProfileViewSet)"""
urlpatterns = [
    path(r'app/',ProfileAPIView.as_view()),
    path(r'list/',ProfileAPIView2.as_view()),
    path(r'register/',CreateUserView.as_view()),
    path('auth/login/',LoginView.as_view()),
    path('auth/logout/',LogoutView.as_view()),
    path('address/',Addressview.as_view()),
    path('companyaddress/',Company_addressview.as_view())
    #url(r'app/',views.ProfileAPIView),
]
