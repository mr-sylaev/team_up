"""it_place URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from settings import dev as settings

urlpatterns = [
    # contrib
    url(r'^admin/', admin.site.urls),

    # apps
    url(r'^user/', include('apps.users.urls', namespace='user')),
    url(r'^events/', include('apps.events.urls', namespace='event')),
    url(r'^projects/', include('apps.projects.urls', namespace='projects')),

    # rest-api
    url(r'^rest-api/', include('api.urls')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # main
    url(r'^', include('apps.main.urls', namespace='main')),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
