from django.urls import path
from .views import (
  NewsListView,
  StoredNewsListView,
)

urlpatterns = [
  path("", NewsListView.as_view()),  
  path("saved/", StoredNewsListView.as_view()),  
]
