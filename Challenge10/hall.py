import psutil
import subprocess

def get_priority_time():
    try:
        output = subprocess.check_output(['ps'])
        lines = output.decode().strip().split('\n')
        priority_process_time = 0

        # Skip the header line
        lines = lines[1:]

        for line in lines:
            fields = line.split()
            if len(fields) >= 10:
                # The elapsed time is usually in the tenth field
                elapsed_time = int(fields[9])
                priority_process_time += elapsed_time

        return priority_process_time
    except subprocess.CalledProcessError:
        raise RuntimeError("Error: Unable to retrieve priority process time. Skipping...")

cpu_times = psutil.cpu_times()
user_time = cpu_times.user
kernel_time = cpu_times.system
idle_time = cpu_times.idle
priority_time = get_priority_time()

try:
    iowait_time = psutil.cpu_times().iowait
except AttributeError:
    print("Warning: Unable to retrieve I/O wait time. Skipping...")
    iowait_time = 0

try:
    interrupt_time = psutil.cpu_times().irq
except AttributeError:
    print("Warning: Unable to retrieve interrupt time. Skipping...")
    interrupt_time = 0

try:
    soft_interrupt_time = psutil.cpu_times().softirq
except AttributeError:
    print("Warning: Unable to retrieve soft interrupt time. Skipping...")
    soft_interrupt_time = 0

if hasattr(psutil.cpu_times(), 'steal'):
    other_os_time = psutil.cpu_times().steal
else:
    print("Warning: Unable to retrieve other OS time. Skipping...")
    other_os_time = 0

if hasattr(psutil.cpu_times(), 'guest'):
    guest_time = psutil.cpu_times().guest
else:
    print("Warning: Unable to retrieve guest time. Skipping...")
    guest_time = 0

file_path = "psutil_output.txt"

with open(file_path, "w") as file:
    file.write(f"Time spent by normal processes executing in user mode: {user_time} seconds\n")
    file.write(f"Time spent by processes executing in kernel mode: {kernel_time} seconds\n")
    file.write(f"Time when the system was idle: {idle_time} seconds\n")
    file.write(f"Time spent by priority processes executing in user mode: {priority_time} seconds\n")
    file.write(f"Time spent waiting for I/O to complete: {iowait_time} seconds\n")
    file.write(f"Time spent for servicing hardware interrupts: {interrupt_time} seconds\n")
    file.write(f"Time spent for servicing software interrupts: {soft_interrupt_time} seconds\n")
    file.write(f"Time spent by other operating systems: {other_os_time} seconds\n")
    file.write(f"Time spent running a virtual CPU for guest operating systems: {guest_time} seconds\n")

    print(f"Time spent by normal processes executing in user mode: {user_time} seconds")
    print(f"Time spent by processes executing in kernel mode: {kernel_time} seconds")
    print(f"Time when the system was idle: {idle_time} seconds")
    print(f"Time spent by priority processes executing in user mode: {priority_time} seconds")
    print(f"Time spent waiting for I/O to complete: {iowait_time} seconds")
    print(f"Time spent for servicing hardware interrupts: {interrupt_time} seconds")
    print(f"Time spent for servicing software interrupts: {soft_interrupt_time} seconds")
    print(f"Time spent by other operating systems: {other_os_time} seconds")
    print(f"Time spent running a virtual CPU for guest operating systems: {guest_time} seconds")

print(f"Information saved to {file_path} successfully.")
