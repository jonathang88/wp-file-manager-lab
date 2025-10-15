# wp-file-manager-lab

**Educational lab** documenting the exploitation path, privilege escalation and mitigations for a vulnerable WordPress plugin (wp-file-manager / related wp plugins) in an isolated CTF/lab environment.

> NOTE: This repository is sanitized for public release. IPs, private keys and flags have been redacted or replaced with `[REDACTED]`.

## Contents
- `lab-report.md` — sanitized lab report (summary and findings).
- `lab-report.pdf` — optional PDF export of the report (not included).
- `notes/` — detailed notes (recon, exploitation concepts, privilege escalation, mitigation).
- `scripts/` — safe, non-exploitative helpers (plugin detector).
- `screenshots/` — sanitized evidence images.
- `environment/docker-compose.example.yml` — sample, safe docker-compose to recreate a lab (example).
- `LICENSE` — MIT.

## Disclaimer
This repository is for **educational and defensive** purposes only. Do not run exploit code or use these techniques outside authorized test environments.

## How to reproduce safely (high level)
1. Use an isolated network or VM.
2. Deploy a test WordPress instance and install a deliberately vulnerable plugin version (use official, legal sources).
3. Follow the conceptual steps in `lab-report.md` and `notes/` to learn the methodology.
