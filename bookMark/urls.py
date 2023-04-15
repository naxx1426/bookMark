"""
URL configuration for bookMark project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path,include
from user import views

from it_drf_utils.router_builder import RouterBuilder
from it_drf_utils.auth import ITTokenRefreshView, ITTokenObtainPairView

from bookmark.views import BookMarkView

router = RouterBuilder(trailing_slash=False)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('retrieve/', views.retrieve, name='retrieve'),
    path('send_email/', views.send_email, name='send_email'),
    path('check_token_validity/', views.check_token_validity, name='check_token_validity'),
    path('refreshtoken/', views.refresh_token, name='refresh_token'),
    path("", include(router.urls)),
    path("", include(router.url_patterns)),
    path('bookmark/', BookMarkView.default, name='bookmark'),
]
