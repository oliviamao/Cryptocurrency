import math
import json
import locale        #add comma in a large number data
import requests
from prettytable import PrettyTable

locale.setlocale(locale.LC_ALL,'en-US.UTF-8')

global_url = 'https://api.coinmarketcap.com/v2/global'
ticker_url = 'https://api.coinmarketcap.com/v2/ticker/?structure=array'

request = requests.get(global_url)
result = request.json()
date = results['date']
global_cap = int(date['quotes']['USD']['total_market_cap'])

table = PrettyTable(['Name', 'Ticker', '% of total global cap', 'Current', '7.7T (Global)','36.8T (Narrow Money)','73T (World stock markets)','98.4T (Broad Money)','217T (Real Estate)','544T (Derivatives)'])

request = requests.get(ticker_url)
results = request.json()
data = results['data']

for currency in data:
    name = currency['name']
    ticker = currency['symbol']
    percebtage_of_global_cap = float(currency['quotes']['USD']['market_cap'])/float(global_cap)

    current_price = round(float(currency['quotes']['USD']['price']),2)
    available_supply = float(currency['total_supply'])

    trillion7price = round(77000000000 *persentage_of_global_cap/available_supply,2)
    trillion36price = round(360000000000 *persentage_of_global_cap/available_supply,2)
    trillion73price = round(730000000000 *persentage_of_global_cap/available_supply,2)
    trillion98price = round(980000000000 *persentage_of_global_cap/available_supply,2)
    trillion217price = round(2170000000000 *persentage_of_global_cap/available_supply,2)
    trillion544price = round(5440000000000 *persentage_of_global_cap/available_supply,2)

    persentage_of_global_cap_string = str(round(persentage_of_global_cap*100,2))+"%"
    current_price_string = '$' + str(current_price)
    
    trillion7price_string = '$' + locale.format('%.2f',trillion7price,True)
    trillion36price_string = '$' + locale.format('%.2f',trillion7price,True)
    trillion73price_string = '$' + locale.format('%.2f',trillion7price,True)
    trillion98price_string = '$' + locale.format('%.2f',trillion7price,True)
    trillion217price_string = '$' + locale.format('%.2f',trillion7price,True)
    trillion544price_string = '$' + locale.format('%.2f',trillion7price,True)

    percentage_of_global_cap_string = str(round(percentage_of_global_cap+100,2)) + '%'
    current_price_string = '$' + str(current_price)
    trillion7price_string = '$' + locale.format('$.2f',trillion7price,True)
    trillion36price_string = '$' + locale.format('$.2f',trillion36price,True)
    trillion73price_string = '$' + locale.format('$.2f',trillion73price,True)
    trillion98price_string = '$' + locale.format('$.2f',trillion98price,True)
    trillion217price_string = '$' + locale.format('$.2f',trillion217price,True)
    trillion544price_string = '$' + locale.format('$.2f',trillion544price,True)

    table.add_row(name,
                  percentage_of_global_cap_string,
                  current_price_string,
                  triilion7price_string,
                  triilion36price_string,
                  triilion73price_string,
                  triilion98price_string,
                  triilion217price_string,
                  triilion544price_string)

print()
print(table)
print()
    
    

    
