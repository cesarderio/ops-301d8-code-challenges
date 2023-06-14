#!/usr/bin/env python3

# Script Name:                  Python
# Author:                       Raphael Chookagian
# Date of latest revision:      06/13/2023
# Purpose:                      Create a Python script that:

# Create a Python script that fetches this information using Psutil:

# - Time spent by normal processes executing in user mode
# - Time spent by processes executing in kernel mode
# - Time when the system was idle
# - Time spent by priority processes executing in user mode
# - Time spent waiting for I/O to complete.
# - Time spent for servicing hardware interrupts
# - Time spent for servicing software interrupts
# - Time spent by other operating systems running in a virtualized environment
# - Time spent running a virtual CPU for guest operating systems under the control of the Linux kernel

# Install Psutil.
import psutil
import subprocess

# Declaration of variables
# Get the CPU times
cpu_times = psutil.cpu_times()

# Get the time spent by normal processes executing in user mode
user_time = cpu_times.user

# Get the time spent by processes executing in kernel mode
kernel_time = cpu_times.system

# Get the time when the system was idle
idle_time = cpu_times.idle

# Get the time spent by priority processes executing in user mode
def get_priority_time():
    try:
        output = subprocess.check_output(['ps', '--no-headers', '-o', 'psr,etimes', '--sort=-psr'])
        lines = output.decode().strip().split('\n')
        priority_process_time = 0

        for line in lines:
            fields = line.strip().split()
            cpu_number = int(fields[0])
            elapsed_time = int(fields[1])
            if cpu_number == -2:  # Priority process CPU number in Linux
                priority_process_time += elapsed_time

        return priority_process_time
    except subprocess.CalledProcessError:
        print("Error: Unable to retrieve priority process time. Skipping...")
        return 0

priority_time = get_priority_time()

# Get the time spent waiting for I/O to complete
iowait_time = psutil.cpu_times().iowait if hasattr(psutil.cpu_times(), 'iowait') else 0

# Get the time spent for servicing hardware interrupts
interrupt_time = psutil.cpu_times().irq if hasattr(psutil.cpu_times(), 'irq') else 0

# Get the time spent for servicing software interrupts
soft_interrupt_time = psutil.cpu_times().softirq if hasattr(psutil.cpu_times(), 'softirq') else 0

# Get the time spent by other operating systems running in a virtualized environment
guest_time = psutil.cpu_times().steal if hasattr(psutil.cpu_times(), 'steal') else 0

# Get the time spent running a virtual CPU for guest operating systems under the control of the Linux kernel
guest_nice_time = psutil.cpu_times().guest_nice if hasattr(psutil.cpu_times(), 'guest_nice') else 0

# Main

# Print the results
# - Time spent by normal processes executing in user mode
print()
print(f"Time spent by normal processes executing in user mode: {user_time} seconds")
print()

# - Time spent by processes executing in kernel mode
print(f"Time spent by processes executing in kernel mode: {kernel_time} seconds")

print()
# - Time when system was idle
print(f"Time when the system was idle: {idle_time} seconds")

print()
# - Time spent by priority processes executing in user mode
print(f"Time spent by priority processes executing: {priority_time} seconds")

print()
# - Time spent waiting for I/O to complete
print(f"Time spent waiting for I/O to complete: {iowait_time} seconds")

print()
# - Time spent for servicing hardware interrupts
print(f"Time spent for servicing hardware interrupts: {interrupt_time} seconds")

print()
# - Time spent for servicing software interrupts
print(f"Time spent for servicing software interrupts: {soft_interrupt_time} seconds")

print()
# - Time spent by other operating systems running in a virtualized environment
print(f"Time spent by other operating systems: {guest_time} seconds")

print()
# - Time spent running a virtual CPU for guest operating systems under the control of the Linux kernel
print(f"Time spent running a virtual CPU for guest operating systems: {guest_nice_time} seconds")

print()
# Stretch Goals:

# Specify the file path for saving the information
file_path = "psutil_output.txt"

# Open the file in write mode
with open(file_path, "w") as file:
    # Write the information to the file
    file.write(f"Time spent by normal processes executing in user mode: {user_time} seconds\n")
    file.write(f"Time spent by processes executing in kernel mode: {kernel_time} seconds\n")
    file.write(f"Time when the system was idle: {idle_time} seconds\n")
    file.write(f"Time spent by priority processes executing: {priority_time} seconds\n")
    file.write(f"Time spent waiting for I/O to complete: {iowait_time} seconds\n")
    file.write(f"Time spent for servicing hardware interrupts: {interrupt_time} seconds\n")
    file.write(f"Time spent for servicing software interrupts: {soft_interrupt_time} seconds\n")
    file.write(f"Time spent by other operating systems: {guest_time} seconds\n")
    file.write(f"Time spent running a virtual CPU for guest operating systems: {guest_nice_time} seconds\n")

# Print a message indicating the successful saving of the information
print(f"Information saved to {file_path} successfully.")
