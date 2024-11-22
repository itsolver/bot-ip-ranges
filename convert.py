"""Script to fetch and convert bot IP ranges from various sources to CSV format."""

import csv
from typing import List, Tuple
import requests

def fetch_bing_ips() -> List[Tuple[str, str]]:
    """Fetch Bing bot IPs from official source"""
    response = requests.get('https://www.bing.com/toolbox/bingbot.json', timeout=30)
    data = response.json()
    ips = []
    for prefix in data.get('prefixes', []):
        if 'ipv4Prefix' in prefix:
            ips.append((prefix['ipv4Prefix'], 'Bingbot'))
        elif 'ipv6Prefix' in prefix:
            ips.append((prefix['ipv6Prefix'], 'Bingbot'))
    return ips

def fetch_google_ips() -> List[Tuple[str, str]]:
    """Fetch Google crawler IPs from official source"""
    url = 'https://developers.google.com/static/search/apis/ipranges/googlebot.json'
    response = requests.get(url, timeout=30)
    data = response.json()
    ips = []
    for prefix in data.get('prefixes', []):
        if 'ipv4Prefix' in prefix:
            ips.append((prefix['ipv4Prefix'], 'googlecrawler'))
        elif 'ipv6Prefix' in prefix:
            ips.append((prefix['ipv6Prefix'], 'googlecrawler'))
    return ips

def fetch_uptimerobot_ips() -> List[Tuple[str, str]]:
    """Fetch UptimeRobot IPs from official source"""
    response = requests.get('https://uptimerobot.com/inc/files/ips/IPv4andIPv6.txt', timeout=30)
    # Split by whitespace and filter out empty strings
    ips = [ip.strip() for ip in response.text.split() if ip.strip()]
    # Convert to list of tuples with name
    return [(ip, 'uptimerobot') for ip in ips]

def write_csv(data: List[Tuple[str, str]], output_file: str):
    """Write data to CSV file with type detection"""
    with open(output_file, 'w', newline='', encoding='utf-8') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['type', 'prefix', 'name'])

        for ip, name in data:
            # Determine if IPv4 or IPv6 based on presence of ':'
            ip_type = 'IPv6' if ':' in ip else 'IPv4'
            writer.writerow([ip_type, ip, name])

def main():
    """Execute the IP range fetching and CSV conversion process."""
    # Dictionary of source functions and their output files
    sources = {
        'bingbots.csv': fetch_bing_ips,
        'googlecrawlers.csv': fetch_google_ips,
        'uptimerobots.csv': fetch_uptimerobot_ips
    }

    for output_file, fetch_function in sources.items():
        try:
            print(f"Fetching data for {output_file}...")
            data = fetch_function()
            write_csv(data, output_file)
            print(f"Successfully created {output_file}")
        except requests.RequestException as e:
            print(f"Network error processing {output_file}: {str(e)}")
        except (IOError, ValueError) as e:
            print(f"Error processing {output_file}: {str(e)}")

if __name__ == "__main__":
    main()
