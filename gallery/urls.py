from django.urls import path
from . import views

urlpatterns = [
    # This makes the gallery the "home" of this app
    path('', views.gallery_view, name='gallery'),
]
