import argparse
from collections import deque
from bs4 import BeautifulSoup
import re
import requests
import urllib.parse
import socket
from colorama import Fore, Style

#P = Fore.WHITE
#M = Fore.RED

logo = f"""\033[1;34m====================================================
\033[1;31m╭━━━┳━╮╭━┳━━━┳━━┳╮╱╱╱╱╱╭━━━┳━━━┳━━━┳━━━┳━━━┳━━━┳━━━╮
┃╭━━┫┃╰╯┃┃╭━╮┣┫┣┫┃╱╱╱╱╱┃╭━╮┃╭━╮┃╭━╮┃╭━╮┃╭━╮┃╭━━┫╭━╮┃
┃╰━━┫╭╮╭╮┃┃╱┃┃┃┃┃┃╱╱╱╱╱┃╰━━┫┃╱╰┫╰━╯┃┃╱┃┃╰━╯┃╰━━┫╰━╯┃
\033[1;37m┃╭━━┫┃┃┃┃┃╰━╯┃┃┃┃┃╱╭┳━━╋━━╮┃┃╱╭┫╭╮╭┫╰━╯┃╭━━┫╭━━┫╭╮╭╯
┃╰━━┫┃┃┃┃┃╭━╮┣┫┣┫╰━╯┣━━┫╰━╯┃╰━╯┃┃┃╰┫╭━╮┃┃╱╱┃╰━━┫┃┃╰╮
╰━━━┻╯╰╯╰┻╯╱╰┻━━┻━━━╯╱╱╰━━━┻━━━┻╯╰━┻╯╱╰┻╯╱╱╰━━━┻╯╰━╯
\033[1;34m====================================================
\033[1;31mCredits : \033[1;37mNetSensei
\033[1;31mCoded by : \033[1;37mAsio
\033[1;31mVersion : \033[1;37m1.0
\033[1;34m====================================================
\033[0m"""

print(logo)
parser = argparse.ArgumentParser(description='Email Scraper')
parser.add_argument('-d', '--url', help='URL', required=True)
parser.add_argument('-b', '--limit', help='Limit of URLs to scrape (type "all" for no limit)', default='all')
args = parser.parse_args()

user_url = args.url
limit = None if args.limit.lower() == 'all' else int(args.limit)

urls = deque([user_url])
scraped_urls = set()
emails = set()
hosts = {}
ips = set()
ipv6s = set()
servers = set()
social_media = {
    'Facebook': set(),
    'Twitter': set(),
    'Instagram': set(),
    'LinkedIn': set()
}
count = 0

try:
    while urls:
        count += 1
        if limit and count > limit:
            break

        url = urls.popleft()
        scraped_urls.add(url)
        parts = urllib.parse.urlsplit(url)
        base_url = f'{parts.scheme}://{parts.netloc}'
        path = url[:url.rfind('/') + 1] if '/' in parts.path else url

        print(f'\033[1;34m[\033[1;37m{count}\033[1;34m] \033[1;34mProcessing \033[1;37m{url}' + Style.RESET_ALL)

        try:
            response = requests.get(url)
            response.raise_for_status()
        except (requests.exceptions.MissingSchema, requests.exceptions.ConnectionError, requests.exceptions.HTTPError):
            continue

        new_emails = set(re.findall(r'[a-z0-9\.\-+_]+@\w+\.\w+', response.text, re.I))
        emails.update(new_emails)

        soup = BeautifulSoup(response.text, 'html.parser')
        for anchor in soup.find_all('a'):
            link = anchor.get('href', '')

            if link.startswith('/'):
                link = base_url + link
            elif not link.startswith(('http', 'https')):
                link = urllib.parse.urljoin(path, link)

            if link not in urls and link not in scraped_urls:
                urls.append(link)

        try:
            ip = socket.gethostbyname(parts.netloc)
            ips.add(ip)
        except socket.gaierror:
            pass

        try:
            ipv6 = socket.getaddrinfo(parts.netloc, None, socket.AF_INET6)[0][4][0]
            ipv6s.add(ipv6)
        except socket.gaierror:
            pass

        hosts[parts.netloc] = {'ip': ip, 'ipv6': ipv6s}

        server = response.headers.get('Server')
        if server:
            servers.add(server)

        social_media_patterns = {
            'Facebook': r'facebook\.com/[\w\d.-]+',
            'Twitter': r'twitter\.com/[\w\d.-]+',
            'Instagram': r'instagram\.com/[\w\d.-]+',
            'LinkedIn': r'linkedin\.com/[\w\d.-]+'
        }
        for platform, pattern in social_media_patterns.items():
            matches = re.findall(pattern, response.text, re.I)
            social_media[platform].update(matches)

except KeyboardInterrupt:
    print('\n\033[1;31mProcess interrupted by the user.' + Style.RESET_ALL)

print('\n\033[1;34m[\033[1;31m✦\033[1;34m] \033[1;31mResults \033[1;31m:' + Style.RESET_ALL)

print(f'\n\033[1;34m[\033[1;31m+\033[1;34m] \033[1;34mHost Found (\033[1;37m{len(hosts)}\033[1;34m)')
for host, info in hosts.items():
    print(Fore.WHITE + f'{host}, {info["ip"]}, {info["ipv6"]}')

print(f'\n\033[1;34m[\033[1;31m+\033[1;34m] \033[1;34mEmail Found (\033[1;37m{len(emails)}\033[1;34m)')
for email in emails:
    print(Fore.WHITE + f'{email}')

print(f'\n\033[1;34m[\033[1;31m+\033[1;34m] \033[1;34mServer (\033[1;37m{", ".join(servers)}\033[1;34m)')

#print('\n\033[1;31m[\033[1;36m+\033[1;31m] \033[1;34mSocial Media \033[1;31m:')
for platform, links in social_media.items():
    print(f'\n\033[1;34m[\033[1;31m+\033[1;34m] \033[1;34m{platform} Found (\033[1;37m{len(links)}\033[1;34m)')
    for link in links:
        print(Fore.WHITE + f'{link}')