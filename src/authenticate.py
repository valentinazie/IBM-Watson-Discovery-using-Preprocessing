from dotenv import load_dotenv
import pandas as pd
from ibm_watson import IAMTokenManager
import os
import urllib3
from ibm_watson import DiscoveryV2
from ibm_cloud_sdk_core.authenticators import BearerTokenAuthenticator

def authentication():
    urllib3.disable_warnings()
    load_dotenv()
    iam_token_manager = IAMTokenManager(apikey=os.getenv('API_KEY'))
    token = iam_token_manager.get_token()

    authenticator = BearerTokenAuthenticator(token)

    ## Initialize discovery instance ##
    discovery = DiscoveryV2(
        version='2023-03-31',
        authenticator=authenticator
    )
    discovery.set_service_url('https://api.us-south.discovery.watson.cloud.ibm.com')
    return discovery

def get_project_id_by_name(discovery, project_name):
    discovery.set_disable_ssl_verification(True)

    response=discovery.list_projects().get_result()
    df = pd.DataFrame(response['projects'])
    cnc_project_id = df[df['name']==project_name]['project_id'].values[0]
    return cnc_project_id

def fetch_project_data(discovery, cnc_project_id):
    query_results = discovery.query(
        project_id=cnc_project_id,
        query='',  # Empty query to fetch all documents
        count=2000  # Fetch 2000 documents (max limit)
    ).get_result()
    return query_results

