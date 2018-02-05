# return_labkey_participants Module Project Requirements 
## Participants
    - Product owner: NHS GMCs
    - Team:NHS GMCs
    - Stakeholders:NHS GMCs, Genomics England

## Current Status
_Draft_

## Purpose
This function takes a gelID from the CIP API and queries GEL's Labkey Production server.
The 'participants' view is queried (schema name = gel_rare_diseases, query name = participant_identifier), filtering where the gelID == labkey Participant ID.
This view has a single record for each participant and contains the columns forenames, surname, date of birth, person identifier type, person identifier and participant_id.
This view can be accessed at https://gmc.genomicsengland.nhs.uk/labkey/project/home/begin.view --> login --> GMC --> rare disease --> MerCURy --> Rare disease --> core --> participants.


## Project Goals & Objectives 
- Goals
    Using the gelID, query LabKey using the LabKey pyuthon module which returns results in a dictionary.
- Out of scope / non goals
    The results are not parsed in anyway.
        
## Requirements
| Requirement | Description | Acceptance Criteria |
|-------------|-------------|---------------------|
|Returns results for a desired participant |-|Dictionary values for 'Row count' and 'rows' are accurate|

### Functional
- The input is a gelID (eg 10000001).
- The participants view is queried, filtering where the gelID matches the labkey participant ID.
- A dictionary is returned, with any matching particpants found within the 'rows' key.
 
### Technical
- An active Labkey account is required with username and password specified in the ~/.netrc file.
- Uses the Python Labkey module (https://github.com/LabKey/labkey-api-python).

### Usability 
- Function can be imported by other classes/functions.