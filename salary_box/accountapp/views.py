from django.shortcuts import redirect, render
from accountapp.forms import *
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth import logout
from django.contrib import messages #import messages


# Create your views here.


def signup(request):
    if request.method == "POST":
        form = signupform(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            messages.success(request, f'Account created successfully!')
            return redirect('/')
        else:
            messages.error(request, f'Something went worng!, Please try again')
            return redirect('/auth/signup')

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
         if user:
                auth_login(request, user)
                messages.success(request, f'Login successfully!')
                return redirect('/') 
         else:
             messages.error(request, f'Something went worng!, Please try again')
             return redirect('/')
        else:
            messages.error(request, f'Something went worng!, Please try again')
            return redirect('/auth/login')

    else:
        form = loginForm()
        ctx = {'form':form}
        return render(request, 'account/login.html', ctx)
        


def log_out(request):
    logout(request)
    messages.success(request, f'Logout successfully!')
    return redirect('/')