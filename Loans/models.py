from django.db import models
from accdetails.models import AccountDetails
# Create your models here.
class Loans(models.Model):
	Recipent = models.ForeignKey(AccountDetails, on_delete = models.CASCADE)
	Location = models.CharField(max_length=50)
	DOB = models.DateField()
	mobile_number = models.IntegerField()
	purpose= models.CharField(max_length=100)
	Amount = models.IntegerField()
	Interest= models.IntegerField()
	collateral_choices= [
	('1', 'House'),
	('2', 'Land'),
	('3', 'Others'),]
	collateral = models.CharField(max_length=1,choices=collateral_choices)
	Approved = models.BooleanField(default = False)
