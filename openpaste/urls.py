from django.conf.urls import patterns, include, url
from django.contrib import admin
from .api import router

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'openpaste.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'application_openpaste.views.initial_menu', name='HomePage'),
    url(r'^text-inset/', 'application_openpaste.views.send_text_paste', name='HomePage text paste'),
    url(r'^image-inset/', 'application_openpaste.views.send_image_inset', name='HomePage text paste'),
    url(r'^all_inset', 'application_openpaste.views.all_inset', name='All Inset'),
    url(r'^show_inset/-.*-.*', 'application_openpaste.views.show_one_inset', name='Show one inset'),
    url(r'^api/v1/', include(router.urls)),

)
