#!/usr/bin/env python3

import subprocess
import re
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

AUTH_LOG = "/var/log/auth.log"

blocked_ips = set()

def ip_already_blocked(ip):
    result = subprocess.run(
        ["sudo", "iptables", "-L", "INPUT", "-n"],
        capture_output=True,
        text=True
    )

    return ip in result.stdout

def block_ip(ip_address):
    if ip_address in blocked_ips:
        return

    if ip_already_blocked(ip_address):
        blocked_ips.add(ip_address)
        return

    subprocess.run([
        "sudo", "iptables",
        "-A", "INPUT",
        "-s", ip_address,
        "-j", "REJECT"
    ])

    blocked_ips.add(ip_address)

    print(f"[+] Blocked suspicious IP: {ip_address}")

    with open("/home/ubuntu/zero-trust-automation-monitoring/reports/blocked-ips.log", "a") as f:
        f.write(f"Blocked IP: {ip_address}\n")

class LogMonitorHandler(FileSystemEventHandler):

    def __init__(self):
        self.last_position = 0

    def on_modified(self, event):

        if event.src_path != AUTH_LOG:
            return

        with open(AUTH_LOG, "r") as log_file:

            log_file.seek(self.last_position)

            new_lines = log_file.readlines()

            self.last_position = log_file.tell()

            for line in new_lines:

                if "Failed password" in line:

                    ip_match = re.search(r'from (\S+)', line)

                    if ip_match:
                        ip_address = ip_match.group(1)
                        block_ip(ip_address)

if __name__ == "__main__":

    print("[+] Zero Trust auto-response monitoring started.")

    event_handler = LogMonitorHandler()

    observer = Observer()

    observer.schedule(
        event_handler,
        path="/var/log",
        recursive=False
    )

    observer.start()

    try:
        while True:
            time.sleep(1)

    except KeyboardInterrupt:
        observer.stop()

    observer.join()
