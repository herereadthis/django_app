from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    # Examples:
    # url(r'^$', 'django_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    # The url() function is passed four arguments.
    # required - Regex, to match URL patterns
    # required - view, to call the specified view function with an HttpRequest
    # object as the first argument and any "captured" values from the regular
    # expression as other arguments.
    # optional - kwargs, which can be passed in a dictionary
    # optional - name - allows you to refer to it unambiguously elseware
    url(r'^polls/', include('polls.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
