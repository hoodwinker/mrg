from datetime import datetime, date as dt, timedelta
import pytest
import random
from api import get_normal_currency, custom_api, get_symbols_list, random_date, api_key

#################	NORMAL TESTS

@pytest.mark.parametrize("r_symbol", ['RUB'])
def test_custom_date(r_symbol):
	s_date = random_date()
	a = get_normal_currency(date=s_date, symbols=r_symbol)

	assert a.get('success') == True
	assert a.get('base') == 'EUR' #assert correct base
	
	rates = a.get('rates') 
	assert len(list(rates.values())) == 1 #assert symbol is requested symbol
	assert rates.get(r_symbol, '') != '' #assert date is requested date

	r_date = a.get('date')
	assert  r_date ==  s_date #assert date is requested date

def test_latest():
	latest_a = get_normal_currency(date='latest')

	assert latest_a.get('success') == True
	assert latest_a.get('base') == 'EUR' #assert correct base
	
	rates = latest_a.get('rates')
	random_rate = random.choice(list(rates.values()))
	assert isinstance(int(random_rate), int) #assert correct rate

	latest_date = latest_a.get('date')
	assert (datetime.today() - datetime.strptime(latest_date, "%Y-%m-%d")).days < 2 #assert latest_date is latest date

def test_symbols_count():
	list_of_symbols = get_symbols_list()
	arr_symbols = list(list_of_symbols.keys())

	latest_a = get_normal_currency(symbols=arr_symbols)
	assert len(latest_a.get('rates')) == len(arr_symbols)

#################	SYMBOLS VALUE

def test_no_symbols_parameter():
	base, date, symbols, key = ['EUR', 'latest', None, api_key]
	a = custom_api(base, date, symbols, key)

	assert a.get('success') == True

def test_empty_symbols_value():
	base, date, symbols, key = ['EUR', 'latest', '', api_key]
	a = custom_api(base, date, symbols, key)

	assert a.get('success') == True

def test_invalid_symbols_value():
	base, date, symbols, key = ['EUR', 'latest', 'AAA', api_key]

	a = custom_api(base, date, symbols, key)
	assert a.get('success') == False

#################	ACCESS_KEY VALUE

def test_latest_no_access_key_parameter():
	base, date, symbols, key = ['EUR', 'latest', 'USD', None]

	a = custom_api(base, date, symbols, key)
	print(a)
	assert a.get('success') == False
	assert a.get('rates', '') == ''

def test_latest_empty_access_key_value():
	base, date, symbols, key = ['EUR', 'latest', 'USD', '']

	a = custom_api(base, date, symbols, key)
	assert a.get('success') == False
	assert a.get('rates', '') == ''

def test_latest_invalid_access_key_value():
	base, date, symbols, key = ['EUR', 'latest', 'USD', '123456']

	a = custom_api(base, date, symbols, key)
	assert a.get('success') == False
	assert a.get('rates', '') == ''

def test_custom_no_access_key_parameter():
	base, date, symbols, key = ['EUR', random_date(), 'USD', None]

	a = custom_api(base, date, symbols, key)
	assert a.get('success') == False
	assert a.get('rates', '') == ''

def test_custom_empty_access_key_value():
	base, date, symbols, key = ['EUR', random_date(), 'USD', '']

	a = custom_api(base, date, symbols, key)
	assert a.get('success') == False
	assert a.get('rates', '') == ''

def test_custom_invalid_access_key_value():
	base, date, symbols, key = ['EUR', random_date(), 'USD', '123456']

	a = custom_api(base, date, symbols, key)
	assert a.get('success') == False
	assert a.get('rates', '') == ''

#################	BASE VALUE

def test_no_base_parameter():
	base, date, symbols, key = [None, 'latest', 'USD', api_key]

	a = custom_api(base, date, symbols, key)
	assert a.get('success') == True
	assert a.get('base') == 'EUR'

def test_empty_base_value():
	base, date, symbols, key = ['', 'latest', 'USD', api_key]

	a = custom_api(base, date, symbols, key)
	assert a.get('success') == True
	assert a.get('base') == 'EUR'

def test_two_base_values():
	base, date, symbols, key = ["EUR, USD", 'latest', 'USD', api_key]

	a = custom_api(base, date, symbols, key)
	assert a.get('success') == False

def test_forbidden_base_value():
	base, date, symbols, key = ['USD', 'latest', 'USD', api_key]

	a = custom_api(base, date, symbols, key)
	assert a.get('success') == False

def test_invalid_base_value():
	base, date, symbols, key = ['1', 'latest', 'USD', api_key]

	a = custom_api(base, date, symbols, key)
	assert a.get('success') == False

#################	DATE VALUE

def test_no_date_endpoint():
	base, date, symbols, key = ['EUR', None, 'USD', api_key]

	try:
		a = custom_api(base, date, symbols, key)
		raise AssertionError
	except:
		pass

def test_two_date_values():
	two_dates = random_date() + " " + random_date()
	base, date, symbols, key = ['EUR', two_dates, 'USD', api_key]

	a = custom_api(base, date, symbols, key)
	assert a.get('success') == False

def test_invalid_date_value():
	base, date, symbols, key = ['EUR', '2016', 'USD', api_key]

	a = custom_api(base, date, symbols, key)
	assert a.get('success') == False

def test_min_date_value():
	min_date = dt(1999, 1, 1).strftime("%Y-%m-%d")
	base, date, symbols, key = ['EUR', min_date, 'USD', api_key]

	a = custom_api(base, date, symbols, key)
	assert a.get('success') == True

def test_below_min_date_value():
	below_min_date = dt(1998, 12, 31).strftime("%Y-%m-%d")
	base, date, symbols, key = ['EUR', below_min_date, 'USD', api_key]

	a = custom_api(base, date, symbols, key)
	assert a.get('success') == False

def test_max_date_value():
	max_date = datetime.today() + timedelta(days=1)
	max_date = max_date.strftime("%Y-%m-%d")

	base, date, symbols, key = ['EUR', max_date, 'USD', api_key]

	a = custom_api(base, date, symbols, key)
	assert a.get('success') == False