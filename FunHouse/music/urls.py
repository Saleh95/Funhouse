__author__ = 'Saleh'
from django.conf.urls import url,include
from .views import IndexView,DetailView,song_download
app_name = 'music'
urlpatterns = [
    url(r'^(?P<pk>\d+)-(?P<slug>[-\w]+)/$', DetailView.as_view(), name='detail'),
    url(r'^(?P<pk>\d+)/download/$', song_download, name='download'),
    url(r'^$',IndexView.as_view(),name='Index')
]
