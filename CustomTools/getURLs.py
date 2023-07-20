#!/usr/bin/env python3

import sys
import requests
from scapy.all import sr1, IP, ICMP
from bs4 import BeautifulSoup

try:
    # url under test
    testsubject = 'https://isc2.org'

    # override test subject if passed command args
    if (len(sys.argv) == 1) & ('http' in sys.argv[0]):
        testsubject = sys.argv[0]

    # send layer 3 packet
    p=sr1(IP(dst=testsubject.replace('https://', ''))/ICMP())

    # if response scrape the website for urls
    if p:
        # send HTTP GET and capture the response
        response = requests.get(testsubject)
        # begin parse response...
        soup = BeautifulSoup(response.text, 'html.parser')
        l = ''
        for link in soup.find_all('a'):
            l = link.get('href')
            if l[0:4] == 'http':
                # url found --> print
                print(link.get('href'))
except:
    print("An error has occured. Test subject may not be available.")
else:
    print("URL search completed without errors.")




