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
            print('--------------->>',user)
            return redirect('/')

    else:    
        form = signupform()
        ctx = {'form': form}
        return render(request, 'account/signup.html', ctx)

def log_out(request):
    logout(request)
    return redirect('/')