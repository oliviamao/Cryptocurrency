import json
import requests

ticker_url = 'https://api.coinmarketcap.com/v2/ticker/?structure=array'

limit = 100
start = 1
sort = 'id'
convert = 'USD'

choice = input('Do you want to enter any custom parameters?(Y/N): ').strip().upper()

if choice == 'Y':
    limit = input('What is the custom limit?: ')
    start = input('Whar is the custom atart numer?: ')
    sort = input('What do you want to sort by?: ')
    convert = input('What is your local currency?: ')

ticker_url += '&limit' + str(limit) + '&sort' + sort +'&start' + str(start) + '&convert' + convert

request = requests.get(ticker_url)
results = request.json()

print(json.dumps(results, sort_keys=True, indent=4))

data = results['data']

print()
for currency in data:
     rank = currency['rank']
     name = currency['name']
     symbol = currency['symbol']

     circulating_supply = int(currency['circulating_supply'])
     total_supply = int(currency['total_supply'])

     quotes = currency['quotes'][convert]
     market_cap = quotes['market_cap']
     hour_change = quotes['percent_change_1h']
     day_change = quotes['percent_change_24h']
     week_change = quotes['percent_change_7d']
     price = quotes['price']
     volume = quotes['volume_24h']

     volume_string = '{:,}'.format(volume)
     market_cap_string = '{:,}'.format(market_cap)
     circulating_supply_string = '{:,}'.format(circulating_supply)
     total_supply_string = '{:,}'.format(total_supply)

     print(str(rank) + ': ' + name + '(' + symbol + ')')
     print('Market cap: ' + market_cap_string)
     print('Price: $' + str(price))
     print('24h Volume: $' + volume_string)
     print('Hour change: ' + str(hour_change) + '%')
     print('Day change: '+ str(day_change)+ '%' )
     print('Week change' + str(week_change) + '%')
     print('Total supply' + total_supply_string)
     print('Circulating supply: ' + circulating_supply_string)
     print('Percentage of coins in circulation: ' + str(int(circulating_supply / total_supply * 100)))
     print()

     choice = input('Again?(y/n): ')

     if choice == 'n':
         break
