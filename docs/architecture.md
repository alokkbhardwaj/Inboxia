# Email System Architecture

This project uses a containerized architecture to implement a self-hosted email system.

## Components
- Postfix: SMTP server for sending and receiving email
- Dovecot: IMAP server for mailbox access
- Roundcube: Webmail interface
- Docker Compose: Service orchestration

## Email Flow
Sending:
User → Roundcube → Postfix → Internet

Receiving:
Internet → Postfix → Dovecot → Roundcube → User
