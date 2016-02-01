from django.conf.urls import patterns, include, url
from django.contrib import admin
from .api import router

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'openpaste.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'application_openpaste.views.start_page', name='HomePage'),
    url(r'^all_inset', 'application_openpaste.views.all_inset', name='All Inset'),
    url(r'^api/v1/', include(router.urls)),

)
