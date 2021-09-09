from django.urls import path
from blog import views

urlpatterns = [
    path('', views.base_page, name='home'),
    path('blog/', views.index_blog, name='index_blog'),
]
