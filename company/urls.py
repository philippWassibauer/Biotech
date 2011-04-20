from django.conf import settings
from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template
from django.contrib import admin
from django.contrib.auth.models import User
admin.autodiscover()
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = patterns("",
    url(r'^', include('cms.urls')),
)

if settings.SERVE_MEDIA:
    urlpatterns += staticfiles_urlpatterns()

