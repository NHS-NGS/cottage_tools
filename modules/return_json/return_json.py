import config
import requests

def return_json(self,url):
	'''This function takes a url and will return the response as a json'''
	# if proxy is set in the config file
	if config.proxy:
		response = requests.get(url, headers = {"Authorization": "JWT " + self.token}, proxies = config.proxy) # note space is required after JWT 
	# if no proxy
	else:
		response = requests.get(url, headers = {"Authorization": "JWT " + self.token}) # note space is required after JWT 
	
	# pass this in the json format to the parse_json function
	return response.json()