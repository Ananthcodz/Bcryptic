from django.shortcuts import render,redirect
from .models import creditcard
from accdetails.models import AccountDetails
import random
# Create your views here.
def CCcreate(request):
	if request.method == "POST":


			return redirect('CreditCard')

def CreditCard(request):
	_AccObj = AccountDetails.objects.get(UserName = request.user.username)
	if creditcard.objects.filter(UserName = _AccObj).exists():
		obj = creditcard.objects.filter(UserName = _AccObj)
		Dict = {'Card':obj}
		return render(request, 'CreditCard.html',Dict)
	else:
		if request.method == "POST":
				Data = request.POST
				cardno = cardnumber()
				_cvv = cvv()
				_Obj = creditcard(UserName = _AccObj, credit_card = Data['CreditCard'], Purpose = Data['Purpose'], CardNo = cardno, Firstname =  Data['FirstName'], Lastname =  Data['LastName'], CVV = _cvv, Permitted = False)
				_Obj.save()
				return redirect('CreditCard')
		else:
			return render(request, 'CCcreate.html')

def cardnumber():
	a = ""
	for i in range(0,16):
			a += str(random.randint(0,9))
	_CCs = creditcard.objects.all()
	no = int(a)
	if creditcard.objects.all().exists():
		_CC = creditcard.objects.all()
		for z in _CCs:
			if z.CardNo == no:
				return cardnumber()
			else:
				return no
	else:
		return no
def cvv():
	a = ""
	for i in range(0,3):
			a += str(random.randint(0,9))
	no = int(a)
	if creditcard.objects.all().exists():
		_CC = creditcard.objects.all()
		
		for z in _CC:
			if z.CVV == no:
				return cvv()
			else:
				return no
	else:
		return no