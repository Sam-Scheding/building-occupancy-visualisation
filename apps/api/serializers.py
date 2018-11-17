from rest_framework import serializers
from apps.main.models import Node, Device, AccessPoint

class NodeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Node
        fields = ['mac_address', 'name']


class DeviceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Device
        fields = ['discovered_by', 'mac_address', 'age', 'vendor', 'time',]

class APSerializer(serializers.ModelSerializer):

    class Meta:
        model = AccessPoint
        fields = [
            'discovered_by',
            'mac_address',
            'signal_strength',
            'channel',
            'ssid',
            'age',
            'signal_to_noise_ratio',
            'time',

        ]

# class TreeSerializer(serializers.ModelSerializer):

#     aps = APSerializer(source='accesspoint_set', many=True)
#     devices = DeviceSerializer(source='device_set', many=True)

#     class Meta:
#         model = Node
#         fields = ['mac_address', 'name', 'aps', 'devices']
