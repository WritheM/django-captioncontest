from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Comment the admin/doc line below to disable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Comment the next line to disable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^admin', include(admin.site.urls)),
    
    # This is used for login/logout for the social apps stuff, facebook predominiatly
    url(r'^user/', include('social_auth.urls')),
        
    url(r'^cc/', include('cc.urls')),
)
