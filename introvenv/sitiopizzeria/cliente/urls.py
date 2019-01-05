from django.urls import path
from . import views
urlpatterns = [
url(r'^$', 'index', name='index'),
url(r'^cliente$', 'cliente', name='cliente'),
]