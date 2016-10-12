from django.conf.urls import url, include
from . import views
urlpatterns = [
	#url(r'^signup/$', views.signup, name='signup'),
	url(r'^$', views.index, name='index'),
	
]
 
