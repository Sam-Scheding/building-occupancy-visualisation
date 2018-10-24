from django.shortcuts import render
from django.views import generic
from apps.main.models import Node, AccessPoint, Device
from apps.api.serializers import NodeSerializer, DeviceSerializer, APSerializer # , TreeSerializer
from rest_framework import viewsets
from apps.api.utils import mixins
from rest_framework_csv import renderers
from django.conf import settings
from django.http import HttpResponse
import csv

# /api/node
class NodeView(viewsets.ModelViewSet):

    queryset = Node.objects.all()
    serializer_class = NodeSerializer

# /api/ap
class APView(mixins.PostListMixin, viewsets.ModelViewSet):

    queryset = AccessPoint.objects.all()
    serializer_class = APSerializer

# /api/device
class DeviceView(mixins.PostListMixin, viewsets.ModelViewSet):

    queryset = Device.objects.all().order_by('discovered_by')
    serializer_class = DeviceSerializer

# /api/tree
# class TreeView(viewsets.ModelViewSet):

#     queryset = Node.objects.all()
#     serializer_class = TreeSerializer
