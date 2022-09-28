from django.shortcuts import render
from random import randint

def indexpage(request):

    if request.method == 'POST':

        username = request.POST['tarea']
        username = len(username.split())
    else:
        username = 0
    return render(request, 'index.html', {"length": username})

def loadnewpage(request):
    mypass = ''
    passwords = []

    newpass = []
    if request.method == 'POST':
        print('The request is a post request')
        length = request.POST['plength']
        i = 0
        
        while i < 5:
            generate(length, mypass, passwords)
            i = i + 1

        for p in passwords:
            if len(p) == int(length):
                newpass.append(p)
    
            
    return render(request, 'page.html', {'context': newpass})

def generate(length, mypass, d = []):
    
    i = 1
    while i <= int(length):
        a = randint(48, 122)

        if a >= 48 and a <= 57 or a >= 63 and a <= 90 or a >= 97 and a <= 122:

            mypass = mypass + chr(a)
            i = i + 1
            d.append(mypass)
        elif (a >= 58 <= 62) or (a >= 91 <= 96):
            continue



