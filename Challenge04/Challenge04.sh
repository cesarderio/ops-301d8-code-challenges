#!/bin/bash

# Script Name:                  Copy & Append Date and Time
# Author:                       Raphael Chookagian
# Date of latest revision:      06/05/2023
# Purpose:                      Create a bash script that backs up and clears the log


# Declare Variables

daTime=$(date +"%Y%m%d")

backItUp="/Desktop"

# Declare Functions

# print file size
fSize() {
  file="$1"
  size=$(du -h "$file" | awk '{print $1}')
  echo "File: $file, Size: $size"
  }

# Function to compress and backup the file
compBack() {
  file="$1"
  filename=$(basename "$file")
  back_Ups="${backItUp}/${filename}-$daTime.tar.gz"
  tar -czf "$back_Ups" "$file"
  echo "Logs backups: $file to $back_Ups"
    
  # clear contents of log file
  echo "" > "$file"
  echo "$file has been cleared."
    
  # Print the file sizes
  ogSize=$(du -h "$file" | awk '{print $1}')
  comp_Size=$(du -h "$back_Ups" | awk '{print $1}')
  
  echo "Original File: $file, Size: $ogSize"
  echo "Compressed File: $back_Ups, Size: $comp_Size"
  

# Main

# file sizes
fSize "/var/log/syslog"

fSize "/var/log/wtmp"

# compress/backup files/logs
compBack "/var/log/syslog"

compBack "/var/log/wtmp"

# End
