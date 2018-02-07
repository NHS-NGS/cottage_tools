# return_json
### Module function
This function takes a url which should point to a CIP-API endpoint. It uses the Python Requests module to return the contents of that url as a json file.

### Inputs
When the function is called a url is required to be passed as an input. 
Prior to this function being called an authentication token should be created using the authentication function. This assigns a authentication token to the variable self.token.
This token is used by the requests module to gain access to the CIP-API, therefore self must also be passed as an input to access this variable

The usage is therefore:
> json = return_json.return_json(self,url)

### How the function works 
The requests python module and the config file are imported.
The requests module then performs a get action on the url, specifying the authentication token.
If any proxy settings are defined in the config file these are also passed by the requests module.

### Outputs
The response is returned as a json object

### Proxy settings
A proxy setting may be required to access the CIP-API.
This can be specified in the config file. 
If no proxy settings are required set the config option should be set to False
See http://docs.python-requests.org/en/master/user/advanced/#proxies for further information.

### Dependancies
[requests python module](http://docs.python-requests.org/en/master/)

### Contributors
[@aledj2](https://github.com/aledj2)

### Release
v1.0 - 06/02/2018
