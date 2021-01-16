from django.shortcuts import render
import requests
import json
import dateutil.parser, pytz
from bs4 import BeautifulSoup
#NewConfirmed TotalConfirmed NewDeaths TOtal Deaths NewRecovered TotalRecovered
# Create your views here.


def about(req):
	return render(req, 'data/about.html')

def gdp(req):
	context = {}
	return render(req, 'data/gdp.html', context)

def covid(req):
	response = requests.get('https://api.covid19api.com/summary')
	json_data = json.loads(response.text)
	context = {}
	for idx, val in enumerate(json_data["Countries"]):
		x = val['Country']
		if x == "Russian Federation":
			x = "Russia"
		elif x == "Viet Nam":
			x = "Vietnam"
		elif x == "Korea (North)":
			x = "North Korea"
		elif x == "Korea (South)":
			x = "South Korea"
		elif x == "Côte d'Ivoire":
			x = "Ivory Coast"
		elif x == "Congo (Brazzaville)":
			x = "Republic of the Congo"
		elif x == "Congo (Kinshasa)":
			x = "Democratic Republic of the Congo"
		elif x == "Tanzania, United Republic of":
			x = "United Republic of Tanzania"
		elif x == "Eritrea":
			x = "Somaliland"
		elif x == "Lao PDR":
			x = "Laos"
		elif x == "Iran, Islamic Republic of":
			x = "Iran"
		elif x == "Czech Republic":
			x = "Czechia"
		elif x == "Serbia":
			x = "Republic of Serbia"
		elif x == "Macedonia, Republic of":
			x = "Macedonia"
		elif x == "Republic of Kosovo":
			x = "Kosovo"
		elif x == "Venezuela (Bolivarian Republic)":
			x = "Venezuela"
		elif x == "Taiwan, Republic of China":
			x = "Taiwan"
		elif x == "Syrian Arab Republic (Syria)":
			x = "Syria"
		context[x + "_CONFIRMED"] = str(val['TotalConfirmed'])
		context[x + "_DEATHS"] = str(val['TotalDeaths'])
		context[x + "_RECOVERED"] = str(val['TotalRecovered'])
		context[x + "_NEW_CONFIRMED"] = str(val['NewConfirmed'])
		context[x + "_NEW_DEATHS"] = str(val['NewDeaths'])
		context[x + "_NEW_RECOVERED"] = str(val['NewRecovered'])
		context[x + "_DATE"] = str(dateutil.parser.parse(str(val['Date'])).astimezone(pytz.timezone("Canada/Eastern"))) + " E.S.T"
	print(context)
	return render(req, 'data/covid.html', {"context": context})


def government_spending(req):
	return render(req, 'data/government_spending.html')

