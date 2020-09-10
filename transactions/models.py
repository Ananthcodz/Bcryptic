from django.db import models
from accdetails.models import AccountDetails
# Create your models here.
class Transactions(models.Model):
	Transcation_Id = models.BigIntegerField()
	Username = models.ForeignKey(AccountDetails, on_delete = models.DO_NOTHING)
	Money = models.BigIntegerField()
	Type_Choices = [('1','Deposit'),
	('2','Withdraw')]
	Type = models.CharField(max_length=1, choices= Type_Choices)
