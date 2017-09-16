from django.conf.urls import url
from django.contrib import admin
from home.views import home
from archive.views import archive
from articles.views import article

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', home),
    url(r'^archive/$', archive),
    url(r'^(?P<slug>[-\w]+)/$', article),
]
