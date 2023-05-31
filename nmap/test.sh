#!/bin/bash

# Script Name:                  GitHub
# Author:                       Raphael Chookagian
# Date of latest revision:      05/10/2023
# Purpose:                      scripts I put together for 301d8 lab 02 for nmap commands

# Declare Variables
# Declare Functions
# Create
# Main

# host discovery
# sudo nmap -sn <target IP range>
# sudo nmap -sn 192.168.1.102 # <-- For Kali VM 05.31.2023

# host discovery and output to file
sudo nmap -sn 192.168.1.102 >> ~/Desktop/scan_Output.txt

# Perform a fast, aggressive scan of the network.
sudo nmap -T4 -A 192.168.1.102 >> ~/Desktop/scan_Output.txt

# Scan the 1000 most common ports on each host on the network.
sudo nmap -p- --top-ports 1000 192.168.1.102 >> ~/Desktop/scan_Output.txt

# Perform an intense scan on all hosts on the network.
sudo nmap -T4 -p- 192.168.1.102 >> ~/Desktop/scan_Output.txt

# Perform a slow, comprehensive scan on all hosts on the network.
sudo nmap -T2 -p- 192.168.1.102 >> ~/Desktop/scan_Output.txt

# (Windows10) From a terminal prompt, run a netstat command that shows all active ports.
netstat -ano # ano displays active connections and listening ports

# on a specific IP or machine/target
# netstat -ano -a -n <target IP/hostname>

# Run a netstat command that displays the routing table.
netstat -r # -r flag displays routing table

# Run a netstat command that only displays connections for the TCP protocol.
# -p tcp tells "netstat" to filter and display only TCP connections.
netstat -ano -p tcp 





# End
