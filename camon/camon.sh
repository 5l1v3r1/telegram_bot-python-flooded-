#!/bin/bash
ip="wget -O - -q icanhazip.com"
$ip  > /home/ignat/bot_serv/camon/ip.txt
cat ip.txt port.txt > /home/ignat/bot_serv/camon/ip_port.txt
command sed -e ':a;N;$!ba;s/\n//g' /home/ignat/bot_serv/camon/ip_port.txt > /home/ignat/bot_serv/camon/logfile.txt

