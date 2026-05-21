# Advanced Software-Defined Perimeter Security Architecture

## Objectives
- Implement adaptive authentication using MFA for SSH access
- Encrypt traffic in transit using TLS/SSL
- Configure NGINX as a secure HTTPS reverse proxy
- Isolate backend services behind the perimeter gateway
- Create monitoring and intrusion-detection scripts
- Simulate controlled attack scenarios to validate security controls

## Tools Used
- Ubuntu 24.04
- NGINX
- Apache2
- OpenSSL
- PAM Google Authenticator
- Hydra
- mitmproxy
- iftop
- Bash
- systemd

## Key Skills Demonstrated
- Zero Trust perimeter architecture
- MFA integration with PAM and SSH
- TLS certificate generation and HTTPS configuration
- Reverse proxy security hardening
- Network traffic monitoring
- SSH brute-force detection logic
- Controlled security attack simulation
- Linux security operations and validation

## Troubleshooting Log
- Fixed Apache and NGINX port conflicts by isolating Apache on port 8080.
- Replaced hardcoded eth0 monitoring logic with automatic interface detection.
- Added auth.log and journalctl fallback logic for Ubuntu 24.04 compatibility.
- Avoided unsafe root SSH brute-force testing and used controlled ubuntu-user testing instead.
- Corrected misleading MitM assumptions regarding TLS plaintext interception.
- Used non-interactive OpenSSL certificate generation for automation and reproducibility.
