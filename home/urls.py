from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index),
    path('contact/', views.contact),
    path('blog/', views.blog),
    path('register/', views.register, name='register'),
    path('login/', views.Login ,name='login'),
    path('logout/', views.Logout, name='logout'),
    path("add_blog/", views.add_blogs, name="add_blog"),
]