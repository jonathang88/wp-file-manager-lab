# Lab report — wp-file-manager (sanitized)

## Overview
This lab documents the exploitation of a vulnerable WordPress plugin in an isolated environment. The original notes were sanitized to remove IPs, private keys and flags.

**High-level flow (sanitized):**
1. Reconnaissance using WP fingerprinting and plugin enumeration.
2. Identification of an outdated/vulnerable plugin.
3. Obtaining a public exploit for the plugin (research via SearchSploit) and adapting it in a controlled lab.
4. Uploading a webshell to the target via an upload vulnerability and confirming access (sanitized URLs).
5. Obtaining a reverse shell to the attacker's controlled listener inside the lab network.
6. Local enumeration: `sudo -l` and checking for misconfigured sudo entries.
7. Privilege escalation by abusing an allowed binary (`nokogiri`) executed via sudo without password.
8. Persistence by creating a backdoor script and scheduling it (crontab) — documented as conceptual steps only.
9. Post-exploitation: reading sensitive files, retrieving flags (redacted), and evidence captured as sanitized screenshots.
10. Recommendations and mitigations provided at the end.

## Key findings (sanitized)
- Vulnerable plugin discovered via aggressive plugin detection.
- Public exploit (referenced by SearchSploit) was used in the lab to place a webshell.
- Webshell allowed command execution and reverse shell into the lab.
- Sudo misconfiguration allowed running `/usr/local/bin/nokogiri` as another user without password, enabling privilege escalation.
- Additional techniques observed: wildcard injection, symlink tricks, and use of pspy64 for process monitoring.

## Evidence
Sanitized logs and step notes are in `notes/`. Screenshots (sanitized) are expected in `screenshots/`.

## Mitigations (summary)
- Keep WordPress core and plugins updated.
- Remove NOPASSWD sudo rules or restrict allowed binaries.
- Restrict and validate file uploads; enforce allowed file types and sanitization.
- Use a WAF and monitor file creation in upload directories.
- Monitor process creation and unexpected cron jobs.
