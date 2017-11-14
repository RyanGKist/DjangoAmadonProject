from django.conf.urls import url
from . import views

urlpatterns = [
	url('^$' , views.index),
	url('^buy$', views.purchase),
	url('^clear$', views.clear),
	url('^return$', views.return_S)
]