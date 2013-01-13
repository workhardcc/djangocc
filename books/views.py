# Create your views here.
from django.shortcuts import render_to_response
from django.http import HttpResponse,Http404
from books.models import Book
def search_form(request):
	return render_to_response('search_form.html')
#def search(request):
#	if 'a' in request.GET:
#		message = 'you searched for: %r' % request.GET['a']
#	else:
#		message = 'you submitted an empty form'
#	return HttpResponse(message)
def search(request):
	errors=[]
   	if 'q' in request.GET:
        	q = request.GET['q']
        	if not q:
			errors.append('Enter a search term.')
		elif len(q)>20:
			errors.append('please enter at most 20 characters')
        	else:
            		books = Book.objects.filter(title__icontains=q)
            		return render_to_response('search_results.html',{'books': books, 'query': q})
    	return render_to_response('search_form.html',{'errors': errors})

#	if 'q' in request.GET and request.GET['q']:
#		q=request.GET['q']
#		books=Book.objects.filter(title__icontains=q)
#		return render_to_response('search_results.html',
#	            {'books': books, 'query': q})
#  	else:
#		return render_to_response('search_form.html',{'error':True})
