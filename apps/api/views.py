from django.shortcuts import render
from django.views import generic
from apps.main.models import Node, AccessPoint, Device
from apps.api.serializers import NodeSerializer, DeviceSerializer, APSerializer # , TreeSerializer
from rest_framework import viewsets
from apps.api.utils import mixins
from django.conf import settings
from django.http import HttpResponse
import datetime

# /api/node
class NodeView(viewsets.ModelViewSet):

    queryset = Node.objects.all()
    serializer_class = NodeSerializer

# /api/ap
class APView(mixins.PostListMixin, viewsets.ModelViewSet):

    # queryset = AccessPoint.objects.all()
    serializer_class = APSerializer

    def get_queryset(self):

        now = datetime.datetime.now()
        ten_minutes_ago = now - datetime.timedelta(minutes=10)
        devices = Device.objects.order_by('discovered_by', 'time').filter(time__range=(ten_minutes_ago, now))
        return devices

# /api/device
class DeviceView(mixins.PostListMixin, viewsets.ModelViewSet):

    # queryset = Device.objects.all().order_by('discovered_by')
    serializer_class = DeviceSerializer

    def get_queryset(self):

        now = datetime.datetime.now()
        then = now - datetime.timedelta(minutes=30)
        aps = AccessPoint.objects.order_by('discovered_by', 'time').filter(time__range=(then, now))
        return aps

# /api/tree
# class TreeView(viewsets.ModelViewSet):

#     queryset = Node.objects.all()
#     serializer_class = TreeSerializer
