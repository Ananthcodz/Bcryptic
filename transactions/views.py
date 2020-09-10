from django.shortcuts import render,redirect
from .models import Transactions
from accdetails.models import AccountDetails
from BankingSystem.models import BankingSystem
import random
# Create your views here.
def Transact(request):
	if request.method == 'POST':
		Data = request.POST
		_ID = cardnumber()
		_User = AccountDetails.objects.get(UserName = request.user.username)
		obj = Transactions(Transcation_Id = _ID, Username = _User, Money = Data['Amount'], Type = Data['Type'])
		_obj = BankingSystem.objects.get(Username = _User)
		if Data['Type'] == "1":
			_obj.Balance += int(Data['Amount'])
		else:
			_obj.Balance -= int(Data['Amount'])
		_obj.save()
		obj.save()
		return redirect('BankingSystem')

def cardnumber():
	a = ""
	for i in range(0,16):
			a += str(random.randint(0,9))
	_CCs = Transactions.objects.all()
	no = int(a)
	if Transactions.objects.all().exists():
		_CC = Transactions.objects.all()
		for z in _CCs:
			if z.Transcation_Id == no:
				return cardnumber()
			else:
				return no
	else:
		return no
