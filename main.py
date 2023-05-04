import requests

#-----------------------------------------------------------------------------------------------------------------#

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'

currency = 'BTC' #Currency Symbol

params = {
    'symbol': currency,
    'convert': 'USD'
}

headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': 'ae42d262-3a62-41ef-86e5-af052ef8d5f5' #API KEY
}

response = requests.get(url, headers = headers, params = params)
price = response.json()['data']['BTC']['quote']['USD']['price']

#-----------------------------------------------------------------------------------------------------------------#