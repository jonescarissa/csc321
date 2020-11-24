# Packet Capture
To get the network traffic using tcpdump:
    - tcpdump -i eth0 -w wuserver.pcap
    - tcpdump -i eth0 -w wuclient.pcap
    - tcpdump -i eth0 -w taskvent.pcap
    - tcpdump -i eth0 -w taskwork.pcap
    - tcpdump -i eth0 -w tasksink.pcap

# Parsing Out Relevant Packets
To mergae all of the packet capture data into one file:
    - mergecap -w full-take.pcap wuserver.pcap wuclient.pcap taskvent.pcap 
        tasksink.pcap taskwork.pcap

To separate the two exercises into two different files:
    For the weather server:
        - tcpdump -n -r full-take.pcap port 5556 -w weather.pcap
    For the task server:
        - tcpdump -n -r full-take.pcap port 5557 and 5558 -w task.pcap

