from django.conf.urls import url
from .views import ListEventView, DetailEventView, CreateEventView


urlpatterns = [
    url(r'^$', ListEventView.as_view(), name='list'),
    url(r'^(?P<pk>\d+)/$', DetailEventView.as_view(), name='detail'),
    url(r'^create$', CreateEventView.as_view(), name='create'),
]
