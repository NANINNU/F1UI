from django.urls import path

from . import views
from .views import show_example_wikipedia_page


urlpatterns = [
    path("", views.index, name="constructors"),
    path("wikipedia-example", show_example_wikipedia_page, name='wikipedia_example')
]