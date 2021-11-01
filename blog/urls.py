from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.conf.urls import url
from django.conf import settings
from . import views


urlpatterns = [
    path('', views.article_list, name='all_articles'),
    path('<slug:slug>/', views.article_view, name='article_view'),
    path('search/<category>/', views.article_category, name='article_category'),    
]