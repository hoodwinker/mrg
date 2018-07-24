from requests import get
import json
from datetime import datetime, date as dt, timedelta
import random

api_key = '7ba8d6a5299674afac0f2abd45e410d9'

def get_normal_currency(base='EUR', symbols='USD', date='latest'):
	if isinstance(symbols, list):
		symbols = ','.join(symbols)
		
	if isinstance(date, dt):
		date = date.strftime("%Y-%m-%d")

	url = 'http://data.fixer.io/{date}?base={base}&symbols={symbols}&access_key={key}' \
		.format(base=base, symbols=symbols, date=date, key=api_key)

	r = get(url)
	response = json.loads(r.content)
	return response

def custom_api(base, date, symbols, key):

	url_def = 'http://data.fixer.io/'
	url_def += date if date else ''
	url_def += '?'
	url_def += 'base=' + base if base else ''
	url_def += '&' if base and symbols else ''
	url_def += 'symbols=' + symbols if symbols else ''
	url_def += '&access_key=' + key if key else ''

	r = get(url_def)
	response = json.loads(r.content)
	return response

def get_symbols_list():
	url = 'http://data.fixer.io/api/symbols?access_key={}'.format(api_key)
	r = get(url)
	response = json.loads(r.content)

	list_of_symbols = response.get('symbols')

	return list_of_symbols

def random_date():
	mindate = dt(2000, 1, 1)
	maxdate = datetime.today().date() - timedelta(days=1)
	return (mindate + (maxdate - mindate) * random.random()).strftime("%Y-%m-%d")