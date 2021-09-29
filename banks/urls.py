from django.urls import path
from . import views

app_name = 'banks'

urlpatterns = [
    path('', views.index, name="index"),
    path('add/', views.add, name='add'),
    path('change/<int:pk>', views.change, name='change'),
    path('delete/<int:pk>', views.delete),
    path('bank/<int:pk>', views.BankDetailView.as_view(), name='bank_detail'),
    path('credit/<int:pk>', views.CreditDetailView.as_view(), name='credit_detail'),
    path('credit/<int:pk>', views.calculate),
]