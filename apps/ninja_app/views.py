# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from random import randrange

# Create your views here.
def index(request):
    if 'gold' not in request.session:
        request.session['gold'] = 0
    if 'activities' not in request.session:
        request.session['activities'] = []
    return render(request, 'ninja_app/index.html')

def process(request):
    if request.method == "POST":
        if request.POST['building'] == "farm":
            money = randrange(10,21)
        elif request.POST['building'] == "cave":
            money = randrange(5,11)
        elif request.POST['building'] == "house":
            money = randrange(2,6)
        elif request.POST['building'] == "casino":
            money = randrange(-50,51)
        
        building = request.POST['building']
        request.session['gold'] += money
        if money >= 0:
            sign = 1
        else:
            sign = -1
        money = abs(money)
        request.session['activities'].append((sign, money, building))
        print request.session['activities']
    return redirect('/')

