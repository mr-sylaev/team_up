from django.conf.urls import url
from .views import HomePageView
from .views import index


urlpatterns = [
    url(r'^$', HomePageView.as_view(), name='home_page'),
    url(r'^$',index,name='reit'),

]
