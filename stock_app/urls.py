"""Defines URL patterns for stock_app"""

from django.urls import path
from . import views

app_name = 'stock_app'
urlpatterns = [
	#Home Page
	path('', views.index, name='index'),
]
