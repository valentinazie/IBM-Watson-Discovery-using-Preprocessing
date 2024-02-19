import pandas as pd
from dotenv import load_dotenv
import authenticate
import reformatting
import config
import utilities
import logging
from typing import Dict, List

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def fetch_discovery_data() -> Dict:
    """
    Authenticate with IBM Watson Discovery and fetch project data.

    Returs:
    cnc_data: The raw data fetched from the project.
    """
    try:
        discovery = authenticate.authentication()
        project_id = authenticate.get_project_id_by_name(discovery, config.project_name)
        cnc_data = authenticate.fetch_project_data(discovery, project_id)
        return cnc_data
    except Exception as e:
        logging.error(f"An error occurred during Watson Discovery call: {e}")
        raise

def get_output(raw_data: Dict) -> List[Dict]:
    contents_ordered = reformatting.html_extract(raw_data)
    utilities.save_json(contents_ordered, config.FORMATTED_JSON_PATH) 
    result = reformatting.reformat_contents(contents_ordered)
    return result


if __name__ == '__main__':
    wd_raw_data = fetch_discovery_data()
    utilities.save_json(wd_raw_data, config.RAW_JSON_PATH)
    result_bf_json = get_output(wd_raw_data)
    utilities.save_json(result_bf_json, config.REFORMATTED_JSON_PATH)
    elastic_bulk = reformatting.elastic_search_formatting(result_bf_json, config.index_name)
    utilities.save_bulk(elastic_bulk, config.ELASTIC_JSON_PATH)