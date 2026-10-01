# Layer 7 Application Tools

Educational tools for Layer 7 (Application Layer) protocol operations.

## Tools

### http_toolkit.py
HTTP/HTTPS reconnaissance and testing toolkit.

**Usage:**
```bash
python http_toolkit.py <url> [OPTIONS]
```

**Examples:**
```bash
# Basic reconnaissance
python http_toolkit.py http://example.com

# Get HTTP headers
python http_toolkit.py http://example.com --headers

# Check HTTP methods
python http_toolkit.py http://example.com --methods

# Directory bruteforce
python http_toolkit.py http://example.com --bruteforce

# Custom wordlist
python http_toolkit.py http://example.com --bruteforce --wordlist common.txt

# DNS lookup
python http_toolkit.py http://example.com --dns
```

### dns_toolkit.py
DNS reconnaissance and enumeration toolkit.

**Usage:**
```bash
python dns_toolkit.py <domain> [OPTIONS]
```

**Examples:**
```bash
# Full DNS reconnaissance
python dns_toolkit.py example.com --full

# Get specific records
python dns_toolkit.py example.com --a
python dns_toolkit.py example.com --mx
python dns_toolkit.py example.com --ns
python dns_toolkit.py example.com --txt

# Subdomain enumeration
python dns_toolkit.py example.com --subdomains

# Zone transfer attempt
python dns_toolkit.py example.com --axfr

# Reverse DNS
python dns_toolkit.py --reverse 8.8.8.8
```

### smtp_toolkit.py
SMTP mail server reconnaissance and testing.

**Usage:**
```bash
python smtp_toolkit.py <hostname> [OPTIONS]
```

**Examples:**
```bash
# Get SMTP banner
python smtp_toolkit.py mail.example.com --banner

# Get server info
python smtp_toolkit.py mail.example.com --info

# Check TLS support
python smtp_toolkit.py mail.example.com --info --tls

# User enumeration
python smtp_toolkit.py mail.example.com --enum

# Check specific user
python smtp_toolkit.py mail.example.com --vrfy admin

# Test MAIL FROM
python smtp_toolkit.py mail.example.com --mail-from test@example.com
```

### ftp_toolkit.py
FTP server reconnaissance and testing.

**Usage:**
```bash
python ftp_toolkit.py <hostname> [OPTIONS]
```

**Examples:**
```bash
# Get FTP banner
python ftp_toolkit.py ftp.example.com --banner

# Check anonymous access
python ftp_toolkit.py ftp.example.com --anonymous

# Get server info
python ftp_toolkit.py ftp.example.com --info

# FTP bruteforce
python ftp_toolkit.py ftp.example.com --bruteforce

# Recursive directory listing
python ftp_toolkit.py ftp.example.com --recursive
```

## Requirements

```bash
pip install -r requirements.txt
```

Or install individually:
```bash
pip install requests dnspython
```

## Installation

```bash
# Install dependencies
pip install requests dnspython

# Make scripts executable (Linux/Mac)
chmod +x layer7/*.py
```

## Important Notes

- These tools are for **educational purposes only**
- Use only on systems you own or have permission to test
- Unauthorized access to systems is illegal
- SMTP/FTP testing may trigger security alerts
- Always respect rate limits and server policies

## Safety Guidelines

- Get proper authorization before testing
- Be aware of applicable laws and regulations
- Use responsibly and ethically
- Don't overload target systems
- Consider using dedicated testing environments

## Protocol-Specific Notes

### HTTP
- Always use HTTPS when available
- Respect robots.txt
- Don't abuse API endpoints

### DNS
- DNS queries are generally safe
- Zone transfers are rarely allowed
- Consider privacy implications

### SMTP
- Mail servers log all connections
- User enumeration may be blocked
- Test on your own mail servers

### FTP
- Anonymous FTP is becoming rare
- Bruteforce attacks are easily detected
- Many modern systems disable FTP
