import requests
import pyodbc
import json
import datetime
import sys
import getopt

# Import local settings
import config as config # config file 
from modules.authentication import authentication
from modules.return_ir_list import return_ir_list
from modules.return_json import return_json


class main():
	def __init__(self):
		# call function to retrieve the api token
		self.token=authentication.APIAuthentication().get_token()
	
	def get_interpretation_list(self):
		json = return_ir_list.return_interpretation_request_list(self,cip="omicia")
		print json["count"]

if __name__ == "__main__":
	main().get_interpretation_list()