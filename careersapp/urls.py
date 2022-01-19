from django.contrib import admin
from django.urls import path
from careersapp import views

urlpatterns = [
    path('',views.home,name='Home'),
    path('form/',views.careersViewSet.as_view() ,name='View'),

    

    ]