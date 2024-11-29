from django.urls import path

from . import views as tables_views  # apps.tables.views
from apps.f1 import views as f1_views  # apps.f1.views

urlpatterns = [
    path('f1_search/', f1_views.f1_search, name='f1_search'),  # f1 뷰
    path("", tables_views.datatables, name="datatables"),  # tables 뷰
    path('delete-product/<int:id>/', tables_views.delete_product, name="delete_product"),
    path('update-product/<int:id>/', tables_views.update_product, name="update_product"),
]
