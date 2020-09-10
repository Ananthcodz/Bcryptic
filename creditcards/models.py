from django.db import models
from accdetails.models import AccountDetails
# Create your models here.

class creditcard(models.Model):
	UserName = models.ForeignKey(AccountDetails, on_delete= models.DO_NOTHING)
	credit_cardchoices = [
    ('1', 'State Bank of India'),
    ('2', 'Central Bank of India'),
    ('3' ,'Swiss Bank '),
    ('4' , 'Bank of Baroda'),
    ('5' , 'HDFC'),
    ('6' , 'Credit one'),
    ('7', 'ICICI'),]
	credit_card = models.CharField(max_length=1,choices=credit_cardchoices)
	CardNo = models.BigIntegerField()
	Firstname = models.CharField(max_length=50)
	Lastname = models.CharField(max_length=50)
	CVV = models.IntegerField()
	Purpose = models.CharField(max_length = 100)
	Permitted = models.BooleanField(default = False)
