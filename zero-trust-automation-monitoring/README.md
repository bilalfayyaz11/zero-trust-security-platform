# Zero Trust Automation and Monitoring Platform

## Overview

This project demonstrates the implementation of a Zero Trust monitoring and automated threat response environment using the Elastic Stack, Linux firewall controls, Apache, and Python automation.

The environment combines network segmentation, SIEM-style observability, authentication monitoring, automated policy enforcement, and event-driven threat response workflows.

---

## Objectives

* Implement Zero Trust segmentation policies
* Configure protected backend infrastructure
* Deploy Elastic Stack monitoring services
* Ingest and analyze authentication logs
* Automate security policy adjustments
* Detect suspicious authentication activity
* Simulate SOC-style automated incident response
* Visualize security telemetry using Kibana

---

## Technologies Used

* Ubuntu Linux 24.04
* Python 3.12
* Elasticsearch 8
* Logstash 8
* Kibana 8
* Filebeat 8
* Apache HTTP Server
* iptables / nftables
* Java 17
* watchdog
* Bash scripting

---

## Key Skills Demonstrated

* Zero Trust architecture implementation
* SIEM deployment and configuration
* Log ingestion pipeline engineering
* Security monitoring automation
* Infrastructure observability
* Event-driven incident response
* Firewall policy automation
* Authentication monitoring
* Python security scripting
* Linux security administration
* DevSecOps operations

---

## Architecture

### Protected Backend Layer

* Apache hosted on port 8080
* HTTP authentication enforced
* Firewall-controlled access

### Monitoring Pipeline

Filebeat → Logstash → Elasticsearch → Kibana

### Security Automation

* Real-time auth.log monitoring
* Failed-login detection
* Automated IP blocking
* Incident logging

---

## Project Structure

scripts/

* auto_policy_adjust.py

configs/

* filebeat-zero-trust.yml
* logstash-zero-trust-pipeline.conf
* iptables-rules.txt

reports/

* network-segmentation-summary.md
* log-monitoring-pipeline-summary.md
* security-automation-summary.md
* final-validation-report.txt

validation/

* apache-auth-test.html
* apache-test-page.html
* auto-policy-runtime.log

---

## Security Controls Implemented

### Network Segmentation

* Cross-zone restrictions enforced using iptables
* Persistent firewall policies configured

### Access Control

* Apache authentication protection enabled
* Port-level access restrictions enforced

### SIEM Monitoring

* Authentication and system logs ingested
* Security event tagging enabled
* Log aggregation operational

### Automated Threat Response

* Real-time authentication monitoring
* Automatic suspicious-IP blocking
* Event-driven policy enforcement

---

## Troubleshooting & Modernization Log

### Replaced Deprecated apt-key

Modern Ubuntu 24.04 requires signed keyrings instead of apt-key.

### Upgraded Elastic Repository

Migrated from outdated Elastic 7.x repository to Elastic 8.x.

### Fixed Elasticsearch YAML Duplication

Duplicate YAML keys caused Elasticsearch startup failure:
JsonReadContext._checkDup

Resolved by rebuilding a clean minimal configuration.

### Optimized ELK for Low-Memory Environment

Reduced JVM heap allocation for:

* Elasticsearch
* Logstash

to support operation on a 3.7 GB RAM lab VM.

### Fixed Python CPU Burn

Replaced:
while True: pass

with:
time.sleep(1)

to avoid 100% CPU utilization.

### Fixed Invalid subprocess Syntax

Corrected:
"-j REJECT"

to:
"-j", "REJECT"

for valid subprocess argument handling.

### Fixed Ubuntu 24.04 PEP 668 Restrictions

Used isolated Python virtual environment for watchdog installation.

---

## Validation Results

Validated successfully:

* Elasticsearch cluster
* Logstash ingestion
* Filebeat shipping
* Kibana accessibility
* Apache protected service
* Firewall enforcement
* Security automation runtime
* Real-time monitoring pipeline

---

## Outcome

This project demonstrates practical implementation of Zero Trust monitoring, SIEM engineering, and automated threat response workflows using modern Linux security engineering techniques.
