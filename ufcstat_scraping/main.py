# import libraries
import requests
import pandas as pd
from ufc_scraper import get_events, get_fights, get_fights_records


headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.48'}
base_url = 'http://ufcstats.com/statistics/events/completed?page=all'

response = requests.get(base_url, headers=headers)
print(response)


fights = get_fights_records(response, headers)
ufc_fights_records = pd.DataFrame(fights)
ufc_fights_records.to_csv('ufc_fights_records.csv', index=False)
print(ufc_fights_records.head())
