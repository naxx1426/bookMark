from django.urls import path

from . import views

urlpatterns = [
                path('', views.index, name='index'),
                path('register/', views.register, name='register'),
                path('verify/', views.verify, name='verify'),
                path('send_email/', views.send_email, name='send_email'),
]