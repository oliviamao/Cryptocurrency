import json
import requests
from datetime import datetime

global_url = 'https://api.coinmarketcap.com/v2/global/'

request = requests.get(global_url)
results = request.json()

active_cryptocurrencies = results['data']['active_cryptocurrencies']

active_markets = results['data']['active_markets']

bitcoin_persentage = results['data']['bitcoin_percentage_of_market_cap']

last_updated = results['data']['last_updated']

global_cap = int(results['data']['quotes']['USD']['total_market_cap'])

global_volume = int(results['data']['quotes']['USD']['total_volume_24h'])

active_cryptocurrencies_string = "{:,}".format(active_cryptocurrencies)
active_markets_string = "{:,}".format(active_markets)
global_cap_string = "{:,}".format(global_cap)
global_volume_string = "{:,}".format(global_volume)

last_updated_string = datetime.fromtimestamp(last_updated).strftime('%B %d, %Y at %I: %M%p')

print()
print("There are currently "  + str(active_cryptocurrencies_string) + " active_currencies and " + str(active_markets_string) + " active markets.")
print('The global cap of allcrptos is '+ str(global_cap_string) + ' and the 24 global volume is ' + str(global_volume_string) + '.')
print("Bitcoin's total percentage of global cap is " + str(bitcoin_persentage) + '.')
print()
print("This information was last updated on " + str(last_updated_string) + '.')
