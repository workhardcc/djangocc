from django.conf.urls import patterns, include, url
from mysite.view import hello,nowtime,hours_ahead,current_date,display_meta,models,object_list,again,about,image,hello_pdf
from django.views.generic.simple import direct_to_template
from books.views import search,search_form
from contact.view import contact1,thanks
from newblog.views import login,firstpage,faildpage,register,logout
#from django.contrib.auth.views import logout
from django.contrib import admin
admin.autodiscover()
from books.models import Publisher,Book
from django.views.generic import list_detail
from django.conf.urls.defaults import *
#from django.contrib.auth.views 
from django.views.decorators.cache import cache_page
publisher_info={ 'queryset': Publisher.objects.all(), 'template_name': 'publisher_list_page.html','template_object_name':'publisher','extra_context': {'book_list':Book.objects.all}}
book_info={'queryset': Book.objects.order_by('id'),'template_name':'book.html',}
urlpatterns = patterns('',
#    ('^$', hello),
    (r'^time/$', nowtime),
    (r'^time/plus/(\d{1,2})/$', hours_ahead),
    (r'^time/birthday/$',hours_ahead,{'a':1}),
    (r'^current_date/$',current_date),
    (r'^display_meta/$',display_meta),
    (r'^search-form/$',search_form),
    (r'^search/$',search),
    (r'^contact/$',contact1),
    (r'^contact/thanks/$',thanks),
    (r'^xx/$',again),
    (r'^events/$', object_list, {'model': 'Event.html'}),
    (r'^blog/entries/$', object_list, {'model': 'BlogEntry.html'}),
    (r'^add/$', object_list),
    (r'^thank/$',direct_to_template,{'template':'thanks.html'}),
    (r'^about/(\w+)/$', about),
    (r'^publishers/$',list_detail.object_list,publisher_info),
    (r'^book/$',list_detail.object_list,book_info),
    (r'^png/$',image),
    (r'^pdf/$',hello_pdf),
   # (r'^feed/(?P<url>.*)/$','django.contrib.syndication.views.feed',{'feed_dict':feeds}),
    (r'^accounts/login/$', login),
    (r'^accounts/logout/$',logout),
    (r'^account/loggedin/$',firstpage),
    (r'^account/invalid/$',faildpage),
    (r'^account/register/$',register),
    (r'^admin/',include(admin.site.urls)),
)
