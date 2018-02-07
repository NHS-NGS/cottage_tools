---
---
# return_ir
## Module function
This function has two inputs, the Interpretation Request ID (an integer) and the version number for the interpretation request. These values are used to create the url to the interpretation request which is then accessed using the return_json function.


## Inputs
Two inputs are required:
1. Interpretation_Request_ID
2. IR_version
 

#### Usage 
IR_json = return_ir.return_ir(self, Interpretation_Request_ID, IR_version)
> eg IR_json = return_ir.return_ir(self, 100, 1)

## How the function works 
The interpretation request ID and the version number are incorporated into the url: https://cipapi.genomicsengland.nhs.uk/api/interpretationRequests/Interpretation_Request_ID/IR_version/

This url is then passed to the return_json module which returns the result of that url as an json object.

## Outputs
The contents of the interpretation request endpoint is returned as a json object

## Contributors
[@aledj2](https://github.com/aledj2)

## Release
v1.0 - 07/02/2018
