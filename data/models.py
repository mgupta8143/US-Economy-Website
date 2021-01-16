from django.db import models

# Create your models here.
class ForexRates(models.Model):
	EUR_USD = models.CharField(max_length = 10)