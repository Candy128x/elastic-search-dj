from elasticsearch_dsl import DocType, Index, Text, Date
# from django_elasticsearch_dsl.documents import Document
# from customer.models.customer import Customer

'''
customer_index = Index('customers')
customer_index.settings(number_of_shards=1,number_of_replicas=0)


@customer_index.doc_type
class CustomerDocument(DocType):
    name = fields.TextField(
        attr='name',
        fields={
            'suggest': fields.Completion(),
        }
    )
'''


class CustomerIndex(DocType):
    name = Text()
    email = Text()
    contact_no = Text()
    password = Text()
    extra = Text()

    class Meta:
        index = 'customer-index'