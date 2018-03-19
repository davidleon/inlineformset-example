from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings


handler500 = 'utils.views.server_error'

urlpatterns = []

# Debug/Development URLs
if settings.DEBUG is True:  # pragma: no cover
    urlpatterns += [
        url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    ]

# Admin Site
admin.autodiscover()

# Includes
urlpatterns += [
    url(r'^admin/', admin.site.urls),
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'', include('books.urls')),
]
