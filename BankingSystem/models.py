from django.db import models
from accdetails.models import AccountDetails
# Create your models here.
class BankingSystem(models.Model):
	Username = models.ForeignKey(AccountDetails, on_delete = models.CASCADE)
	Balance=models.BigIntegerField()