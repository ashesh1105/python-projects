from django.conf.urls import url
from my_app import views

urlpatterns = [
    url(r'^users/', views.users, name='users'),
    url(r'^help/', views.help, name='help'),
    url(r'^$', views.index, name='index'),
]
