from customer.api.v1.customer_api_view import CustomerListApiView, CustomerDetailApiView
from django.urls import path



urlpatterns = [
    path('api/v1/', CustomerListApiView.as_view()),
    path('api/v1/<int:pk>/', CustomerDetailApiView.as_view()),
]