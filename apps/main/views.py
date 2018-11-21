from django.shortcuts import render
from django.views import generic
# from django.views.generic import edit
from apps.main.models import Node, Device, AccessPoint
from apps.core import views
from django.conf import settings
from django.db.models import Max, Min, Count
import datetime

class HomeView(generic.TemplateView, views.BaseView):

    template_name = 'index.html'
    page_title = "Overview"

    def count_devices(self):
        cutoff_time = datetime.datetime.now() - datetime.timedelta(minutes=3)
        live_devices = Device.objects.filter(time__gt=cutoff_time).values('mac_address')
        distinct_live_devices = live_devices.distinct()
        for dev in distinct_live_devices:
            print(dev)
        return len(distinct_live_devices)

    def nodes(self):
        nodes = Node.objects.all().order_by('name')
        for node in nodes:
            cutoff_time = datetime.datetime.now() - datetime.timedelta(hours=1)

            aps = AccessPoint.objects.filter(discovered_by=node).values_list('mac_address', flat=True).distinct()
            node.aps = []
            for mac in aps:
                detections = AccessPoint.objects.filter(mac_address=mac, time__gt=cutoff_time).order_by('-time')
                if detections:
                    ap = detections.first()
                    ap.detections = len(detections)
                    node.aps += [ap]


            devices = Device.objects.filter(discovered_by=node).values_list('mac_address', flat=True).distinct()
            node.devices = []

            cutoff_time = datetime.datetime.now() - datetime.timedelta(minutes=3)

            for mac in devices:
                detections = Device.objects.filter(mac_address=mac, time__gt=cutoff_time).order_by('-time')
                if detections:
                    device = detections.first()
                    device.detections = len(detections)
                    node.devices += [device]

        return nodes

    def maps_api_key(self):
        return settings.GOOGLE_MAPS_API_KEY
