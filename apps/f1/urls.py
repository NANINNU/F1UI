from django.urls import path
from . import views

urlpatterns = [
    path('search/', views.f1_search, name='f1_search'),  # F1 검색 페이지
    # path('autocomplete/', views.autocomplete, name='autocomplete'),  # 자동완성 API
]
