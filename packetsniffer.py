import subprocess
import time
import logging

logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
logging.getLogger("scapy.loading").setLevel(logging.ERROR)
logging.getLogger("scapy.interactive").setLevel(logging.ERROR)

try:
	from scapy.all import *
except ImportError:
	sys.exit()

interface = 'eth0'
subprocess.call(["ifconfig",interface,"promisc"],stdout=None,stderr=None,shell=False)
print 'Interface has been set to Promiscous mode'

totalpackets=0
sniffingtime=86400
protocols=0
infinite=1

def timenow():
	currenttime=time.strftime("%m%d%y-%H%M%S")
	return currenttime
	
def export():
	p = sniff(iface='eth0',timeout=sniffingtime,count=0)
	wrpcap('/home/debian/Desktop/pcaps/' + timenow() + '.pcap',p);

while infinite==1 :
	export()

