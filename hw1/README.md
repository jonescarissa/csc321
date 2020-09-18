## Datalink
    1.'Four different things are listed: Interface, Internet Address, 
    Physical Address, and Type'
```
  Interface: 192.168.56.1 --- 0x2
  Internet Address      Physical Address      Type
  192.168.56.255        ff-ff-ff-ff-ff-ff     static
  224.0.0.2             01-00-5e-00-00-02     static
  224.0.0.22            01-00-5e-00-00-16     static
  224.0.0.251           01-00-5e-00-00-fb     static
  224.0.0.252           01-00-5e-00-00-fc     static
  239.255.255.250       01-00-5e-7f-ff-fa     static

Interface: 192.168.1.136 --- 0x7
  Internet Address      Physical Address      Type
  192.168.1.1           3c-90-66-8b-ae-51     dynamic
  192.168.1.119         98-5f-d3-b5-b8-ea     dynamic
  192.168.1.255         ff-ff-ff-ff-ff-ff     static
  224.0.0.2             01-00-5e-00-00-02     static
  224.0.0.22            01-00-5e-00-00-16     static
  224.0.0.251           01-00-5e-00-00-fb     static
  224.0.0.252           01-00-5e-00-00-fc     static
  239.255.255.250       01-00-5e-7f-ff-fa     static
  255.255.255.255       ff-ff-ff-ff-ff-ff     static

Interface: 172.18.5.145 --- 0x19
  Internet Address      Physical Address      Type
  172.18.5.159          ff-ff-ff-ff-ff-ff     static
  224.0.0.2             01-00-5e-00-00-02     static
  224.0.0.22            01-00-5e-00-00-16     static
  224.0.0.251           01-00-5e-00-00-fb     static
  239.255.255.250       01-00-5e-7f-ff-fa     static
  255.255.255.255       ff-ff-ff-ff-ff-ff     static
``` 

  2.'I can't really tell if what devices are connected to the network but I can see what companies are connected to the network such as SmartRG, Inc., Microsoft Corporation and Microsoft. So, I'm thinking at the two Microsoft things are my laptop and my Xbox One. I'm thinking the SmartRG, Inc. is the Wifi itself.'
```
  >>> netlayers.arp_table()
    Name  IP               MAC                Company
    ---------------  -----------------  ---------------------
    192.168.56.255   ff:ff:ff:ff:ff:ff
    224.0.0.2        01:00:5e:00:00:02
    224.0.0.22       01:00:5e:00:00:16
    224.0.0.251      01:00:5e:00:00:fb
    224.0.0.252      01:00:5e:00:00:fc
    239.255.255.250  01:00:5e:7f:ff:fa
    192.168.1.1      3c:90:66:8b:ae:51  SmartRG, Inc.
    192.168.1.119    98:5f:d3:b5:b8:ea  Microsoft Corporation
    192.168.1.219    c0:33:5e:ec:33:37  Microsoft
    192.168.1.255    ff:ff:ff:ff:ff:ff
    224.0.0.2        01:00:5e:00:00:02
    224.0.0.22       01:00:5e:00:00:16
    224.0.0.251      01:00:5e:00:00:fb
    224.0.0.252      01:00:5e:00:00:fc
    239.255.255.250  01:00:5e:7f:ff:fa
    255.255.255.255  ff:ff:ff:ff:ff:ff
    172.17.55.255    ff:ff:ff:ff:ff:ff
    224.0.0.2        01:00:5e:00:00:02
    224.0.0.22       01:00:5e:00:00:16
    224.0.0.251      01:00:5e:00:00:fb
    239.255.255.250  01:00:5e:7f:ff:fa
    255.255.255.255  ff:ff:ff:ff:ff:ff
```

## Network

'Ping google.com showed the IP address, the bytes, time and the TTL.'
```
    PS C:\Users\cj917\Documents\belhavencs\csc321\hw1> ping google.com

    Pinging google.com [172.217.0.14] with 32 bytes of data:
    Reply from 172.217.0.14: bytes=32 time=30ms TTL=120
    Reply from 172.217.0.14: bytes=32 time=30ms TTL=120
    Reply from 172.217.0.14: bytes=32 time=34ms TTL=120
    Reply from 172.217.0.14: bytes=32 time=34ms TTL=120

    Ping statistics for 172.217.0.14:
        Packets: Sent = 4, Received = 4, Lost = 0 (0% loss),
    Approximate round trip times in milli-seconds:
        Minimum = 30ms, Maximum = 34ms, Average = 32ms
```

'Ping localhost showed the bytes and the time. Plus localhost was faster.'
```
PS C:\Users\cj917\Documents\belhavencs\csc321\hw1> ping localhost

Pinging DESKTOP-381J2GT [::1] with 32 bytes of data:
Reply from ::1: time<1ms
Reply from ::1: time<1ms
Reply from ::1: time<1ms
Reply from ::1: time<1ms

Ping statistics for ::1:
    Packets: Sent = 4, Received = 4, Lost = 0 (0% loss),
Approximate round trip times in milli-seconds:
    Minimum = 0ms, Maximum = 0ms, Average = 0ms
```