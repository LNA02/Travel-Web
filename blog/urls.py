from django.urls import path
from . import views


urlpatterns = [
    path('', views.list),
    path('<int:id>/', views.post),
    path('search/', views.search, name='search'),
    path('post/<int:id>/next/', views.next_post, name='next_post'),
]