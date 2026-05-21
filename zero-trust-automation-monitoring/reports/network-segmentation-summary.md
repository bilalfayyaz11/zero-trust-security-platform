# Zero Trust Network Segmentation Summary

## Security Zones

- Sensitive Zone: 192.168.1.0/24
- General Zone: 192.168.2.0/24

## Security Controls

- Cross-zone traffic blocked using iptables
- Apache protected with HTTP authentication
- Access restricted through firewall policy enforcement
- Persistent firewall rules enabled

## Service Architecture

Apache backend service runs on port 8080 and simulates protected application infrastructure within a Zero Trust environment.
