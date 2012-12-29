from django.conf.urls import patterns, include, url

urlpatterns = patterns('cc.views',
    # Example for polls.
    url(r'^polls/$', 'polls'),
    url(r'^polls/(?P<poll_id>\d+)/$', 'detail'),
    url(r'^polls/(?P<poll_id>\d+)/results/$', 'results'),
    url(r'^polls/(?P<poll_id>\d+)/vote/$', 'vote'),
    
    url(r'^$', 'index'),
)
