# Zero Trust Security Platform

## Overview

This project demonstrates the implementation of a Zero Trust security architecture using Linux, iptables, NGINX, PAM MFA integration, TLS encryption, and Python-based automation.

The environment simulates segmented security zones, policy-based access controls, secure onboarding workflows, HTTPS enforcement, and infrastructure security automation.

---

## Objectives

* Implement Zero Trust network segmentation
* Enforce access-control policies using iptables
* Configure MFA authentication for SSH access
* Enforce HTTPS/TLS-only communication
* Automate security policy enforcement with Python
* Automate secure onboarding workflows
* Validate Zero Trust deployment controls

---

## Technologies Used

* Ubuntu Linux 24.04
* Python 3.12
* iptables / nftables
* NGINX
* OpenSSL
* PAM (Pluggable Authentication Modules)
* Google Authenticator
* SSH
* Bash scripting

---

## Key Skills Demonstrated

* Zero Trust architecture implementation
* Linux security hardening
* Network segmentation
* MFA authentication integration
* TLS/HTTPS enforcement
* Firewall policy engineering
* Security automation with Python
* Device onboarding workflows
* Infrastructure security validation
* Policy-as-code concepts

---

## Project Structure

scripts/

* apply-network-segmentation.sh
* enforce_network_policy.py
* onboard_device.py

configs/

* iptables-zero-trust-rules.txt
* sshd-config-before-mfa.backup
* sshd-pam-before-mfa.backup
* google-authenticator-secret-redacted.txt

reports/

* network-segmentation-summary.md
* mfa-onboarding-summary.md
* tls-enforcement-summary.md
* python-automation-summary.md
* final-validation-report.txt

validation/

* iptables-validation.txt
* post-automation-iptables.txt
* onboarded-user-validation.txt
* http-redirect-validation.txt
* https-validation-output.html
* tls-certificate-details.txt

web/

* index.html

---

## Security Controls Implemented

### Network Segmentation

* Simulated sensitive and general-user zones
* Cross-zone traffic restrictions enforced

### MFA Authentication

* SSH PAM integration using Google Authenticator
* Interactive authentication enabled

### TLS Enforcement

* HTTPS-only gateway configured
* HTTP automatically redirected to HTTPS

### Access Control Policies

* Port-based firewall restrictions
* Trusted-IP enforcement for services

### Security Automation

* Python-based firewall policy automation
* Automated onboarding workflow

---

## Troubleshooting & Modernization Log

### Fixed Incorrect iptables Chain Usage

Original lab instructions used the INPUT chain for inter-zone segmentation.

Correct implementation:

* FORWARD chain used for routed traffic segmentation
* INPUT chain reserved for host-level service access

### Updated PAM Module Pathing

Ubuntu 24.04 uses:

* /usr/lib/x86_64-linux-gnu/security/

instead of:

* /lib/security/

### Added iptables Persistence Support

Installed:

* iptables-persistent
* netfilter-persistent

to prevent policy loss after reboot.

### Corrected GNU find Syntax

Updated:
find ... -maxdepth 3 -type f

instead of:
find ... -type f -maxdepth 3

to remove warning behavior.

---

## Validation Results

Validated successfully:

* Network segmentation
* TLS encryption
* HTTPS enforcement
* SSH MFA integration
* Firewall policy automation
* Device onboarding workflows
* Secure service configuration

---

## Outcome

This project demonstrates practical implementation of Zero Trust security principles using modern Linux security engineering techniques and infrastructure automation workflows.
