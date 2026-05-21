#!/bin/bash

set -euo pipefail

IP="${1:-}"
ACTION="${2:-}"

if [[ -z "$IP" || -z "$ACTION" ]]; then
    echo "Usage: $0 <IP_ADDRESS> <block|allow>"
    exit 1
fi

if [[ "$ACTION" == "block" ]]; then
    sudo iptables -C INPUT -s "$IP" -j REJECT 2>/dev/null || sudo iptables -A INPUT -s "$IP" -j REJECT
    echo "Blocked IP: $IP"

elif [[ "$ACTION" == "allow" ]]; then
    sudo iptables -D INPUT -s "$IP" -j REJECT 2>/dev/null || true
    echo "Allowed IP: $IP"

else
    echo "Invalid action. Use: block or allow"
    exit 1
fi
