# Layer 4 Network Tools

Educational tools for Layer 4 (Transport Layer) network operations.

## Tools

### tcp_scanner.py
TCP port scanner with multi-threading support.

**Usage:**
```bash
python tcp_scanner.py <target> [-p PORTS] [-t TIMEOUT] [--threads THREADS]
```

**Examples:**
```bash
# Scan common ports
python tcp_scanner.py 192.168.1.1

# Scan specific range
python tcp_scanner.py 192.168.1.1 -p 1-65535

# Scan with custom timeout
python tcp_scanner.py example.com -p 80,443,8080 -t 2
```

### udp_scanner.py
UDP port scanner for service discovery.

**Usage:**
```bash
python udp_scanner.py <target> [-p PORTS] [-t TIMEOUT] [--threads THREADS]
```

**Examples:**
```bash
# Scan common UDP ports
python udp_scanner.py 192.168.1.1

# Scan specific ports
python udp_scanner.py example.com -p 53,123,161

# Scan port range
python udp_scanner.py example.com -p 1-1024
```

### icmp_toolkit.py
ICMP operations (ping, traceroute).

**Usage:**
```bash
python icmp_toolkit.py <target> [--ping] [--traceroute] [--count N] [--hops N]
```

**Examples:**
```bash
# Ping host
python icmp_toolkit.py example.com --ping

# Traceroute
python icmp_toolkit.py example.com --traceroute

# Ping with 10 packets
python icmp_toolkit.py example.com --ping --count 10
```

**Note:** Requires administrator/root privileges.

### connection_tester.py
TCP connection testing and analysis.

**Usage:**
```bash
python connection_tester.py <target> -p PORT [OPTIONS]
```

**Examples:**
```bash
# Test single connection
python connection_tester.py example.com -p 80 --single

# Connection speed test
python connection_tester.py example.com -p 80 --speed

# Port knocking
python connection_tester.py example.com -p 80 --knock 1000,2000,3000

# TCP handshake test
python connection_tester.py example.com -p 443 --handshake
```

## Requirements

```bash
pip install -r requirements.txt
```

Or install individually:
```bash
# No external dependencies for most tools
# Only standard library required
```

## Important Notes

- These tools are for **educational purposes only**
- Use only on networks and systems you own or have permission to test
- Unauthorized network scanning is illegal in many jurisdictions
- ICMP tools require administrator/root privileges
- UDP scanning is slower and less reliable than TCP

## Safety

- Always get proper authorization before scanning
- Be aware of local laws and regulations
- Use responsibly and ethically
- Consider the impact on target systems
