import pyshark
import sys

filename = input("Please enter the file name to keep LiveCapture results: ")

cap = pyshark.LiveCapture(interface='eth0', bpf_filter='udp port 53')

cap.sniff(packet_count=5)

def print_dns_info(pkt):
	if pkt.dns.qry_name:
		print("DNS Request from %s: %s" % (pkt.ip.src, pkt.dns.qry_name))
	elif pkt.dns.resp_name:
		print("DNS Request from %s: %s" % (pkt.ip.src, pkt.dns.resp_name))

for pkt in cap:
	sys.stdout = open(filename, 'w')
	print(pkt)
	sys.stdout.close()
