#!/bin/bash

set -euo pipefail

INTERFACE="${1:-$(ip route | awk '/default/ {print $5; exit}')}"
LOG_FILE="/var/log/network_traffic.log"

if [[ -z "$INTERFACE" ]]; then
    echo "No active network interface detected."
    exit 1
fi

echo "Monitoring network traffic on interface: $INTERFACE"
echo "Log file: $LOG_FILE"

sudo iftop -t -s 10 -i "$INTERFACE" | sudo tee -a "$LOG_FILE"
