from django.template.loader import get_template
from django.shortcuts import render_to_response
from django.http import HttpResponse,Http404
from django.template import Context, Template,RequestContext,TemplateDoesNotExist 
from django.db import models
from reportlab.pdfgen import canvas
from django.views.generic.simple import direct_to_template
#from blog import User,Article,Tags
import datetime,time
from django.contrib import auth
def hello(request):
	return HttpResponse('hello world')
def nowtime(request):
	now=time.ctime()
	html='<html><body>now: %s</body></html>' % now
	return HttpResponse(html)
def hours_ahead(request, a):
	try:
		add=int(a)
	except ValueError:
		raise Http404()
	dt = datetime.datetime.now() + datetime.timedelta(hours=add)
	html='<html><body>add %s hour(s), it will become %s.</html></body>' % (add, dt)
	return HttpResponse(html)
def current_date(request):
	now=datetime.datetime.now()
	dict={'current_date':now}
	return render_to_response('current.time.html',dict)
#	t=get_template('current.time.html')
#	html=t.render(Context({'current_date': now}))
#	return HttpResponse(html)
def display_meta(request):
     values = request.META.items()
     values.sort()
     html = []
     for k,v in values:
         html.append('<tr><td>%s</td><td>%s</td><tr>' % (k,v))
    # return HttpResponse('<table>%s</table>' % '\n'.join(html))
     ua= request.META['HTTP_USER_AGENT']
     return HttpResponse(ua)
def search_form(request):
        return render_to_response('search_form.html')
def object_list(request, model='Event.html'):
	template_name=model
	return render_to_response(template_name)
def again(request):
	return render_to_response('again.html')
def about(request,a):
	try:
		return direct_to_template(request, template="about/%s.html" % a)
	except TemplateDoesNotExist:
        	raise Http404()
def image(request):
	image_data = open('/home/workhardcc/Pictures/Screenshot from 2012-11-07 11:34:05.png','rb').read()
	return HttpResponse(image_data, mimetype='image/png')
def hello_pdf(request):
    response=HttpResponse(mimetype='application/pdf')
    response['content-Disposition']='attachment; filename=hello.pdf'
    p = canvas.Canvas(response)
    p.drawString(100, 100, "Hello world.")
    p.showPage()
    p.save()
    return response
'''def login(request):
    return render_to_response('again.html')
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)
    if user is not None and user.is_active:
        auth.login(request, user)
        return HttpResponseRedirect("/account/loggedin/")
    else:
        return HttpResponseRedirect("/account/invalid/")
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect("/account/loggedout/")'''
