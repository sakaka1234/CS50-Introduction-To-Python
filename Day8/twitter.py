import re

url = input("What's your URL ?").strip()

if matches := re.search(r"^https?://(?:www\.)?twitter\.(?:com|org)/(.+)$",url,re.IGNORECASE):
    print(f"Username : {matches.group(1)}")