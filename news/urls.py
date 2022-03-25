from django.urls import path
from news.views import *


urlpatterns = [
    path('', index_news, name='index_news'),
]
