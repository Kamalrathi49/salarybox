from django.shortcuts import redirect, render
from accountapp.forms import *
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth import logout

# Create your views here.


def signup(request):
    if request.method == "POST":
        form = signupform(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('/')

    else:    
        form = signupform()
        ctx = {'form': form}
        return render(request, 'account/signup.html', ctx)


def log_in(request):
    if request.method == 'POST':
        form = loginForm(request.POST)
        if form.is_valid():
         username = form.cleaned_data['username']
         password = form.cleaned_data['password']
         user = authenticate(request, username = username, password=password)
         print('------------------------->>>>>>>', user)
         if user:
             auth_login(request, user)
             return redirect('/') 
         else:
             return redirect('/auth/login')
        else:
            return redirect('/login')
    
    else:
        form = loginForm()
        ctx = {'form':form}
        return render(request, 'account/login.html', ctx)
        


def log_out(request):
    logout(request)
    return redirect('/')