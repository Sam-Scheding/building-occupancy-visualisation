from django.db import models

"""
    Node is a Pi Zero. Each time one of these is found, we want to display it
    as a map marker
"""
class Node(models.Model):

    # A human readable name for the node
    name = models.CharField(max_length=30, default='Pi Zero')
    mac_address = models.CharField(max_length=30, primary_key=True)


"""
    AccessPoint is a WiFi Router. Each Pi Zero will be aware of 0 or more of these
    When they discover a new one, they feed that information to the mesh network sink
    which then makes a PUT request to instantiate an instance of this model.

    This data is used to geo-locate the Pi Zeros
"""
class AccessPoint(models.Model):

    discovered_by = models.ForeignKey(Node, on_delete=models.CASCADE)
    mac_address = models.CharField(max_length=18, primary_key=True)  # The MAC address of the WiFi node. It's typically called a BSS, BSSID or MAC address.
    signal_strength = models.IntegerField()  # The current signal strength measured in dBm.
    age = models.IntegerField(default=0)  # The number of milliseconds since this access point was detected.
    channel = models.IntegerField()  # The channel over which the client is communicating with the access point.
    signal_to_noise_ratio = models.IntegerField()  #  The current signal to noise ratio measured in dB. e.g. Signal Strength - Noise floor = SNR
    ssid = models.CharField(max_length=50)
    vendor = models.CharField(max_length=60)

"""
    Device is a WiFi enabled devices that are used to identify people. The Pi Zeros
    discover new Devices and feed that information to the mesh network sink. The
    sink node then makes a PUT request to this webapp that instantiates an instance
    of this model.

    This data is displayed on the Map and is associated with each Node Model.
"""
class Device(models.Model):

    discovered_by = models.ForeignKey(Node, on_delete=models.CASCADE)
    mac_address = models.CharField(max_length=18, primary_key=True)
    age = models.IntegerField(default=0)
    vendor = models.CharField(max_length=60, blank=True)
