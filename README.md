# Pyshark
Network sniffer via Pyshark

# Install Pyshark
>>> pip3 install pyshark

# LiveCapture(livecap.py)
>>> cap = pyshark.LiveCapture(interface='eth0')
>>> cap.sniff(packet_count=5)
...
