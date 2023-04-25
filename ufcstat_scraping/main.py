import requests
import json
from ufcstat_lxml import get_events

# connect to website
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.48'}
base_url = 'http://ufcstats.com/statistics/events/completed?page=all'

# base_tree = html.fromstring(requests.get(base_url, headers=headers).content)
response = requests.get(base_url, headers=headers)
print(response)


events = get_events(response)

print(events)

