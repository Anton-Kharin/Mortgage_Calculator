from django.http import HttpResponseRedirect
from django.http import HttpResponseNotFound
from django.shortcuts import render
from .models import *
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

def index(request):
    context = {
        'banks' : Bank.objects.all(),
    }
    return render(request, "banks/index.html", context)
def add(request):
    name = request.POST.get('name')
    if name:
        newbank = Bank(name=name)
        newbank.save()
    return HttpResponseRedirect(reverse('banks:index'))
def change(request, pk):
    bank = Bank.objects.get(pk=pk)
    if request.method == 'GET':
        return render(request, "banks/change.html", {'bank': bank})
    elif request.method == "POST":
        bank.name = request.POST.get('name')
        bank.save()
        return HttpResponseRedirect(reverse('banks:index'))
    else:
        HttpResponseRedirect(reverse('banks:index'))
def delete(request, pk):
    try:
        bank = Bank.objects.get(pk=pk)
        bank.delete()
        return HttpResponseRedirect(reverse("banks:index"))
    except Bank.DoesNotExist:
        return HttpResponseNotFound("<h2>Bank not found</h2>")

class BankDetailView(DetailView):
    model = Bank

class CreditDetailView(DetailView):
    model = Credit

def calculate(request, pk):
    credit = Credit.objects.get(pk=pk)
    if request.action == "#":
        P = credit.max_loan - credit.max_loan * credit.min_down_payment / 100
        month = credit.loan_term * 12

        for m in range(1, month + 1):
            payment = round(P * (1 + credit.rates / (12 * 100)) ** m, 2)
            print(f'm:{m % 12:0>2}) y:{m // 12:0>2}) {payment:,.2f}')
    else:
        HttpResponseRedirect(reverse('banks:index'))