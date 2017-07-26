#!/usr/bin/env python
import nmap
ns = nmap.PortScanner()


#input IP to scan, ports, flags
ns.scan('192.168.1.1','1-1024',)


print ns.scaninfo()
print ns.scanstats()
#Print machine state
print ns['192.168.1.1'].state()
#Print active protocols
print ns['192.168.1.1'].all_protocols()
#Print open ports
print ns['192.168.1.1']['tcp'].keys()
