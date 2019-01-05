from django.urls import path
from . import views
urlpatterns = [
url(r'^$', 'index', name='index'),
url(r'^homepage$', 'homepage', name='homepage'),
]