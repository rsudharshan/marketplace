from django.conf.urls.defaults import patterns, include, url
from marketplace.views import hello
from marketplace.views import quiz_guess
from marketplace.views import home
from marketplace.views import signup,show_object
from django.views.static import *
from marketplace.views import update,logout
from marketplace.views import authenticate
from marketplace.views import updatepro
from django.conf import settings
from settings import DEBUG
from django.views.generic.simple import direct_to_template
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
imgroot=settings.MEDIA_ROOT,"/prdimg"
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'trav.views.home', name='home'),
    # url(r'^trav/', include('trav.foo.urls')),
url(r'^hello/',hello),
url(r'^home/',home),
url(r'^update/',update),
url(r'^show/',show_object),

url(r'^updatepro/',updatepro),
url(r'^verify/',authenticate),
url(r'^signup/$',signup),
url(r'^logout/$',logout),

# Uncomment the admin/doc line below to enable admin documentation:
url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
url(r'^media/prdimg/(?P<path>.*)$', 'django.views.static.serve', {'document_root': imgroot}),
url(r'^test/(?P<user_id>\d+)/$',quiz_guess,name='quiz_guess'),
# Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),
)
