from django.shortcuts import render,redirect
from .models import BankingSystem
from accdetails.models import AccountDetails
from transactions.models import Transactions
from externalbanktrans.models import ExternalTransactions
# Create your views here.
def Banking_System(request):
	_Obj = AccountDetails.objects.get(UserName = request.user.username)
	Model = BankingSystem.objects.get(Username = AccountDetails.objects.get(UserName = request.user.username))
	_a = Transactions.objects.filter(Username = _Obj)
	_b = ExternalTransactions.objects.filter(Username = _Obj)
	Context = {'BankModel':Model, 'Trans1': _a , 'Trans2':_b}
	return render(request, 'BankingSystem.html',Context)
