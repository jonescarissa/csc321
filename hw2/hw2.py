"BU Student"

# To view the IP configuration, you use the 'ipconfig' command.
'''
PS C:\Users\cj917\Documents\belhavencs\csc321\hw2> ipconfig
Windows IP Configuration


Ethernet adapter VirtualBox Host-Only Network:

   Connection-specific DNS Suffix  . :
   Link-local IPv6 Address . . . . . : fe80::9dd2:4029:8524:b4f%3
   IPv4 Address. . . . . . . . . . . : 192.168.56.1
   Subnet Mask . . . . . . . . . . . : 255.255.255.0
   Default Gateway . . . . . . . . . :

Wireless LAN adapter Local Area Connection* 1:

   Media State . . . . . . . . . . . : Media disconnected
   Connection-specific DNS Suffix  . :

Wireless LAN adapter Local Area Connection* 2:

   Media State . . . . . . . . . . . : Media disconnected
   Connection-specific DNS Suffix  . :

Wireless LAN adapter Wi-Fi:

   Connection-specific DNS Suffix  . : belhaven.edu
   Link-local IPv6 Address . . . . . : fe80::e125:af07:d26f:b632%8
   IPv4 Address. . . . . . . . . . . : 192.168.176.117
   Subnet Mask . . . . . . . . . . . : 255.255.240.0
   Default Gateway . . . . . . . . . : 192.168.176.1

Ethernet adapter vEthernet (Default Switch):

   Connection-specific DNS Suffix  . :
   Link-local IPv6 Address . . . . . : fe80::4d42:ece3:939f:5896%25
   IPv4 Address. . . . . . . . . . . : 172.18.5.81
   Subnet Mask . . . . . . . . . . . : 255.255.255.240
   Default Gateway . . . . . . . . . :
'''
# To view all of the interfaces, I used the netifaces module along the
# the interface module
'''
    def get_interfaces():
   ...:     netifaces.interfaces()
   ...:     return netifaces.interfaces()
   ...: if __name__ == "__main__":
   ...:     print(get_interfaces())
   ...: 
['{050C0F94-AE9C-4D28-8C3E-791560DCE340}', 
'{C9258352-6373-48C6-B248-7A56F5680EF8}', 
'{2495B7B9-6045-4DAB-B369-436DBEA04454}', 
'{5DA139CC-DAD9-482A-855D-82404E2186EA}', 
'{3856EC56-987F-11E9-8E66-806E6F6E6963}', 
'{DA422564-FF77-4F48-A304-CCDA67814578}']
'''

