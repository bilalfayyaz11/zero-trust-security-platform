import os
import subprocess

def create_user(username):
    print(f"[+] Creating onboarding user: {username}")

    check_user = subprocess.run(
        ["id", username],
        capture_output=True,
        text=True
    )

    if check_user.returncode == 0:
        print("[*] User already exists.")
        return

    subprocess.run([
        "sudo", "useradd",
        "-m",
        "-s", "/bin/bash",
        username
    ])

    print(f"[+] User {username} created.")

def generate_mfa_notice(username):
    notice_path = f"/home/ubuntu/zero-trust-deployment-blueprint/reports/{username}-mfa-notice.txt"

    with open(notice_path, "w") as f:
        f.write(f"""
Zero Trust Device Onboarding Report

User: {username}

Status:
- Linux account provisioned
- Ready for MFA enrollment
- SSH PAM authentication compatible

Security Note:
Interactive MFA secret generation should be completed securely by the end-user.
""")

    print(f"[+] MFA onboarding report created: {notice_path}")

new_user = "ztuser"

create_user(new_user)
generate_mfa_notice(new_user)

print("[+] Device onboarding automation completed.")
