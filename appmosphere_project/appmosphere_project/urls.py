"""
URL configuration for appmosphere_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from enum import auto
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from appmosphere_app.views import ProfilePageViewSet
from appmosphere_app.views import CommentViewSet
from appmosphere_app.views import FeedViewSet
from appmosphere_app.views import MyObtainTokenPairViewSet
from appmosphere_app.views import RegisterViewSet
from rest_framework_simplejwt.views import TokenRefreshView
# from appmosphere_app.views import UserViewSet

 
router = DefaultRouter()
router.register(r'profilepage', ProfilePageViewSet)
router.register(r'comment',CommentViewSet)
router.register(r'feed', FeedViewSet)
router.register(r'register', RegisterViewSet)

urlpatterns = [
    path("", include (router.urls)),
    path("admin/", admin.site.urls),
    path('token/', MyObtainTokenPairViewSet.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),    
]

