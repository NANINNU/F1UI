from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="rules"),
    path('pdf/', views.serve_pdf, name='serve_pdf'),
]