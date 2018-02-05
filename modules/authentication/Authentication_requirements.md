# Authentication Module Project Requirements 
## Participants
    - Product owner: NHS GMCs
    - Team:NHS GMCs
    - Stakeholders:NHS GMCs, Genomics England

## Current Status
_Draft_

## Purpose
This function provides an authentication token which can be used by the requests modules to query the GEL CIP-API endpoints

## Project Goals & Objectives 
    - Goals
        Taking a username and password return a authentication token from the CIP API get_token end point (https://cipapi.genomicsengland.nhs.uk/api/get-token/)
    - Out of scope / non goals
        Querying any other CIP end points.
        
## Requirements
| Requirement | Description | Acceptance Criteria | Priority | GitHub Issue(s) |
|-------------|-------------|---------------------|----------|-----------------|
|Python (2.7) with Requests and os modules             |    -         |            -         |   -       |                 |
|Active GeL CIP-API user account             |     -        |              -       |    -      |           -      |
|Config file with proxy settings             |     -        |            -         |     -     |           -      |

### Functional
- When function is called a token is returned.
 
### Technical
- Uses username and password recorded in files specicified in the config file.
- Uses Python request module.
- Token is returned as a string.
- Error handling managed.

### Usability 
- Function can be imported by other classes/functions.

