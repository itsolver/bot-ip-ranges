# Bot IP Ranges

This repository contains scripts and data for maintaining lists of IP ranges used by various bot services:
- Bing Bot
- Google Crawler
- UptimeRobot

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/itsolver/bot-ip-ranges.git
   cd bot-ip-ranges
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the conversion script to fetch and update IP ranges:
   ```bash
   python allowedbotsips/convert.py
   ```

This will create/update CSV files containing the latest IP ranges for each service:
- bingbots.csv
- googlecrawlers.csv
- uptimerobots.csv

Each CSV file contains two columns:
- IP range (IPv4 or IPv6)
- Bot service name

**Note:** For Cloudflare compatibility, all IPv6 addresses are converted to /64 CIDR notation. This is required because Cloudflare's IP list import does not support individual IPv6 addresses and requires /64 CIDR blocks instead.

## Data Sources

The script fetches data directly from these official sources:
- Bing Bot: https://www.bing.com/toolbox/bingbot.json
- Google Crawler: https://developers.google.com/static/search/apis/ipranges/googlebot.json
- UptimeRobot: https://uptimerobot.com/inc/files/ips/IPv4andIPv6.txt

## License

MIT 
