from django.conf.urls import url
from buttons import views

urlpatterns = [
    url(r'^$', views.button, name='button'),
    url(r'^button', views.button, name='button'),
]