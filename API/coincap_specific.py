import requests
import json

convert = "USD"

listings_url = 'https://api.coinmarketcap.com/v2/listings/'
url_end = '?structure=array&convert=' + convert
request = requests.get(listings_url)
results = request.json()

data = results['data']

ticker_url_pairs = {}
for currency in data:
    symbol = currency['symbol']
    url = currency['id']
    ticker_url_pairs[symbol] = url

#print(ticker_url_pairs)

while True:

    print()
    choice = input("Enter the ticker symbol of a cryptocurrency: ").upper()

    ticker_url = 'https://api.coinmarketcap.com/v2/ticker/' + str(ticker_url_pairs[choice]) + '/' + url_end
    request = requests.get(listings_url)
    results = request.json()
    
    #print(json.dumps(results, sort_keys=True, indent=4))
    
    data = results['data'][0]
                   
