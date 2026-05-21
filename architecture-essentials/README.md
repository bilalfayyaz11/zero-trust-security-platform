# Zero Trust Security Framework Implementation

## Objectives
- Implement least privilege access using Linux users and sudoers policies.
- Apply micro-segmentation using iptables firewall rules.
- Configure MFA hardening for SSH authentication using PAM Google Authenticator.
- Simulate database access restriction using Zero Trust access control logic.

## Tools Used
- Ubuntu 24.04
- Linux Users and Groups
- sudoers
- iptables
- OpenSSH
- PAM
- Google Authenticator
- curl
- netcat
- Python HTTP Server

## Key Skills Demonstrated
- Zero Trust Architecture implementation
- Least privilege access control
- Role-based access restrictions
- Linux privilege management
- Network micro-segmentation
- Firewall rule ordering and validation
- SSH authentication hardening
- MFA integration using PAM
- Cloud lab troubleshooting

## Implementation Summary
This project demonstrates foundational Zero Trust controls on a Linux cloud environment. Users were assigned different privilege levels, network ports were segmented with firewall rules, database access was restricted, and SSH authentication was hardened with MFA.

## Troubleshooting Log
- Fixed outdated MFA package logic by using `libpam-google-authenticator`.
- Avoided unsafe direct sudoers editing by using `/etc/sudoers.d/`.
- Fixed privileged port error by using `sudo python3 -m http.server 80`.
- Prevented SSH lockout by backing up SSH and PAM configs before MFA changes.
- Corrected iptables rule order so localhost MySQL access appears before the global MySQL DROP rule.