def income(req):
	rates = {
		"Alabama_AVG": 0,
		"Alaska_AVG": 0,
		"Arizona_AVG": 0,
		"Arkansas_AVG": 0,
		"California_AVG": 0,
		"Colorado_AVG": 0,
		"Connecticut_AVG": 0,
		"Delaware_AVG": 0,
		"District_of_Columbia_AVG": 0,
		"Florida_AVG": 0,
		"Georgia_AVG": 0,
		"Hawaii_AVG": 0,
		"Idaho_AVG": 0,
		"Illinois_AVG": 0,
		"Indiana_AVG":0,
		"Iowa_AVG": 0,
		"Kansas_AVG": 0,
		"Kentucky_AVG": 0,
		"Louisiana_AVG": 0,
		"Maine_AVG": 0,
		"Maryland_AVG": 0,
		"Massachusetts_AVG": 0,
		"Michigan_AVG": 0,
		"Minnesota_AVG": 0,
		"Mississippi_AVG": 0,
		"Missouri_AVG": 0,
		"Montana_AVG": 0,
		"Nebraska_AVG": 0,
		"Nevada_AVG": 0,
		"New_Hampshire_AVG": 0,
		"New_Jersey_AVG": 0,
		"New_Mexico_AVG": 0,
		"New_York_AVG": 0,
		"North_Carolina_AVG": 0,
		"North_Dakota_AVG": 0,
		"Ohio_AVG": 0,
		"Oklahoma_AVG": 0,
		"Oregon_AVG": 0,
		"Pennsylvania_AVG": 0,
		"Rhode_Island_AVG": 0,
		"South_Carolina_AVG": 0,
		"South_Dakota_AVG": 0,
		"Tennessee_AVG": 0,
		"Texas_AVG": 0,
		"Utah_AVG": 0,
		"Vermont_AVG": 0,
		"Virginia_AVG": 0,
		"Washington_AVG": 0,
		"West_Virginia_AVG": 0,
		"Wisconsin_AVG": 0,
		"Wyoming_AVG": 0,
		"Alabama_MEDIAN": 0,
		"Alaska_MEDIAN": 0,
		"Arizona_MEDIAN": 0,
		"Arkansas_MEDIAN": 0,
		"California_MEDIAN": 0,
		"Colorado_MEDIAN": 0,
		"Connecticut_MEDIAN": 0,
		"Delaware_MEDIAN": 0,
		"District_of_Columbia_MEDIAN": 0,
		"Florida_MEDIAN": 0,
		"Georgia_MEDIAN": 0,
		"Hawaii_MEDIAN": 0,
		"Idaho_MEDIAN": 0,
		"Illinois_MEDIAN": 0,
		"Indiana_MEDIAN":0,
		"Iowa_MEDIAN": 0,
		"Kansas_MEDIAN": 0,
		"Kentucky_MEDIAN": 0,
		"Louisiana_MEDIAN": 0,
		"Maine_MEDIAN": 0,
		"Maryland_MEDIAN": 0,
		"Massachusetts_MEDIAN": 0,
		"Michigan_MEDIAN": 0,
		"Minnesota_MEDIAN": 0,
		"Mississippi_MEDIAN": 0,
		"Missouri_MEDIAN": 0,
		"Montana_MEDIAN": 0,
		"Nebraska_MEDIAN": 0,
		"Nevada_MEDIAN": 0,
		"New_Hampshire_MEDIAN": 0,
		"New_Jersey_MEDIAN": 0,
		"New_Mexico_MEDIAN": 0,
		"New_York_MEDIAN": 0,
		"North_Carolina_MEDIAN": 0,
		"North_Dakota_MEDIAN": 0,
		"Ohio_MEDIAN": 0,
		"Oklahoma_MEDIAN": 0,
		"Oregon_MEDIAN": 0,
		"Pennsylvania_MEDIAN": 0,
		"Rhode_Island_MEDIAN": 0,
		"South_Carolina_MEDIAN": 0,
		"South_Dakota_MEDIAN": 0,
		"Tennessee_MEDIAN": 0,
		"Texas_MEDIAN": 0,
		"Utah_MEDIAN": 0,
		"Vermont_MEDIAN": 0,
		"Virginia_MEDIAN": 0,
		"Washington_MEDIAN": 0,
		"West_Virginia_MEDIAN": 0,
		"Wisconsin_MEDIAN": 0,
		"Wyoming_MEDIAN": 0,
	}
	result = requests.get("https://dqydj.com/average-income-by-state-median-top-percentiles/")
	src = result.content
	soup = BeautifulSoup(src)
	spans = soup.find_all("td")
	i = 3
	for key in rates:
		if i % 2 == 1:
			rates[key] = spans[i].text.replace(",","").replace("$","")
			if i == 103:
				i = 105
			i += 2
	#i is 103
	return render(req, 'data/income.html', rates)

