import subprocess

def run_command(command):
    result = subprocess.run(command, capture_output=True, text=True)
    return result.stdout.strip(), result.stderr.strip()

def block_ip(ip_address):
    print(f"[+] Blocking IP: {ip_address}")
    stdout, stderr = run_command([
        "sudo", "iptables", "-A", "INPUT",
        "-s", ip_address,
        "-j", "REJECT"
    ])
    return stdout, stderr

def allow_ip(ip_address):
    print(f"[+] Allowing IP: {ip_address}")
    stdout, stderr = run_command([
        "sudo", "iptables", "-A", "INPUT",
        "-s", ip_address,
        "-j", "ACCEPT"
    ])
    return stdout, stderr

blocked_ip = "192.168.1.100"
allowed_ip = "192.168.2.100"

block_ip(blocked_ip)
allow_ip(allowed_ip)

print("[+] Zero Trust policy automation completed.")
