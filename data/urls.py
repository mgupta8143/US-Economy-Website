from django.urls import path
from . import views

urlpatterns = [
    path('', views.about, name = 'about'),
    path('exchange-rates/', views.exchange_rates, name = "exchange-rates"),
    path('data-rates/', views.data_rates, name = "data-rates"),
    path('unemployment/', views.unemployment, name = "unemployment"),
    path('income/', views.income, name = "income"),
    path('GDP/', views.gdp, name = "GDP"),
    path('government-spending/', views.government_spending, name = "government-spending"),
    path('COVID-19/', views.covid, name = "covid"),
  ]
