import requests
import json

url = "https://api.monobank.ua/bank/currency"
url_nbu = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json"


def send_request_currency_nbu() -> dict:
    req = requests.get(url_nbu)
    response = json.loads(req.text)
    result = {}
    for i in response:
        if i['cc'] == 'USD':
            result['date'] = i['exchangedate']
            result['USD'] = i['rate']
        elif i['cc'] == 'EUR':
            result['EUR'] = i['rate']
    return result
