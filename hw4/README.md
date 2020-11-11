1. Get the domain names:
    cat domains.tsv | tail -n + 2| cut -f 2 >> domains.txt

2. Find the servers of the IP addresses:
    cat domains.txt| while read name; do host ${name}; done| cut -d ' ' -f 4| while read ip; do host ${ip}; done| awk '{print $5}' >> servers_of_ip4.txt

3. Put the servers and IP addresses:
    cat servers_of_ip4.txt| while read name; do host ${name}; done| awk '{print $1}' >> servers_and_ip.txt

4. Put the domains and IP addresses:
    cat domains_and_addresses.txt| awk '{print $1, $4}' >> domain_and_ip4.txt

5. Put everything into a graph on excel -> domains_servers_ip.csv