#!/usr/bin/env python3

import argparse
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import json
import sys
import time

def extract_links(base_url):
    """
    DL the page & return relative URLs
    """
    try:
        response = requests.get(base_url, timeout=10)
        response.raise_for_status()
    except requests.RequestException as e: # checker for the 200 return code, it not then return error
        print(f"[ERROR] Error getting {base_url}: {e}", file=sys.stderr)
        return []

    soup = BeautifulSoup(response.text, 'html.parser') # page's soup
    found_paths = set()

    base_netloc = urlparse(base_url).netloc
    base_scheme = urlparse(base_url).scheme

    for a in soup.find_all('a', href=True): # for all links
        href = a['href']
        absolute_url = urljoin(base_url, href)
        parsed_absolute = urlparse(absolute_url)

        if parsed_absolute.netloc == base_netloc: # check that the obtained link from the page contains the provided link
            path = parsed_absolute.path
            found_paths.add(path)

    return sorted(found_paths)


def main():
    parser = argparse.ArgumentParser(description="Extract links from URLs.")
    parser.add_argument('-u', dest='urls', action='append', required=True,
                        help="URL to analyse.")
    parser.add_argument('-o', dest='output', choices=['json', 'stdout'], required=True,
                        help="json or stdout, output format")
    args = parser.parse_args()

    result = {}

    for base_url in args.urls: # Loop for all link provided
        paths = extract_links(base_url)
        base_root = f"{urlparse(base_url).scheme}://{urlparse(base_url).netloc}"
        result[base_root] = paths

    if args.output == 'json': # check the output format and displays from the asked output format
        print(json.dumps(result, indent=2))
    else:  # stdout
        for base, paths in result.items():
            for path in paths:
                print(f"{base}{path}") # link rebuild


if __name__ == '__main__':
    main()
    while True: #infinite sleep
        time.sleep(3600)
