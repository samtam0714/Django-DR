from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^simple/$', views.simple_upload, name='simple_upload'),
    url(r'^form/$', views.model_form_upload, name='model_form_upload'),
    url(r'^abc/$', views.abc, name='abc'),
    url(r'^score/$', views.score, name='score'),
    url(r'^cosimscore/$', views.cosimscore, name='cosimscore'),
]
