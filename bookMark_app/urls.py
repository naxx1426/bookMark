from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
                    path('', views.index, name='index'),
                    path('register/', views.register, name='register'),
                    path('verify/', views.verify, name='verify'),
                ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)