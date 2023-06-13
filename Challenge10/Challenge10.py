#!/usr/bin/env python3

# Script Name:                  Python
# Author:                       Raphael Chookagian
# Date of latest revision:      06/12/2023
# Purpose:                      Create a Python script that:

# Create a Python script that fetches this information using Psutil:

# - Time spent by normal processes executing in user mode
# - Time spent by processes executing in kernel mode
# - Time when system was idle
# - Time spent by priority processes executing in user mode
# - Time spent waiting for I/O to complete.
# - Time spent for servicing hardware interrupts
# - Time spent for servicing software interrupts
# - Time spent by other operating systems running in a virtualized environment
# - Time spent running a virtual CPU for guest operating systems under the control of the Linux kernel

# Install Psutil.
import psutil

# Declaration of variables

# Get the CPU times
cpu_times = psutil.cpu_times()

# - Time spent by normal processes executing in user mode
user_time = cpu_times.user

# - Time spent by processes executing in kernel mode
kernel_time = cpu_times.system

# - Time when system was idle
idle_time = cpu_times.idle

# - Time spent by priority processes executing in user mode
priority_user_time = cpu_times.priority_user

# - Time spent waiting for I/O to complete.
iowait_time = cpu_times.iowait

# - Time spent for servicing hardware interrupts
interrupt_time = cpu_times.interrupt

# - Time spent for servicing software interrupts
soft_interrupt_time = cpu_times.softirq


# - Time spent by other operating systems running in a virtualized environment

# Get current process ID
current_pid = psutil.Process().pid

# Get list of all running processes
all_processes = psutil.process_iter()

# set initial total time at 0
total_time = 0.0

# Iterate over each process
for process in all_processes:
    try:
        # Exclude the current process and processes owned by the current user
        if process.pid != current_pid and process.username() != psutil.Process().username():
            # Get the CPU times of the process
            cpu_times = process.cpu_times()
            
            # Sum up the time spent by other operating systems
            total_time += cpu_times.system

    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
        # Handle exceptions that may occur during process retrieval
        pass

# - Time spent running a virtual CPU for guest operating systems under the control of the Linux kernel
guest_time = cpu_times.guest



# Main

# Print the results

# - Time spent by normal processes executing in user mode
print(f"Time spent by normal processes executing in user mode: {user_time} seconds")

# - Time spent by processes executing in kernel mode
print(f"Time spent by processes executing in kernel mode: {kernel_time} seconds")

# - Time when system was idle
print(f"Time when the system was idle: {idle_time} seconds")

# - Time spent by priority processes executing in user mode
print(f"Time spent by priority processes executing in user mode: {priority_user_time} seconds")

# - Time spent waiting for I/O to complete.
print(f"Time spent waiting for I/O to complete: {iowait_time} seconds")

# - Time spent for servicing hardware interrupts
print(f"Time spent for servicing hardware interrupts: {interrupt_time} seconds")

# - Time spent for servicing software interrupts
print(f"Time spent for servicing software interrupts: {soft_interrupt_time} seconds")

# - Time spent by other operating systems running in a virtualized environment
print(f"Time spent by other operating systems: {total_time} seconds")

# - Time spent running a virtual CPU for guest operating systems under the control of the Linux kernel
print(f"Time spent running a virtual CPU for guest operating systems: {guest_time} seconds")


# End

