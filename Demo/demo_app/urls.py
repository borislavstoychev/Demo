from django.urls import path, include
from Demo.demo_app import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('', views.DemoView, basename='demo')

urlpatterns = [
    path("", include(router.urls)),
]