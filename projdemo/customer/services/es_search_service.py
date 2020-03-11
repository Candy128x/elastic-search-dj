# from .utils import BookPublishIndex
from customer.es_documents.customer_document import CustomerIndex
from elasticsearch.helpers import bulk
from elasticsearch import Elasticsearch
from customer.models.customer import Customer
from elasticsearch_dsl import *

......

def bulk_indexing():
    CustomerIndex.init()
    es = Elasticsearch()
    bulk(client=es, actions=(b.indexing() for b in Customer.objects.all().iterator()))