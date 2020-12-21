from django.db import models

class ORMProduct(models.Model):
    reference = models.CharField(max_length=30, primary_key=True)
    brand_id = models.CharField(max_length=30)