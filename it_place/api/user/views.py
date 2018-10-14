from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework import filters
from apps.users.models import ItUser
from .serializers import  ItUserSerializer
from django_filters.rest_framework import DjangoFilterBackend


class ItUserSetPagination(PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page_size'
    max_page_size = 2


class ItUserViewSet(viewsets.ModelViewSet):
    queryset = ItUser.objects.all()
    serializer_class = ItUserSerializer
    pagination_class = ItUserSetPagination
    filter_fields = ('city', 'skills', 'specialty', 'edu')
    search_fields = ('first_name', 'last_name')
    filter_backends = (filters.SearchFilter, DjangoFilterBackend)
