from django.shortcuts import render,redirect
from .models import ExternalTransactions
from accdetails.models import AccountDetails
from BankingSystem.models import BankingSystem
import random
# Create your views here.
def ExtTransact(request):
	if request.method == 'POST':
		Data = request.POST
		_ID = cardnumber()
		_User = AccountDetails.objects.get(UserName = request.user.username)
		obj = ExternalTransactions(Transcation_Id = _ID, Username = _User, Money = Data['Amount'], Type = Data['Type'], IFSC = Data['IFSC'], Bank = Data['CreditCard'])
		_obj = BankingSystem.objects.get(Username = _User)
		if Data['Type'] == "2":
			_obj.Balance += int(Data['Amount'])
		elif Data['Type'] == "1":
			_obj.Balance -= int(Data['Amount'])
		_obj.save()
		obj.save()
	return redirect('BankingSystem')

def cardnumber():
	a = ""
	for i in range(0,9):
		a += str(random.randint(0,9))
	_CCs = ExternalTransactions.objects.all()
	no = int(a)
	if ExternalTransactions.objects.all().exists():
		_CC = ExternalTransactions.objects.all()
		for z in _CCs:
			if z.Transcation_Id == no:
				return cardnumber()
			else:
				return no
	else:
		return no