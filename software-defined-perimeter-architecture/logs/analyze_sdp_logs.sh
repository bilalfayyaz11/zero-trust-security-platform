#!/bin/bash

set -euo pipefail

echo "===== SDP CONTROLLER ACCESS LOGS ====="
sudo tail -20 /var/log/nginx/sdp-controller-access.log 2>/dev/null || echo "No controller access logs found."

echo
echo "===== SDP CONTROLLER ERROR LOGS ====="
sudo tail -20 /var/log/nginx/sdp-controller-error.log 2>/dev/null || echo "No controller error logs found."

echo
echo "===== SDP BROKER SERVICE LOGS ====="
sudo journalctl -u sdp-broker --no-pager | tail -20

echo
echo "===== IPTABLES / KERNEL ENFORCEMENT LOGS ====="
sudo journalctl -k --no-pager | grep "SDP-Enforcement" | tail -20 || echo "No iptables enforcement logs yet."
