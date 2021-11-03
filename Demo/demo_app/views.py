from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from Demo.demo_app.custom_pagination import CustomPagination
from Demo.demo_app.models import Demo
from Demo.demo_app.serializers import SerializerDemo


class DemoView(viewsets.ModelViewSet):
    serializer_class = SerializerDemo
    queryset = Demo.objects.all()
    pagination_class = CustomPagination
