# Ops Challenge: Clearing Logs

## Overview

Log clearing can be useful as an administrator of your logs are routinely rotated, or you’re in a situation where the log file sizes are getting out of hand. Today, you will be writing a bash script that clears log files for you.

## Objectives

Write a log clearing bash script.

## Tasks

Write a bash script that performs the following tasks:

* Print to the screen the file size of the log files before compression

* Compress the contents of the log files listed below to a backup directory
  * /var/log/syslog
  * /var/log/wtmp

* The file name should contain a time stamp with the following format -YYYYMMDDHHMMSS
  * Example: /var/log/backups/syslog-20220928081457.zip

* Clear the contents of the log file

* Print to screen the file size of the compressed file

* Compare the size of the compressed files to the size of the original log files

## Stretch Goals

In offensive security operations, often an attacker will want to use a log clearing script to remove the evidence of their behavior on the targeted computer systems. How can your script be used to clear tracks?

* Watch [How To Clear Tracks & Logs On Linux](https://www.youtube.com/watch?v=TgquV_OA-lU&ab_channel=HackerSploit)

* Using the knowledge of various logs described in this video, expand your script; what other system logs can you clear? See how many logs you can clear!

* In your comments per log cleared, explain what the log tracks in the Ubuntu system. Why is this log important?
