from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.conf.urls import url
from django.conf import settings
from . import views


urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('contact/', views.contact_us, name='contact_us'),
    path('activate/<uidb64>/<token>/', views.activate_account, name='activate_account'),
]