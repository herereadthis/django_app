from django.conf.urls import patterns, url
# import views from polls app
# To get a URL to a view, Django uses what are known as 'URLconfs' A URLconf
# maps URL patterns (regex) to views
from polls import views

# Generic view
urlpatterns = patterns(
    '',
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
    url(
        r'^(?P<pk>\d+)/results/$',
        views.ResultsView.as_view(),
        name='results'
    ),
    url(r'^(?P<poll_id>\d+)/vote/$', views.vote, name='vote'),
)

'''
# This is doing the long form way.
urlpatterns = patterns(
    '',
    # example: /polls/
    url(r'^$', views.index, name='index'),
    # example: /polls/5/
    # If the URL matches this, it will run the detail method in views.py
    # at django_project/urls.py will pass anything that comes after '/polls/*'
    # then whatever regex matches calls the appropriate view method.
    # anything inside a parenthesis captures the matching text and sends it as
    # an argument to view function: ?P<poll_id>
    # we can use name='detail' to use {% url %} template tag
    url(r'^(?P<poll_id>\d+)/$', views.detail, name='detail'),
    # example: /polls/5/results/
    url(r'^(?P<poll_id>\d+)/results/$', views.results, name='results'),
    # # example: /polls/5/vote/
    url(r'^(?P<poll_id>\d+)/vote/$', views.vote, name='vote'),
)
'''