def unemployment(req):
	rates = {
		"Alabama": 0,
		"Alaska": 0,
		"Arizona": 0,
		"Arkansas": 0,
		"California": 0,
		"Colorado": 0,
		"Connecticut": 0,
		"Delaware": 0,
		"District_of_Columbia": 0,
		"Florida": 0,
		"Georgia": 0,
		"Hawaii": 0,
		"Idaho": 0,
		"Illinois": 0,
		"Indiana":0,
		"Iowa": 0,
		"Kansas": 0,
		"Kentucky": 0,
		"Louisiana": 0,
		"Maine": 0,
		"Maryland": 0,
		"Massachusetts": 0,
		"Michigan": 0,
		"Minnesota": 0,
		"Mississippi": 0,
		"Missouri": 0,
		"Montana": 0,
		"Nebraska": 0,
		"Nevada": 0,
		"New_Hampshire": 0,
		"New_Jersey": 0,
		"New_Mexico": 0,
		"New_York": 0,
		"North_Carolina": 0,
		"North_Dakota": 0,
		"Ohio": 0,
		"Oklahoma": 0,
		"Oregon": 0,
		"Pennsylvania": 0,
		"Rhode_Island": 0,
		"South_Carolina": 0,
		"South_Dakota": 0,
		"Tennessee": 0,
		"Texas": 0,
		"Utah": 0,
		"Vermont": 0,
		"Virginia": 0,
		"Washington": 0,
		"West_Virginia": 0,
		"Wisconsin": 0,
		"Wyoming": 0,
		"US": 0,
		"US_EMPLOYED": 0,
		"US_UNEMPLOYED": 0,
		"US_TOTAL": 0
	}
	result = requests.get("https://www.bls.gov/web/laus/lauhsthl.htm")
	src = result.content
	soup = BeautifulSoup(src)
	spans = soup.find_all("span")
	y = []
	for span in spans:
		if span.has_attr("class") and span['class'][0].find('datavalue') == 0:
			y.append(span.text)
	z = []
	for idx,val in enumerate(y):
		if idx % 5 == 0:
			z.append(val)
	i = 0
	for key in rates:
		rates[key] = z[i]
		i += 1
		if i == 51:
			break
	result = requests.get("http://www.dlt.ri.gov/lmi/laus/us/usadj.htm")
	src = result.content
	soup = BeautifulSoup(src)
	spans = soup.find_all("td")
	y = []
	reached = False
	for span in spans:
		if span.text.find("2020") == 0:
			reached = True
		if reached == True:
			y.append(span.text)
	rates["US"] = y[4]
	rates["US_EMPLOYED"] = y[2]
	rates["US_UNEMPLOYED"] = y[3]
	rates["US_TOTAL"] = y[1]
	return render(req, 'data/unemployment.html', rates)


def exchange_rates(req):
	return render(req, 'data/exchange_rates.html')

