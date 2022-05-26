from django.urls import path
from log_parser.views import *


urlpatterns = [
    path('', log_parser_index, name='log_parser'),
]
