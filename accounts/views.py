from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm
from django.views.decorators.http import require_POST

from accounts.forms import UserLoginForm

def login(request) : 
    if request.method=='POST' :
        form = AuthenticationForm(request, request.POST)
        if form.is_valid() :
            auth_login(request, form.get_user())
        return redirect('meal:index')
    else :
        form = UserLoginForm()
        context = {
            'form' : form,
        }
        return render(request, 'accounts/login.html', context)


@require_POST
def logout(request) :
    auth_logout(request)
    return redirect('accounts:login')
