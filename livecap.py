import pyshark
import sys

filename = input("Please enter the file name to keep LiveCapture results: ")

cap = pyshark.LiveCapture(interface='eth0', bpf_filter='udp port 53')

cap.sniff(packet_count=5)

for pkt in cap:
	sys.stdout = open(filename, 'w')
	print(pkt)
	sys.stdout.close()
