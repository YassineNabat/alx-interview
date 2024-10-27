#!/usr/bin/python3
import sys
import signal

# Initialize metrics
total_file_size = 0
status_codes_count = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0
}
line_count = 0

def print_stats():
    """Prints the current statistics"""
    print(f"File size: {total_file_size}")
    for code in sorted(status_codes_count.keys()):
        if status_codes_count[code] > 0:
            print(f"{code}: {status_codes_count[code]}")

def process_line(line):
    """Processes a single line to update metrics if the format is valid"""
    global total_file_size
    parts = line.split()
    
    # Validate line format
    if len(parts) >= 7 and parts[5] == '"GET' and parts[6].startswith('/projects/260'):
        try:
            status_code = parts[-2]
            file_size = int(parts[-1])
            
            # Update total file size
            total_file_size += file_size
            
            # Update status code count if valid
            if status_code in status_codes_count:
                status_codes_count[status_code] += 1
        except (ValueError, IndexError):
            pass

def signal_handler(sig, frame):
    """Handles keyboard interruption (CTRL + C)"""
    print_stats()
    sys.exit(0)

# Set up signal handler for CTRL + C
signal.signal(signal.SIGINT, signal_handler)

# Main loop to read stdin
for line in sys.stdin:
    process_line(line.strip())
    line_count += 1

    # Print stats after every 10 lines
    if line_count % 10 == 0:
        print_stats()

# Print final stats if there are any remaining lines
if line_count % 10 != 0:
    print_stats()
