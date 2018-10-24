from django.shortcuts import render
from django.views import generic
# from django.views.generic import edit
from apps.main.models import Node, Device, AccessPoint
from apps.core import views
from django.conf import settings

class HomeView(generic.TemplateView, views.BaseView):

    template_name = 'index.html'

    page_title = "Overview"

    """
        @Deprecated
        This method makes 2*n + 1 calls to the DB where n is the number of nodes in the DB
        It's slow af.
        Instead, send a HTTP query to /api/tree. It get's the same information and is completed
        in a single DB query
    """
    def nodes(self):
        nodes = Node.objects.all()
        for node in nodes:
            node.aps = AccessPoint.objects.filter(discovered_by=node)
            node.devices = Device.objects.filter(discovered_by=node)
        return nodes

    def maps_api_key(self):
        return settings.GOOGLE_MAPS_API_KEY
