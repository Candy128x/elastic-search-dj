# from .utils import BookPublishIndex
from customer.es_documents.customer_document import CustomerIndex
from elasticsearch.helpers import bulk
from elasticsearch import Elasticsearch
from elasticsearch_dsl.connections import connections
from customer.models.customer import Customer
from elasticsearch_dsl import *


connections.create_connection()

def bulk_indexing():
    CustomerIndex.init()
    es = Elasticsearch()
    bulk(client=es, actions=(b.indexing() for b in Customer.objects.all().iterator()))

def search(name):
    s = Search().filter('match', name=name)
    response = s.execute()
    print('---response---', response)
    response_to_dict = (response.to_dict())
    response_to_dict = response_to_dict['hits']['hits']
    print('---response_to_dict---', response_to_dict)
    return response