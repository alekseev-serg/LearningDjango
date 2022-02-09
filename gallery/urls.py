from django.urls import path
from gallery.views import *


urlpatterns = [
    path('', gallery_index, name='gallery'),
]
