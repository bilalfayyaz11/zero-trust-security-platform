#!/bin/bash
set -e

echo "Applying Zero Trust network segmentation policies..."

# Flush existing custom lab rules safely
sudo iptables -F
sudo iptables -X

# Default safe baseline
sudo iptables -P INPUT ACCEPT
sudo iptables -P FORWARD ACCEPT
sudo iptables -P OUTPUT ACCEPT

# Allow loopback
sudo iptables -A INPUT -i lo -j ACCEPT

# Allow established connections
sudo iptables -A INPUT -m conntrack --ctstate ESTABLISHED,RELATED -j ACCEPT
sudo iptables -A FORWARD -m conntrack --ctstate ESTABLISHED,RELATED -j ACCEPT

# Simulated Zero Trust zones
SENSITIVE_ZONE="192.168.1.0/24"
GENERAL_ZONE="192.168.2.0/24"

# Correct segmentation: block cross-zone forwarding
sudo iptables -A FORWARD -s "$SENSITIVE_ZONE" -d "$GENERAL_ZONE" -j REJECT
sudo iptables -A FORWARD -s "$GENERAL_ZONE" -d "$SENSITIVE_ZONE" -j REJECT

# Allow same-zone traffic simulation
sudo iptables -A INPUT -s "$SENSITIVE_ZONE" -j ACCEPT
sudo iptables -A INPUT -s "$GENERAL_ZONE" -j ACCEPT

# Resource access policy examples
sudo iptables -A INPUT -p tcp --dport 8080 -s 192.168.1.10 -j ACCEPT
sudo iptables -A INPUT -p tcp --dport 8080 -j REJECT

# Block database access from general user zone
sudo iptables -A INPUT -p tcp --dport 3306 -s "$GENERAL_ZONE" -j REJECT

echo "Zero Trust segmentation policies applied."
