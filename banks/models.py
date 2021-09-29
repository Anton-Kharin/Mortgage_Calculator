from django.db import models
from django.urls import reverse

class Rate(models.Model):
    percent = models.IntegerField(default=1)
    def __str__(self):
        return str(self.percent)


class Bank(models.Model):
    name = models.CharField(max_length=20)
    def __str__(self):
        return self.name
    def absolute_url(self):
        return reverse("banks:bank_detail", args=[self.id])
    def get_rate(self):
        rates = []
        for credit in self.credit_set.all():
            for rate in credit.rates.all():
                if rate not in rates:
                    rates.append(rate)
            return rates

class Credit(models.Model):
    banks = models.ForeignKey(Bank, on_delete=models.CASCADE)
    rates = models.ManyToManyField(Rate)
    max_loan = models.IntegerField(default=0)
    min_down_payment = models.IntegerField(default=0)
    loan_term = models.IntegerField(default=0)

    def __str__(self):
        return str(self.id)
    def absolute_url(self):
        return reverse("banks:credit_detail", args=[self.id])
