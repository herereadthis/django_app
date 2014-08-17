from django.conf.urls import patterns, url
# import views from polls app
# To get a URL to a view, Django uses what are known as 'URLconfs' A URLconf
# maps URL patterns (regex) to views
from polls import views

urlpatterns = patterns(
    '',
    # example: /polls/
    url(r'^$', views.index, name='index'),
    # example: /polls/5/
    # If the URL matches this, it will run the detail method in views.py
    url(r'^(?P<poll_id>\d+)/$', views.detail, name='detail'),
    # example: /polls/5/results/
    url(r'^(?P<poll_id>\d+)/results/$', views.results, name='results'),
    # # example: /polls/5/vote/
    url(r'^(?P<poll_id>\d+)/vote/$', views.vote, name='vote'),
)
