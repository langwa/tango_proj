from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin

from registration.backends.simple.views import RegistrationView

# Create a new class that redirects the user to the index page, if successful at logging
class MyRegistrationView(RegistrationView):
    def get_success_url(self, request, user):
        return '/rango/'

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'tango_proj.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^polls/', include('polls.urls', namespace='polls')),
    url(r'^rango/', include('rango.urls', namespace='rango')),
    url(r'^accounts/register/$', MyRegistrationView.as_view(), name='registration_register'),
    url(r'^accounts/', include ('registration.backends.simple.urls', namespace = 'accounts')),

)

if settings.DEBUG:
    urlpatterns += patterns('django.views.static',

        url(r'^media/(?P<path>.*)', 'serve', {'document_root': settings.MEDIA_ROOT}),

    )
