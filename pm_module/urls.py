from django.conf.urls import include, url

from pm_module import views

urlpatterns = [
    url(r'^$', views.index, name='homepage'),
    url(r'^project/create/', views.create_project, name='create_project'),
    url(r'^project/edit/(?P<pk>[0-9]+)/$', views.edit_project, name='edit_project'),
    url(r'^project/delete/(?P<pk>[0-9]+)/$', views.delete, name='delete_project'),
]
