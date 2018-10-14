from django.conf.urls import url
from .views import LoginView, LogoutView, CreateItUserView, ItUserListView, ItUserDetailView


urlpatterns = [
    url(r'^$', ItUserListView.as_view(), name='list'),
    url(r'^(?P<pk>\d+)/$', ItUserDetailView.as_view(), name='detail'),
    url(r'^login$', LoginView.as_view(), name='login'),
    url(r'^logout$', LogoutView.as_view(), name='logout'),
    url(r'^registration$', CreateItUserView.as_view(), name='registration'),
    # url(r'^update$', UpdateItUserView.as_view(), name='update'),
]
