#!/bin/bash

# Script Name:                  Copy & Append Date and Time
# Author:                       Raphael Chookagian
# Date of latest revision:      05/31/2023
# Purpose:                      Create a bash script that:
# Copies /var/log/syslog to the current working directory
# Appends the current date and time to the filename


# Declare Variables


# current working directory
curr_loki=$(pwd)

# log/file to copy
sys_log="/var/log/syslog"

# where to copy log/file to
# and append date and time to filename
daTime=$(date +"%Y%m%d")
logFile="$curr_loki/syslog_$daTime"

# tell user process has started at date and time
star_Time=$(date +"%Y_%m_%d %H:%M:%S")
echo "[$star_Time] Cloning of system logs has begun"

# copy log to current location
cp "$sys_log" "$logFile"

# let user know system log is being copied
echo "[$star_Time] Cloning in process"




# Declare Functions

# Create

# Main

# End
