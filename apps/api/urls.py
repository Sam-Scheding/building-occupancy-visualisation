from django.contrib import admin
from django.urls import path, include
from apps.api import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('node', views.NodeView, basename='node')
router.register('device', views.DeviceView, basename='device')
router.register('ap', views.APView, basename='access_point')
# router.register('tree', views.TreeView)

urlpatterns = [
    path('', include(router.urls)),
    # path('csv', views.CSVView.as_view(), name='csv'),

]
