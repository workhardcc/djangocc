from django.http import HttpResponseRedirect,HttpResponse
from django.shortcuts import render_to_response
from django import forms
from newblog.forms import CcForm
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
def login(request):
#    if request.user.is_authenticated():
#        return  HttpResponse('xadasda')
    if request.method == 'POST':
	form = CcForm(request.POST)
        username = request.POST.get('USERNAME', '')
        password = request.POST.get('PASSWORD', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None and user.is_active:
            auth.login(request, user)
            return HttpResponseRedirect("/account/loggedin/")
        else:
            return HttpResponseRedirect("/account/invalid/")
    else :
	form = CcForm()
    return render_to_response('login.html',{'form':form})

def firstpage(request):
    return render_to_response('successful.html')
def faildpage(request):
    return render_to_response('invalid.html')
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            return HttpResponseRedirect("")
    else:
        form = UserCreationForm()
    return render_to_response("register.html", {
        'form': form,
    })
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect("/account/loggedout/")
