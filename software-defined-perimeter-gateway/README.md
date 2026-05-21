# Software-Defined Perimeter Zero Trust Gateway

## Objectives
- Build a local Software-Defined Perimeter style access gateway.
- Configure NGINX as a reverse proxy.
- Place Apache behind the proxy as an internal backend.
- Add oauth2-proxy as an identity-aware access layer.
- Create a dynamic iptables policy script.

## Tools Used
- Ubuntu 24.04
- NGINX
- Apache2
- oauth2-proxy v7.12.0
- iptables
- systemd
- Bash

## Key Skills Demonstrated
- Zero Trust access gateway design
- Reverse proxy configuration
- Identity-aware proxy integration
- Linux firewall rule automation
- Service validation and troubleshooting
- Secure backend exposure pattern

## Troubleshooting Log
- Fixed Apache and NGINX port conflict by moving Apache from port 80 to 8080.
- Replaced outdated oauth2-proxy v7.0.0 with v7.12.0.
- Fixed incorrect binary move command for oauth2-proxy.
- Improved firewall script to prevent duplicate iptables rules.
