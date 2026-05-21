# Software-Defined Perimeter Architecture Deep Dive

## Objectives
- Build a simulated Software-Defined Perimeter architecture
- Configure an NGINX-based SDP controller
- Deploy a Flask-based SDP broker
- Isolate an Apache backend service behind the controller
- Implement dynamic firewall policy enforcement using Python and iptables
- Centralize communication flow analysis across controller, broker, and enforcement logs
- Validate the architecture using controlled attack simulations

## Tools Used
- Ubuntu 24.04
- NGINX
- Apache2
- Flask
- Python 3.12
- iptables
- iptables-persistent
- Hydra
- Bash
- systemd
- curl

## Key Skills Demonstrated
- Zero Trust architecture design
- Software-Defined Perimeter component modeling
- Reverse proxy authentication
- Flask service deployment with systemd
- Dynamic firewall policy automation
- Security telemetry collection
- NGINX and kernel log analysis
- Controlled brute-force and request-pressure testing

## Troubleshooting Log
- Fixed missing pip3 by installing python3-pip.
- Replaced unsafe LOIC/DDoS simulation with controlled curl-based local pressure testing.
- Replaced root SSH brute-force testing with controlled ubuntu-user simulation.
- Fixed Flask binding by using 127.0.0.1 instead of ambiguous localhost.
- Fixed missing iptables persistence path by using iptables-persistent and netfilter-persistent.
- Added duplicate-safe firewall rule handling in the Python enforcement engine.
