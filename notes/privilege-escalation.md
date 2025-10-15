# Privilege Escalation (conceptual)

- After obtaining a shell as the web user, run local enumeration:
  - `sudo -l` may reveal binaries allowed to be run as other users without password.

- Example misconfiguration observed in lab:
  - `www-data ALL=(beloved) NOPASSWD: /usr/local/bin/nokogiri`

- Escalation approach (conceptual):
  1. Use sudo to run the allowed binary as the target user.
  2. Abuse the binary's functionality (e.g., reflective execution or reading files) to gain higher privileges.
  3. If key material is available, use it to access other accounts (keys redacted).

- Recommendations:
  - Remove NOPASSWD entries for web/service users.
  - Limit allowed binaries and monitor sudo usage.
