import requests
import json
from core.config import METEOSOURCE_API_KEY
from datetime import datetime

url = 'https://www.meteosource.com/api/v1/free/point'


def send_request_get_weather(place_id='Kyiv',
                             sections='current',
                             language='en',
                             units='auto',
                             key=METEOSOURCE_API_KEY):
    req = requests.get(url, params={'place_id': place_id,
                                    'sections': sections,
                                    'language': language,
                                    'units': units,
                                    'key': key})
    response = json.loads(req.text)
    result = dict()
    result['date'] = datetime.now().strftime('%d.%m.%Y')
    result['place_id'] = place_id
    result['timezone'] = response['timezone']
    result['summary'] = response['current']['summary']
    result['temperature'] = response['current']['temperature']
    return result
