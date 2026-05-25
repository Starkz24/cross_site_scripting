from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('nameRef/', views.nameRef, name='nameRef'),
]
