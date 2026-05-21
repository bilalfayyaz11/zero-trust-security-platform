# Log Monitoring Pipeline Summary

## Objective

Configured Filebeat and Logstash to collect Linux authentication and system logs for Zero Trust monitoring.

## Pipeline Flow

Filebeat reads logs from:
- /var/log/auth.log
- /var/log/syslog

Logstash receives Beats events on port 5044, tags authentication logs, identifies failed login events, and forwards events into Elasticsearch.

## Security Monitoring Use Case

This pipeline supports detection of:
- Failed SSH login attempts
- Authentication anomalies
- Security incidents
- System-level events relevant to Zero Trust enforcement
