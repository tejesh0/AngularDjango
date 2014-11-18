from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView
from authentication.views import UserCreateView

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'djangoAngular.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),

                       url(r'^admin/', include(admin.site.urls)),
                       url('^api/v1/users/$', UserCreateView.as_view(), name='user-create'),

                       url(r'^', TemplateView.as_view(template_name='static/index.html')),
)

