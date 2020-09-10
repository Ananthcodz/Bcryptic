from django.shortcuts import render,redirect
from .models import Loans
from accdetails.models import AccountDetails
# Create your views here.
def _Loans(request):
	_Obj = AccountDetails.objects.get(UserName = request.user.username)
	if request.method == "POST":
		Data = request.POST
		instance = Loans(purpose = Data['Purpose'], mobile_number = Data['Mobile'],DOB = Data['DOB'], Location = Data['Location'], collateral = Data['collateral'], Recipent = AccountDetails.objects.get(UserName = request.user.username), Amount= Data['Amount'], Interest= Data['Interest'])
		instance.save()
		return redirect('Loans')
	else:
		if Loans.objects.filter(Recipent = _Obj).exists():
			obj = Loans.objects.get(Recipent = _Obj)
			Dict = {'Loan': obj}
			return render(request, '_Loans.html', Dict)
		return render(request, 'Loans.html')
	