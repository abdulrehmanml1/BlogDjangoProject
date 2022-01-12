from . import views
from django.urls import path

urlpatterns = [
    path('', views.home,name='blog-home'),
    path('aboutpage', views.about,name='blog-about'),
]
