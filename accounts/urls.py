from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('signup/',views.signup,name ='signup'),
    path('logout/',views.logoutacc,name ='logout'),
    path('login/',views.loginacc,name ='login'),
    
]
