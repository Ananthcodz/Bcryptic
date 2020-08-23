"""accounts URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from accdetails.views import *
from Loans.views import _Loans
from creditcards.views import * 
from BankingSystem.views import * 
from transactions.views import *
from externalbanktrans.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Home, name = "Home"),
    path('Login/', loginPage, name = "Login"),
    path('Register/', registerPage, name = "Register"),
    path('Logout/', logoutUser, name = "logout"),
    path('CreditCard/',CreditCard, name = "CreditCard"),
    path('Loan/',_Loans, name = "Loans"),
    path('Contact/',Contact, name = "Contact"),
    path('BankingSystem/',Banking_System, name = "BankingSystem"),
    path('Transact/', Transact, name = "Transact"),
    path('ExtTransact/', ExtTransact, name = "ExtBank")
    
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)