# To view the MAC addresses for each interface, I used the 'ipconfig /all' command
# in the python shell. The MAC addresses are the physical addresses.
'''
PS C:\Users\cj917\Documents\belhavencs\csc321\hw2> ipconfig /all

Windows IP Configuration

   Host Name . . . . . . . . . . . . : DESKTOP-381J2GT
   Primary Dns Suffix  . . . . . . . : 
   Node Type . . . . . . . . . . . . : Mixed
   IP Routing Enabled. . . . . . . . : No
   WINS Proxy Enabled. . . . . . . . : No
   DNS Suffix Search List. . . . . . : belhaven.edu

Ethernet adapter VirtualBox Host-Only Network:

   Connection-specific DNS Suffix  . :
   Description . . . . . . . . . . . : VirtualBox Host-Only Ethernet Adapter
   Physical Address. . . . . . . . . : 0A-00-27-00-00-03
   DHCP Enabled. . . . . . . . . . . : No
   Autoconfiguration Enabled . . . . : Yes
   Link-local IPv6 Address . . . . . : fe80::9dd2:4029:8524:b4f%3(Preferred) 
   IPv4 Address. . . . . . . . . . . : 192.168.56.1(Preferred) 
   Subnet Mask . . . . . . . . . . . : 255.255.255.0
   Default Gateway . . . . . . . . . : 
   DHCPv6 IAID . . . . . . . . . . . : 873070631
   DHCPv6 Client DUID. . . . . . . . : 00-01-00-01-24-F5-AB-3E-3C-18-A0-E0-02-07
   DNS Servers . . . . . . . . . . . : fec0:0:0:ffff::1%1
                                       fec0:0:0:ffff::2%1
                                       fec0:0:0:ffff::3%1
   NetBIOS over Tcpip. . . . . . . . : Enabled

Wireless LAN adapter Local Area Connection* 1:

   Media State . . . . . . . . . . . : Media disconnected
   Connection-specific DNS Suffix  . : 
   Description . . . . . . . . . . . : Microsoft Wi-Fi Direct Virtual Adapter
   Physical Address. . . . . . . . . : 72-BC-10-76-47-1F
   DHCP Enabled. . . . . . . . . . . : Yes
   Autoconfiguration Enabled . . . . : Yes

Wireless LAN adapter Local Area Connection* 2:

   Media State . . . . . . . . . . . : Media disconnected
   Connection-specific DNS Suffix  . :
   Description . . . . . . . . . . . : Microsoft Wi-Fi Direct Virtual Adapter #2
   Physical Address. . . . . . . . . : 72-BC-10-76-42-1F
   DHCP Enabled. . . . . . . . . . . : Yes
   Autoconfiguration Enabled . . . . : Yes

Wireless LAN adapter Wi-Fi:

   Connection-specific DNS Suffix  . : belhaven.edu
   Description . . . . . . . . . . . : Marvell AVASTAR Wireless-AC Network Controller
   Physical Address. . . . . . . . . : 70-BC-10-76-46-1E
   DHCP Enabled. . . . . . . . . . . : Yes
   Autoconfiguration Enabled . . . . : Yes
   Link-local IPv6 Address . . . . . : fe80::e125:af07:d26f:b632%8(Preferred) 
   IPv4 Address. . . . . . . . . . . : 192.168.176.117(Preferred) 
   Subnet Mask . . . . . . . . . . . : 255.255.240.0
   Lease Obtained. . . . . . . . . . : Thursday, October 1, 2020 4:26:39 PM
   Lease Expires . . . . . . . . . . : Thursday, October 1, 2020 8:45:23 PM
   Default Gateway . . . . . . . . . : 192.168.176.1
   DHCP Server . . . . . . . . . . . : 1.1.1.1
   DHCPv6 IAID . . . . . . . . . . . : 108051472
   DHCPv6 Client DUID. . . . . . . . : 00-01-00-01-24-F5-AB-3E-3C-18-A0-E0-02-07
   DNS Servers . . . . . . . . . . . : 208.67.222.222
                                       208.67.220.220
   NetBIOS over Tcpip. . . . . . . . : Enabled

   Connection-specific DNS Suffix  . :
   Description . . . . . . . . . . . : Hyper-V Virtual Ethernet Adapter
   Physical Address. . . . . . . . . : 00-15-5D-F2-F0-0B
   Autoconfiguration Enabled . . . . : Yes
   Link-local IPv6 Address . . . . . : fe80::4d42:ece3:939f:5896%25(Preferred)
   IPv4 Address. . . . . . . . . . . : 172.18.5.81(Preferred)
   Default Gateway . . . . . . . . . :
   DHCPv6 IAID . . . . . . . . . . . : 419435869
   DHCPv6 Client DUID. . . . . . . . : 00-01-00-01-24-F5-AB-3E-3C-18-A0-E0-02-07
                                       fec0:0:0:ffff::2%1
                                       fec0:0:0:ffff::3%1
   NetBIOS over Tcpip. . . . . . . . : Enabled
'''
# To find the MAC address of a given interface, I put the interface into a 
# string and made the word 'interface' equal to it

'''
interface = '{DA422564-FF77-4F48-A304-CCDA67814578}'

In [8]:import netifaces

In [9]: def get_mac(interface):
   ...:     addrs = netifaces.ifaddresses(interface)
   ...:     addrs[netifaces.AF_LINK]
   ...: print(get_mac(interface))
[{'addr': '00:15:5d:20:d3:1c'}]
'''

