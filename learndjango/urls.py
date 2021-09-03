from django.urls import path
from learndjango import views

urlpatterns = [
    path('', views.index)
]
