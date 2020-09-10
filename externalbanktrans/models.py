from django.db import models
from accdetails.models import AccountDetails

class ExternalTransactions(models.Model):
	Transcation_Id = models.BigIntegerField()
	Username = models.ForeignKey(AccountDetails, on_delete = models.DO_NOTHING)
	Money = models.BigIntegerField()
	Type_Choices = [('1','Deposit'),
	('2','Withdraw')]
	Type = models.CharField(max_length=1, choices= Type_Choices)
	Bank_choices = [
    ('1', 'State Bank of India'),
    ('2', 'Central Bank of India'),
    ('3' ,'Swiss Bank '),
    ('4' , 'Bank of Baroda'),
    ('5' , 'HDFC'),
    ('6' , 'Credit one'),
    ('7', 'ICICI')]
	Bank = models.CharField(max_length=1,choices=Bank_choices)
	IFSC = models.BigIntegerField()