# To view the IPv4 and IPv6 addresses, I used the 'ipconfig /all' command
'''
PS C:\Users\cj917\Documents\belhavencs\csc321\hw2> ipconfig /all

Windows IP Configuration

   Host Name . . . . . . . . . . . . : DESKTOP-381J2GT
   Primary Dns Suffix  . . . . . . . :
   Node Type . . . . . . . . . . . . : Mixed
   IP Routing Enabled. . . . . . . . : No
   WINS Proxy Enabled. . . . . . . . : No
   DNS Suffix Search List. . . . . . : belhaven.edu

Ethernet adapter VirtualBox Host-Only Network:

   Connection-specific DNS Suffix  . :
   Description . . . . . . . . . . . : VirtualBox Host-Only Ethernet Adapter
   Physical Address. . . . . . . . . : 0A-00-27-00-00-03
   DHCP Enabled. . . . . . . . . . . : No
   Autoconfiguration Enabled . . . . : Yes
   Link-local IPv6 Address . . . . . : fe80::9dd2:4029:8524:b4f%3(Preferred)
   IPv4 Address. . . . . . . . . . . : 192.168.56.1(Preferred) 
   Subnet Mask . . . . . . . . . . . : 255.255.255.0
   Default Gateway . . . . . . . . . : 
   DHCPv6 IAID . . . . . . . . . . . : 873070631
   DHCPv6 Client DUID. . . . . . . . : 00-01-00-01-24-F5-AB-3E-3C-18-A0-E0-02-07
   DNS Servers . . . . . . . . . . . : fec0:0:0:ffff::1%1
                                       fec0:0:0:ffff::2%1
                                       fec0:0:0:ffff::3%1
   NetBIOS over Tcpip. . . . . . . . : Enabled

Wireless LAN adapter Local Area Connection* 1:

   Media State . . . . . . . . . . . : Media disconnected
   Connection-specific DNS Suffix  . : 
   Description . . . . . . . . . . . : Microsoft Wi-Fi Direct Virtual Adapter
   Physical Address. . . . . . . . . : 72-BC-10-76-47-1F
   DHCP Enabled. . . . . . . . . . . : Yes
   Autoconfiguration Enabled . . . . : Yes

Wireless LAN adapter Local Area Connection* 2:

   Media State . . . . . . . . . . . : Media disconnected
   Connection-specific DNS Suffix  . : 
   Description . . . . . . . . . . . : Microsoft Wi-Fi Direct Virtual Adapter #2
   Physical Address. . . . . . . . . : 72-BC-10-76-42-1F
   DHCP Enabled. . . . . . . . . . . : Yes
   Autoconfiguration Enabled . . . . : Yes

Wireless LAN adapter Wi-Fi:

   Connection-specific DNS Suffix  . : belhaven.edu
   Description . . . . . . . . . . . : Marvell AVASTAR Wireless-AC Network Controller
   Physical Address. . . . . . . . . : 70-BC-10-76-46-1E
   DHCP Enabled. . . . . . . . . . . : Yes
   Autoconfiguration Enabled . . . . : Yes
   Link-local IPv6 Address . . . . . : fe80::e125:af07:d26f:b632%8(Preferred)
   IPv4 Address. . . . . . . . . . . : 192.168.176.117(Preferred) 
   Subnet Mask . . . . . . . . . . . : 255.255.240.0
   Lease Obtained. . . . . . . . . . : Thursday, October 1, 2020 5:53:28 PM
   Lease Expires . . . . . . . . . . : Thursday, October 1, 2020 9:58:16 PM
   Default Gateway . . . . . . . . . : 192.168.176.1
   DHCP Server . . . . . . . . . . . : 1.1.1.1
   DHCPv6 IAID . . . . . . . . . . . : 108051472
   DHCPv6 Client DUID. . . . . . . . : 00-01-00-01-24-F5-AB-3E-3C-18-A0-E0-02-07
   DNS Servers . . . . . . . . . . . : 208.67.222.222
                                       208.67.220.220
                                       8.8.8.8
   NetBIOS over Tcpip. . . . . . . . : Enabled

Ethernet adapter vEthernet (Default Switch):

   Connection-specific DNS Suffix  . :
   Description . . . . . . . . . . . : Hyper-V Virtual Ethernet Adapter
   Physical Address. . . . . . . . . : 00-15-5D-F2-F0-0B
   DHCP Enabled. . . . . . . . . . . : No
   Autoconfiguration Enabled . . . . : Yes
   Link-local IPv6 Address . . . . . : fe80::4d42:ece3:939f:5896%25(Preferred)
   IPv4 Address. . . . . . . . . . . : 172.18.5.81(Preferred)
   Subnet Mask . . . . . . . . . . . : 255.255.255.240
   Default Gateway . . . . . . . . . :
   DHCPv6 IAID . . . . . . . . . . . : 419435869
   DHCPv6 Client DUID. . . . . . . . : 00-01-00-01-24-F5-AB-3E-3C-18-A0-E0-02-07
   DNS Servers . . . . . . . . . . . : fec0:0:0:ffff::1%1
                                       fec0:0:0:ffff::2%1
                                       fec0:0:0:ffff::3%1
   NetBIOS over Tcpip. . . . . . . . : Enabled
'''

#The IPv4 and IPv6 Addresses. 
'''
In [18]: def get_ips(interface):
    ...:     netifaces.AF_INET
    ...:     netifaces.AF_INET6
    ...: print(get_ips(interface))
None
'''

# To view the IPv4 and IPv6 netmasks, I used 'ipconfig' 
'''
Windows IP Configuration


Ethernet adapter VirtualBox Host-Only Network:

   Connection-specific DNS Suffix  . : 
   Link-local IPv6 Address . . . . . : fe80::9dd2:4029:8524:b4f%3
   IPv4 Address. . . . . . . . . . . : 192.168.56.1
   Subnet Mask . . . . . . . . . . . : 255.255.255.0
   Default Gateway . . . . . . . . . :

Wireless LAN adapter Local Area Connection* 1:

   Media State . . . . . . . . . . . : Media disconnected
   Connection-specific DNS Suffix  . : 

Wireless LAN adapter Local Area Connection* 2:

   Media State . . . . . . . . . . . : Media disconnected
   Connection-specific DNS Suffix  . :

Wireless LAN adapter Wi-Fi:

   Connection-specific DNS Suffix  . : belhaven.edu
   Link-local IPv6 Address . . . . . : fe80::e125:af07:d26f:b632%8
   IPv4 Address. . . . . . . . . . . : 192.168.176.117
   Subnet Mask . . . . . . . . . . . : 255.255.240.0
   Default Gateway . . . . . . . . . : 192.168.176.1

Ethernet adapter vEthernet (Default Switch):

   Connection-specific DNS Suffix  . :
   Link-local IPv6 Address . . . . . : fe80::4d42:ece3:939f:5896%25
   IPv4 Address. . . . . . . . . . . : 172.18.5.81
   Subnet Mask . . . . . . . . . . . : 255.255.255.240
   Default Gateway . . . . . . . . . :
'''

# The netmask of an iterfaces 
'''







    
 