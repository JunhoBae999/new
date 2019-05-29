from django.shortcuts import render
from .models import Portfolio

def home(request) :
    portfolios = Portfolio.objects
    return render(request,'portfolio.html',{'portfolios':portfolios})
