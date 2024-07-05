# pages/urls.py
from django.urls import path
from .views import Viewofaboutme1

urlpatterns = [
    path("", Viewofaboutme1.as_view(), name="aboutme"),
]