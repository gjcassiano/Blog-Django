from django.conf.urls import url

from . import views

urlpatterns = [
 	#url(r'^buscar$', views.formulario_buscar, name='formulario_buscar'),
   	#url(r'^mostrar$', views.formulario_mostrar, name='formulario_mostrar'),
   	url(r'^login.html', views.login, name='login.html'),
   	url(r'^$', views.posts, name='posts'),

   	#url(r'^$', views.index, name='index'),
   
]