#!/usr/bin/env python3
import sys

for line in sys.stdin:
    parts = line.strip().split()
    
    ip = parts[0]
    status = parts[-1]

    # Count requests per IP
    print(f"{ip}\t1")

    # Count errors
    if status == "500":
        print("ERROR\t1")