def data_rates(req):
	rates = {
		"EUR_USD": 0, 
		"Bitcoin_USD": 0,
		"Ethereum_USD": 0,
		"USD_JPN": 0,
		"GBP_USD": 0,
		"AUD_USD": 0,
		"NZD_USD": 0,
		"USD_CNY": 0,
		"USD_HKD": 0,
		"USD_SGD": 0,
		"USD_INR": 0,
		"USD_MXN": 0,
		"USD_PHP": 0,
		"USD_IDR": 0,
		"USD_THB": 0,
		"USD_MYR": 0,
		"USD_ZAR": 0,
		"USD_RUB": 0,
		"EUR_USD_CHANGE": 0, 
		"Bitcoin_USD_CHANGE": 0,
		"Ethereum_USD_CHANGE": 0,
		"USD_JPN_CHANGE": 0,
		"GBP_USD_CHANGE": 0,
		"AUD_USD_CHANGE": 0,
		"NZD_USD_CHANGE": 0,
		"USD_CNY_CHANGE": 0,
		"USD_HKD_CHANGE": 0,
		"USD_SGD_CHANGE": 0,
		"USD_INR_CHANGE": 0,
		"USD_MXN_CHANGE": 0,
		"USD_PHP_CHANGE": 0,
		"USD_IDR_CHANGE": 0,
		"USD_THB_CHANGE": 0,
		"USD_MYR_CHANGE": 0,
		"USD_ZAR_CHANGE": 0,
		"USD_RUB_CHANGE": 0,
		"EUR_USD_CHANGE": 0, 
		"Bitcoin_USD_CHANGE_PERCENT": 0,
		"Ethereum_USD_CHANGE_PERCENT": 0,
		"USD_JPN_CHANGE_PERCENT": 0,
		"GBP_USD_CHANGE_PERCENT": 0,
		"AUD_USD_CHANGE_PERCENT": 0,
		"NZD_USD_CHANGE_PERCENT": 0,
		"USD_CNY_CHANGE_PERCENT": 0,
		"USD_HKD_CHANGE_PERCENT": 0,
		"USD_SGD_CHANGE_PERCENT": 0,
		"USD_INR_CHANGE_PERCENT": 0,
		"USD_MXN_CHANGE_PERCENT": 0,
		"USD_PHP_CHANGE_PERCENT": 0,
		"USD_IDR_CHANGE_PERCENT": 0,
		"USD_THB_CHANGE_PERCENT": 0,
		"USD_MYR_CHANGE_PERCENT": 0,
		"USD_ZAR_CHANGE_PERCENT": 0,
		"USD_RUB_CHANGE_PERCENT": 0,
		"USDX": 0,
	}
	result = requests.get("https://finance.yahoo.com/currencies")
	src = result.content
	soup = BeautifulSoup(src)
	spans = soup.find_all("td")
	for span in spans:
		if span.has_attr('data-reactid'):
			if span['data-reactid'].find("72") == 0:
				rates["EUR_USD"] = float(span.text.replace(',',''))
			elif span['data-reactid'].find("44") == 0:
				rates["Bitcoin_USD"] = float(span.text.replace(',',''))
			elif span['data-reactid'].find("58") == 0:
				rates["Ethereum_USD"] = float(span.text.replace(',',''))
			elif span['data-reactid'].find("86") == 0:
				rates["USD_JPN"] = float(span.text.replace(',',''))
			elif span['data-reactid'].find("100") == 0:
				rates["GBP_USD"] = float(span.text.replace(',',''))
			elif span['data-reactid'].find("114") == 0:
				rates["AUD_USD"] = float(span.text.replace(',',''))
			elif span['data-reactid'].find("128") == 0:
				rates["NZD_USD"] = float(span.text.replace(',',''))
			elif span['data-reactid'].find("254") == 0:
				rates["USD_CNY"] = float(span.text.replace(',',''))
			elif span['data-reactid'].find("268") == 0:
				rates["USD_HKD"] = float(span.text.replace(',',''))
			elif span['data-reactid'].find("282") == 0:
				rates["USD_SGD"] = float(span.text.replace(',',''))
			elif span['data-reactid'].find("296") == 0:
				rates["USD_INR"] = float(span.text.replace(',',''))
			elif span['data-reactid'].find("310") == 0:
				rates["USD_MXN"] = float(span.text.replace(',',''))
			elif span['data-reactid'].find("324") == 0:
				rates["USD_PHP"] = float(span.text.replace(',',''))
			elif span['data-reactid'].find("338") == 0:
				rates["USD_IDR"] = float(span.text.replace(',',''))
			elif span['data-reactid'].find("352") == 0:
				rates["USD_THB"] = float(span.text.replace(',',''))
			elif span['data-reactid'].find("366") == 0:
				rates["USD_MYR"] = float(span.text.replace(',',''))
			elif span['data-reactid'].find("380") == 0:
				rates["USD_ZAR"] = float(span.text.replace(',',''))
			elif span['data-reactid'].find("394") == 0:
				rates["USD_RUB"] = float(span.text.replace(',',''))
	spans = soup.find_all("span")
	y = 0
	for span in spans:
		if span.has_attr('data-reactid'):
			if span['data-reactid'].find("74") == 0:
				rates["EUR_USD_CHANGE"] = float(span.text.replace(',','').replace('%',''))
			elif span['data-reactid'].find("46") == 0:
				rates["Bitcoin_USD_CHANGE"] = float(span.text.replace(',','').replace('%',''))
			elif span['data-reactid'].find("60") == 0:
				rates["Ethereum_USD_CHANGE"] = float(span.text.replace(',','').replace('%',''))
			elif span['data-reactid'].find("88") == 0:
				rates["USD_JPN_CHANGE"] = float(span.text.replace(',','').replace('%',''))
			elif span['data-reactid'].find("102") == 0:
				rates["GBP_USD_CHANGE"] = float(span.text.replace(',','').replace('%',''))
			elif span['data-reactid'].find("116") == 0:
				rates["AUD_USD_CHANGE"] = float(span.text.replace(',','').replace('%',''))
			elif span['data-reactid'].find("130") == 0:
				rates["NZD_USD_CHANGE"] = float(span.text.replace(',','').replace('%',''))
			elif span['data-reactid'].find("256") == 0:
				rates["USD_CNY_CHANGE"] = float(span.text.replace(',','').replace('%',''))
			elif span['data-reactid'].find("270") == 0:
				rates["USD_HKD_CHANGE"] = float(span.text.replace(',','').replace('%',''))
			elif span['data-reactid'].find("284") == 0:
				rates["USD_SGD_CHANGE"] = float(span.text.replace(',','').replace('%',''))
			elif span['data-reactid'].find("298") == 0:
				rates["USD_INR_CHANGE"] = float(span.text.replace(',','').replace('%',''))
			elif span['data-reactid'].find("312") == 0:
				rates["USD_MXN_CHANGE"] = float(span.text.replace(',','').replace('%',''))
			elif span['data-reactid'].find("326") == 0:
				rates["USD_PHP_CHANGE"] = float(span.text.replace(',','').replace('%',''))
			elif span['data-reactid'].find("340") == 0:
				rates["USD_IDR_CHANGE"] = float(span.text.replace(',','').replace('%',''))
			elif span['data-reactid'].find("354") == 0:
				rates["USD_THB_CHANGE"] = float(span.text.replace(',','').replace('%',''))
			elif span['data-reactid'].find("368") == 0:
				rates["USD_MYR_CHANGE"] = float(span.text.replace(',','').replace('%',''))
			elif span['data-reactid'].find("382") == 0:
				rates["USD_ZAR_CHANGE"] = float(span.text.replace(',','').replace('%',''))
			elif span['data-reactid'].find("396") == 0:
				rates["USD_RUB_CHANGE"] = float(span.text.replace(',','').replace('%',''))
			elif span['data-reactid'].find("76") == 0:
				rates["EUR_USD_CHANGE_PERCENT"] = float(span.text.replace(',','').replace('%',''))
			elif span['data-reactid'].find("48") == 0:
				rates["Bitcoin_USD_CHANGE_PERCENT"] = float(span.text.replace(',','').replace('%',''))
			elif span['data-reactid'].find("62") == 0:
				rates["Ethereum_USD_CHANGE_PERCENT"] = float(span.text.replace(',','').replace('%',''))
			elif span['data-reactid'].find("90") == 0:
				rates["USD_JPN_CHANGE_PERCENT"] = float(span.text.replace(',','').replace('%',''))
			elif span['data-reactid'].find("104") == 0:
				rates["GBP_USD_CHANGE_PERCENT"] = float(span.text.replace(',','').replace('%',''))
			elif span['data-reactid'].find("118") == 0:
				rates["AUD_USD_CHANGE_PERCENT"] = float(span.text.replace(',','').replace('%',''))
			elif span['data-reactid'].find("132") == 0:
				rates["NZD_USD_CHANGE_PERCENT"] = float(span.text.replace(',','').replace('%',''))
			elif span['data-reactid'].find("258") == 0:
				rates["USD_CNY_CHANGE_PERCENT"] = float(span.text.replace(',','').replace('%',''))
			elif span['data-reactid'].find("272") == 0:
				rates["USD_HKD_CHANGE_PERCENT"] = float(span.text.replace(',','').replace('%',''))
			elif span['data-reactid'].find("286") == 0:
				rates["USD_SGD_CHANGE_PERCENT"] = float(span.text.replace(',','').replace('%',''))
			elif span['data-reactid'].find("300") == 0:
				rates["USD_INR_CHANGE_PERCENT"] = float(span.text.replace(',','').replace('%',''))
			elif span['data-reactid'].find("314") == 0:
				rates["USD_MXN_CHANGE_PERCENT"] = float(span.text.replace(',','').replace('%',''))
			elif span['data-reactid'].find("328") == 0:
				rates["USD_PHP_CHANGE_PERCENT"] = float(span.text.replace(',','').replace('%',''))
			elif span['data-reactid'].find("342") == 0:
				rates["USD_IDR_CHANGE_PERCENT"] = float(span.text.replace(',','').replace('%',''))
			elif span['data-reactid'].find("356") == 0:
				rates["USD_THB_CHANGE_PERCENT"] = float(span.text.replace(',','').replace('%',''))
			elif span['data-reactid'].find("370") == 0:
				rates["USD_MYR_CHANGE_PERCENT"] = float(span.text.replace(',','').replace('%',''))
			elif span['data-reactid'].find("384") == 0:
				rates["USD_ZAR_CHANGE_PERCENT"] = float(span.text.replace(',','').replace('%',''))
			elif span['data-reactid'].find("398") == 0:
				rates["USD_RUB_CHANGE_PERCENT"] = float(span.text.replace(',','').replace('%',''))
	result = requests.get("https://finance.yahoo.com/quote/DX-Y.NYB/")
	src = result.content
	soup = BeautifulSoup(src)
	spans = soup.find_all("span")
	for span in spans:
		if span.has_attr('data-reactid'):
			if span['data-reactid'].find("14") == 0 and span.has_attr('class'):
				rates["USDX"] = float(span.text.replace(',','').replace('%',''))
	return render(req, 'data/rate_data.html', rates)


