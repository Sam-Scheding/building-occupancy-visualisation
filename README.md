# building-occupancy-visualisation

This is a REST API and visualisation web application that plugs in to an implementation of the following research paper:

    http://www.cse.unsw.edu.au/~salilk/comp6733/Crowd.pdf

In short, the research paper describes a way of estimating crowd density by harvesting MAC Address data from WiFI connected devices. Peter Kydd and I implemented a mesh network of Raspberry Pi Zero W nodes that realises an implementation of the research paper. The data from the mesh network is then POSTed to this REST API via a sink node. 

This Web Application receives POST and PATCH requests at the following endpoints:

    "node": "http://samscheding1.pythonanywhere.com/api/node/",
    "device": "http://samscheding1.pythonanywhere.com/api/device/",
    "ap": "http://samscheding1.pythonanywhere.com/api/ap/"
    
The data collected at these endpoints is then interfaced with the Google GeoLocation API and displayed on a Google Map. 
