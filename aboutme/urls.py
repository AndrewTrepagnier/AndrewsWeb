from django.urls import path
from .views import Aboutme

urlpatterns = [
     path("", Aboutme.as_view(), name="aboutme"),
# path('', Aboutme(), name='aboutme_list'),
]