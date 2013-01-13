# Create your views
from django.http import HttpResponseRedirect,HttpResponse
from django.shortcuts import render_to_response
from django import forms
from blog.form import ContactForm
from django.views.decorators.csrf import csrf_protect
def login(request):
    if request.user.is_authenticated():  
        return  HttpResponse('xadasda') 
    if request.method == 'POST':
	username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None and user.is_active:
	    auth.login(request, user)
            return HttpResponseRedirect("/account/loggedin/")
        else:
            return HttpResponseRedirect("/account/invalid/")
    return render_to_response('login.html')
def firstpage(request):
    return render_to_response('Event.html')
def faildpage(request):
    return render_to_response('thanks.html')
