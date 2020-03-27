import pyshark
import sys

filename = input("Please enter the file name to keep LiveCapture results: ")

cap = pyshark.LiveCapture(interface='eth0')

cap.sniff(packet_count=100)

for pkt in cap:
	sys.stdout = open(filename, 'w')
	print(pkt)
	sys.stdout.close()
