from django.db import models

# Create your models here.
class AccountDetails(models.Model):

	UserName = models.CharField(max_length= 100 , primary_key = True)
	FirstName = models.CharField(max_length = 100)
	LastName = models.CharField(max_length = 100)
	Address = models.CharField(max_length=200)
	phone_number = models.BigIntegerField()
	pan_number = models.IntegerField()
	aadhar_number = models.BigIntegerField()
	email = models.EmailField(max_length=100)
	GenderChoices = [('1', 'Male'),('2', 'Female'),('3', 'Others'),]
	Gender = models.CharField(max_length = 1, choices = GenderChoices)
	def __str__(self):
		return self.UserName