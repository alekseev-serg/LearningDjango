from django.urls import path
from todolist.views import *

urlpatterns = [
    path('', todolist, name='todolist'),
    path('chemp/', chemp, name='chemp'),
    path('done/', done_list, name='done_list'),
    path('update/<str:pk>/', done_task, name='done'),
    path('edit/<str:pk>/', edit_task, name='edit'),
    path('recover/<str:pk>/', recover_task, name='recover'),
    path('delete/<str:pk>', delete_task, name='delete'),
]
