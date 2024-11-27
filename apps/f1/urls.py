from django.urls import path
from . import views

urlpatterns = [
    path('search/', views.f1_search, name='f1_search'),
]