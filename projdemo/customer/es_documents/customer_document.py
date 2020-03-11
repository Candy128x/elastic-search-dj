from django_elasticsearch_dsl import (DocType, fields, Index,)
from customer.models.customer import (Customer)


customer_index = Index('customers')
customer_index.settings(number_of_shards=1,number_of_replicas=0)