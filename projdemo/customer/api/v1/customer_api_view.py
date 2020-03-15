from customer.es_documents.customer_document import CustomerIndex
from customer.models.customer import Customer
from customer.serializers import CustomerSerializer
from datetime import datetime
from django.http import Http404
from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.views import APIView
import requests


class CustomerListApiView(APIView):
    def get(self, request, format=None):
        customers_object = Customer.objects.all().order_by('-id')
        serializer = CustomerSerializer(customers_object, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CustomerDetailApiView(APIView):
    def get_object(self, pk):
        try:
            return Customer.objects.get(pk=pk)
        except Customer.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        customer_object = self.get_object(pk)
        serializer = CustomerSerializer(customer_object)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        customer_object = self.get_object(pk)
        serializer = CustomerSerializer(customer_object, data=request.data)

        # CustomerIndex.init()
        es = Elasticsearch()
        # bulk(client=es, actions=(b.indexing() for b in Customer.objects.all().iterator()))
        # result1 = (b.indexing() for b in Customer.objects.all().iterator())
        # result2 = b
        # print('---result1---', result2)

        # for b in Customer.objects.all().iterator():
        #     print('---b---', b)
        #     print('---b.indexing()---', b.indexing())
        
        # print('---customer_object---', customer_object)
        # print('---customer_object---', customer_object.indexing())

        # obj = CustomerIndex(meta={'id': self.id}, name=self.name,
        #                     email=self.email, contact_no=self.contact_no, extra=self.extra)
        # obj = obj.to_dict(include_meta=True)

        request_data = request.data
        # request_data.update({'id': customer_object.id})
        # request_data.pop('password')
        request_data.update({'entity_type': 'customer'})
        request_data.update({'entity_id': customer_object.id})
        request_data.update({'created_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S')})
        request_data.update({'timestamp': int(datetime.timestamp(datetime.now()))})
        print('---request_data---', request_data)

        url = 'http://localhost:9200/customer-index-2/update-doc/' 
        request_header = {'Content-type': 'application/json'}
        r = requests.post(url, data=request_data, headers=request_header) 
        es_response = r.json()
        print('---es_response---post---', es_response) 


        es_request_data = 0
        # print('---es_request_data---', es_request_data)
        # result2b = CustomerIndex(meta={'id': 121}, **request_data)
        # result2c = result2b.to_dict(include_meta=True)
        # bulk(client=es, actions=(result2c))


        '''
        url = 'http://localhost:9200/first_index/customer/2/_source' 
        r = requests.get(url) 
        es_response = r.json()
        print('---es_response---get---', es_response) 
        '''

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        customer_object = self.get_object(pk)
        customer_object.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
