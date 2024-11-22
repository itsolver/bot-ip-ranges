# Bot IP Ranges for Cloudflare WAF

This repository helps maintain IP allowlists for legitimate bot services to use with Cloudflare's Web Application Firewall (WAF). When implementing country-based blocking in Cloudflare WAF, you'll want to ensure these legitimate bots can still access your site regardless of their country of origin.

## Purpose

1. Create custom IP lists in Cloudflare WAF for allowing legitimate bot traffic from various services including:
   - Search Engines
     - Google Crawler
     - Bing Bot
     - DuckDuckBot
     - AhrefsBot
     - MojeekBot
   - Monitoring Services
     - UptimeRobot
     - BetterUptime Bot
     - Freshping Bot
     - Pingdom Bot
     - Outage Owl
   - Social Media Preview Bots
     - Facebook Bot
     - Twitter Bot
     - Telegram Bot
   - CDN Services
     - Cloudflare
     - BunnyCDN
   - Image Processing
     - ImageKit
     - Imgix
   - Payment Webhooks
     - Stripe Webhook
     - Mollie Webhook

2. These lists can be used in conjunction with Cloudflare WAF rules to:
   - Block traffic from all countries except those specifically allowed
   - While ensuring legitimate bots can still access your site

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

1. Edit the configuration to specify which bot IP lists you want to include:
   ```yaml
   # config.yaml
   enabled_bots:
     - googlebot
     - bingbot
     - uptimerobot
     # Add any of these additional bots as needed:
     # - ahrefsbot
     # - duckduckbot
     # - facebookbot
     # - twitterbot
     # - telegrambot
     # - betteruptimebot
     # - freshpingbot
     # - pingdombot
     # - outageowl
     # - cloudflare
     # - bunnycdn
     # - imagekit
     # - imgix
     # - stripewebhook
     # - molliewebhook
   ```

2. Run the conversion script to fetch and update IP ranges:
   ```bash
   python allowedbotsips/convert.py
   ```

3. Import the generated CSV files into Cloudflare:
   - Go to Security > WAF > Tools > Custom Lists
   - Create a new IP List for each bot service
   - Upload the corresponding CSV files

4. Create WAF rules:
   - Allow traffic from these IP lists using expressions like:
     ```
     ip.src in $google_bots
     ```
   - Combine with country blocking rules as needed

**Note:** For Cloudflare compatibility, all IPv6 addresses are converted to /64 CIDR notation, as required by Cloudflare's IP list import functionality.

## Example WAF Rule Configuration

To block all countries except allowed ones while permitting legitimate bots:

```
(ip.geoip.country ne "US" and ip.geoip.country ne "AU") and not (
  ip.src in $google_bots or
  ip.src in $bing_bots or
  ip.src in $uptime_robot or
  ip.src in $facebook_bot or
  ip.src in $duckduck_bot
  # Add additional bot lists as needed
)
```

This example blocks all traffic except:
- Traffic from US and AU
- Traffic from the allowed bot IP ranges

## Data Sources

The script fetches data from official sources for each bot service. IP lists are sourced from [AnTheMaker/GoodBots](https://github.com/AnTheMaker/GoodBots) which maintains an up-to-date collection of legitimate bot IP ranges.

## License

MIT 
