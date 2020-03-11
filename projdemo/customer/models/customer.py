from django.contrib.postgres.fields import ArrayField, JSONField
from django.db import models


class Customer(models.Model):
    name = models.CharField(null=False, blank=False, max_length=255)
    email = models.EmailField(null=False, blank=False, max_length=255)
    contact_no = models.PositiveIntegerField()
    password = models.CharField(null=False, blank=False, max_length=255)
    extra = JSONField(default=dict, null=True, blank=True)

    class Meta:
        db_table = 'customers'