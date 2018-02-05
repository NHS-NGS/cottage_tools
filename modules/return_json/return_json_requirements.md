# return_json Module Project Requirements 
## Participants
    - Product owner: NHS GMCs
    - Team:NHS GMCs
    - Stakeholders:NHS GMCs, Genomics England

## Current Status
_Draft_

## Purpose
This function takes a url and returns the result as a json object.

## Project Goals & Objectives 
    - Goals
        Takes a url and return a json object containing the result.
    - Out of scope / non goals
        The results are not parsed in anyway.
        
## Requirements
| Requirement | Description | Acceptance Criteria | Priority | GitHub Issue(s) |
|-------------|-------------|---------------------|----------|-----------------|
|Python (2.7) with requests module           |    -         |            -         |   -       |                 |
|authentication token (from authentication module)             |     -        |              -       |    -      |           -      |
|config file with proxy settings             |     -        |              -       |    -      |           -      |

### Functional
- Given a url as an input.
- Returns json object
 
### Technical
- Uses the authentication token assigned to self.token by the authentication module.
- Uses the Python requests module.

### Usability 
- Function can be imported by other classes/functions.

