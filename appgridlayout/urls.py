from django.conf.urls import url
from appgridlayout import views

urlpatterns = [

    url(r'^$', views.index, name='index'),
    url(r'^index', views.index, name='index'),
]