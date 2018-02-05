"""
This script targets the client api version 0.4.0 and later
"""
import labkey

def return_labkey_participants(GELID):
	"""
	Recieves a GEL proband ID
	Using credentials in a .netrc file (~/.netrc) it queries labkey for that GELID returning:
	person_identifier_type,forenames,person_identifier,date_of_birth,participant_id,surname
	"""
    server_context = labkey.utils.create_server_context('gmc.genomicsengland.nhs.uk', 'Genomics England Portal/South London/MeRCURy/Rare Diseases/Core', '/labkey', use_ssl=True)
    my_results = labkey.query.select_rows(
        server_context=server_context,
        schema_name='gel_rare_diseases',
        query_name='participant_identifier',
        filter_array=[
            labkey.query.QueryFilter('participant_id', GELID, 'eq') 
        ]
    ) 
    return my_results

if __name__ == "__main__":
    labkey_results = return_labkey_participants(112002698)
    print labkey_results