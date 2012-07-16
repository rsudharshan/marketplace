from django.conf.urls.defaults import patterns, include, url
from marketplace.views import hello
from marketplace.views import quiz_guess
from marketplace.views import home
from marketplace.views import signup
from django.views.static import *
from marketplace.views import update,logout,sell,search
from marketplace.views import authenticate
from marketplace.views import updatepro,updatesell
from django.conf import settings
from settings import DEBUG
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
PRDIMG_ROOT="%s%s",settings.STATIC_ROOT,"prdimg/"
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'trav.views.home', name='home'),
    # url(r'^trav/', include('trav.foo.urls')),
url(r'^hello/',hello),
url(r'^home/',home),
url(r'^update/',update),
url(r'^updatepro/',updatepro),
url(r'^verify/',authenticate),
url(r'^signup/$',signup),
url(r'^sell/$',sell),
url(r'^updatesell/',updatesell),
url(r'^logout/$',logout),

# Uncomment the admin/doc line below to enable admin documentation:
url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
url(r'^static/prdimg/(?P<path>.*)$', 'django.views.static.serve', {'document_root': PRDIMG_ROOT}),
url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
url(r'^search/(?P<search>\w+)/$',search,name='search'),


url(r'^test/(?P<user_id>\w+)/$',quiz_guess,name='quiz_guess'),

# Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),
)
