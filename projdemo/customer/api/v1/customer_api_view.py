from customer.es_documents.customer_document import CustomerIndex
from customer.models.customer import Customer
from customer.serializers import CustomerSerializer

from django.http import Http404
from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from utils.elastic_search.services.elastic_search_service import ElasticSearchService


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

        ElasticSearchService.store_customer_updation_query(request.data, 'customer', customer_object.id)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        customer_object = self.get_object(pk)
        customer_object.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
