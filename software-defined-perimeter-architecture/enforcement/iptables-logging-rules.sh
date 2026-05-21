#!/bin/bash

set -euo pipefail

sudo iptables -C INPUT -m limit --limit 5/min -j LOG --log-prefix "SDP-Enforcement: " --log-level 4 2>/dev/null || \
sudo iptables -A INPUT -m limit --limit 5/min -j LOG --log-prefix "SDP-Enforcement: " --log-level 4

sudo netfilter-persistent save
