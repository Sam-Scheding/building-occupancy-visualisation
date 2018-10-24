from django.contrib import admin
from apps.main.models import Node, Device, AccessPoint
# Register your models here.
admin.site.register(Node)
admin.site.register(Device)
admin.site.register(AccessPoint)
