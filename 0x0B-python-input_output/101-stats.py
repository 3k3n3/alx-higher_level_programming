#!/usr/bin/python3
"""A script that reads stdin line by line and computes metrics."""
import sys
from collections import defaultdict


total_size = 0
status_counts = defaultdict(int)
line_count = 0

try:
    # Read stdin line by line
    for line in sys.stdin:
        line_count += 1
        fields = line.split()

        # Increment total file size
        try:
            file_size = int(fields[-1])
            total_size += file_size
        except (IndexError, ValueError):
            pass

        # Count status codes
        try:
            status_code = int(fields[-2])
            status_counts[status_code] += 1
        except (IndexError, ValueError):
            pass

        # Print statistics every 10 lines
        if line_count % 10 == 0:
            print("Total file size: {}".format(total_size))
            for code in sorted(status_counts.keys()):
                print("{}: {}".format(code, status_counts[code]))

except KeyboardInterrupt:
    # Print final statistics on keyboard interruption
    print("Total file size: {}".format(total_size))
    for code in sorted(status_counts.keys()):
        print("{}: {}".format(code, status_counts[code]))
