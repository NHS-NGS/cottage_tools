""" CIP-API Authentication module """

import requests
import os
import config


class APIAuthentication:

    """ Generate token and and create a requests 'session'
        http://docs.python-requests.org/en/master/user/advanced/#session-objects
    """

    def __init__(self):
		# url to submit user info to generate token
		self.token_url = "https://cipapi.genomicsengland.nhs.uk/api/get-token/"
		# Call modules to generate token
		self.token = self.get_token()
		

    def get_token(self):
		# read username from file (username is defined in gel_report_config)
		with open(os.path.join(config.app_home,config.username),'r') as f:
			user=f.readline()
		#read password from file (pw is defined in gel_report_config)
		with open(os.path.join(config.app_home,config.pw),'r') as f:
			password=f.readline()
		# use requests module to submit the credentials and return the token
		# if proxy is set in the config file:
		if config.proxy:
			return requests.post(self.token_url, {"username": user, "password":password},proxies=config.proxy).json()["token"]
		else:
			return requests.post(self.token_url, {"username": user, "password":password}).json()["token"]


if __name__ == "__main__":
    auth = APIAuthentication()
    print auth.token



