#!/bin/bash

set -euo pipefail

THRESHOLD="${1:-5}"

AUTH_LOG="/var/log/auth.log"

if [[ -f "$AUTH_LOG" ]]; then
    FAILED_ATTEMPTS=$(sudo grep -c "Failed password" "$AUTH_LOG" || true)
else
    FAILED_ATTEMPTS=$(sudo journalctl -u ssh --no-pager | grep -c "Failed password" || true)
fi

echo "Failed SSH login attempts detected: $FAILED_ATTEMPTS"

if [[ "$FAILED_ATTEMPTS" -gt "$THRESHOLD" ]]; then
    echo "Warning: Too many failed login attempts!"
    echo "Recommended action: review SSH source IPs and apply firewall restrictions."
else
    echo "Access is normal."
fi
