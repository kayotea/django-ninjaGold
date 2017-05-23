# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from random import randrange

# Create your views here.

#shows ws the main index page
def index(request):
    #initialize gold amount and activities array in session
    if 'gold' not in request.session:
        request.session['gold'] = 0
    if 'activities' not in request.session:
        request.session['activities'] = []
    return render(request, 'ninja_app/index.html')

#called when user clicks one of the submit forms on main page
def process(request):
    if request.method == "POST":
        #depending on what they clicked
        #user receives different amounts of gold
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
        #add message to session activities array
        #which will be printed on main page
        request.session['activities'].append((sign, money, building))
        print request.session['activities']
    return redirect('/')

