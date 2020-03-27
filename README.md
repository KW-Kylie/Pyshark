# Pyshark
Network sniffer via Pyshark

# Install Pyshark
$ pip3 install pyshark

# LiveCapture(livecap.py)
Capture basic info from live interface 
$ cap = pyshark.LiveCapture(interface='eth0')
$ cap.sniff(packet_count=5)
...
