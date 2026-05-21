#!/usr/bin/env python3

import argparse
import subprocess
import sys


def run_command(command):
    result = subprocess.run(command, capture_output=True, text=True)

    if result.returncode != 0 and "Bad rule" not in result.stderr:
        print(result.stderr.strip())
        return False

    return True


def rule_exists(ip_address, action):
    jump = "REJECT" if action == "block" else "ACCEPT"
    check = subprocess.run(
        ["sudo", "iptables", "-C", "INPUT", "-s", ip_address, "-j", jump],
        capture_output=True,
        text=True
    )
    return check.returncode == 0


def block_ip(ip_address):
    if not rule_exists(ip_address, "block"):
        return run_command(["sudo", "iptables", "-A", "INPUT", "-s", ip_address, "-j", "REJECT"])
    print(f"Block rule already exists for {ip_address}")
    return True


def allow_ip(ip_address):
    run_command(["sudo", "iptables", "-D", "INPUT", "-s", ip_address, "-j", "REJECT"])
    if not rule_exists(ip_address, "allow"):
        return run_command(["sudo", "iptables", "-A", "INPUT", "-s", ip_address, "-j", "ACCEPT"])
    print(f"Allow rule already exists for {ip_address}")
    return True


def remove_ip_rules(ip_address):
    for jump in ["REJECT", "ACCEPT"]:
        while subprocess.run(
            ["sudo", "iptables", "-C", "INPUT", "-s", ip_address, "-j", jump],
            capture_output=True,
            text=True
        ).returncode == 0:
            run_command(["sudo", "iptables", "-D", "INPUT", "-s", ip_address, "-j", jump])
    return True


def main():
    parser = argparse.ArgumentParser(description="SDP dynamic policy enforcement engine")
    parser.add_argument("action", choices=["block", "allow", "remove"])
    parser.add_argument("ip_address")

    args = parser.parse_args()

    if args.action == "block":
        success = block_ip(args.ip_address)
    elif args.action == "allow":
        success = allow_ip(args.ip_address)
    else:
        success = remove_ip_rules(args.ip_address)

    if success:
        print(f"Policy action '{args.action}' applied for {args.ip_address}")
    else:
        sys.exit(1)


if __name__ == "__main__":
    main()
