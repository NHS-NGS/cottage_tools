# return_labkey Module Project Requirements 
## Participants
    - Product owner: NHS GMCs
    - Team:NHS GMCs
    - Stakeholders:NHS GMCs, Genomics England

## Current Status
_Draft_

## Purpose
This function takes a GELid and queries Labkey, returning person_identifier_type,forenames,person_identifier,date_of_birth,participant_id,surname
This endpoint contains data which has been _'cleaned'_by Genomics England.

## Project Goals & Objectives 
    - Goals
        Takes a GEL id and return a dictionary containing all results, including  patient demographics (name, DoB, identifier eg NHS Number) taken from Labkey (https://gmc.genomicsengland.nhs.uk/labkey/project/home/begin.view --> login --> GMC --> rare disease --> MerCURy --> Rare disease --> core --> participants )
    - Out of scope / non goals
        The results are not parsed in anyway.
        
## Requirements
| Requirement | Description | Acceptance Criteria | Priority | GitHub Issue(s) |
|-------------|-------------|---------------------|----------|-----------------|
|Python (2.7) with Labkey modules             |    -         |            -         |   -       |                 |
|Active GeL Labkey user account - password saved in .netrc file             |     -        |              -       |    -      |           -      |

### Functional
- Given a GEL ID as an input.
- Queries the participants table as described above.
- Returns a dictionary.
- Any matching data found within the 'rows' key.
 
### Technical
- Uses username and password recorded in files specicified in the ~/.netrc file.
- Uses the Python Labkey module.

### Usability 
- Function can be imported by other classes/functions.

