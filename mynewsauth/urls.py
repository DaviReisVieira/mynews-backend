from django.urls import path, include
from .views import AzureLoginView, GoogleLoginView

urlpatterns = [
  path("google/", GoogleLoginView.as_view(), name = "google"),
  path("azure/", AzureLoginView.as_view(), name = "azure"),
]