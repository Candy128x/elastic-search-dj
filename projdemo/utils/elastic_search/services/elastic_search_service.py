from datetime import datetime
import requests
import json


class ElasticSearchService:

    def store_customer_updation_query(request_data, entity_type, entity_id):
        print('---store_customer_updation_query---', request_data) 

        url = 'http://localhost:9200/customer-index-2/update-doc/'
        request_data.update({'entity_type': entity_type})
        request_data.update({'entity_id': entity_id})
        request_data.update({'created_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S')})
        request_data.update({'timestamp': int(datetime.timestamp(datetime.now()))})
        print('---store_customer_updation_query---append---', request_data)
        request_header = {'Content-type': 'application/json'}
        r = requests.post(url, data=json.dumps(request_data), headers=request_header) 
        es_response = r.json()

        print('---store_customer_updation_query---es_response---', es_response) 
