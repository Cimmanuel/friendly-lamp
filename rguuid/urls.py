from django.urls import path

from .views import RGUUIDView

urlpatterns = [
    path("uuids", RGUUIDView.as_view(), name="uuids"),
]
