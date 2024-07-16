# -*- coding: utf-8 -*-
"""
Created on Mon Jul  1 15:53:45 2024

@author: buzzs
"""

from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name='Home'),
    path('George', views.George, name='George'),
    path('Interactive', views.Interactive, name='Interactive'),
    path('Myresluger', views.Myresluger, name='Myresluger'),
]
