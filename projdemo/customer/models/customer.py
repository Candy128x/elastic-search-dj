from customer.es_documents.customer_document import CustomerIndex
from django.contrib.postgres.fields import ArrayField, JSONField
from django.core.validators import MinLengthValidator, RegexValidator
from django.db import models


class Customer(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    name = models.CharField(null=False, blank=False, max_length=255)
    email = models.EmailField(null=False, blank=False, unique=True, max_length=255)
    contact_no = models.CharField(default=None, blank=False, max_length=10, validators=[MinLengthValidator(10)])
    password = models.CharField(null=False, blank=False, max_length=255)
    extra = JSONField(default=dict, null=True, blank=True)

    class Meta:
        db_table = 'customers'

    # Add indexing method to BookPublish
    def indexing(self):
        obj = CustomerIndex(meta={'id': self.id}, name=self.name,
                            email=self.email, contact_no=self.contact_no, extra=self.extra)
        return obj.to_dict(include_meta=True)
