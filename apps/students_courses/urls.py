from django.conf.urls import url 
from . import views

urlpatterns = [
 	url(r'^courses$', views.index),
 	url(r'^courses/(?P<id>\d+)/confirm$', views.confirm),
 	url(r'^courses/(?P<id>\d+)/delete$', views.delete),
 	url(r'^courses/create$', views.create)

]