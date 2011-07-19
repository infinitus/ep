from django.conf.urls.defaults import *
from django.contrib import admin
admin.autodiscover()

# Django-related/Experimental
urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),
)


# EP main web view
urlpatterns += patterns('ep.carparks.views',
        (r'^live/$', 'measurements'),
        (r'^live/(?P<req_cluster>\d{1,2})/$', 'show_data'),
        (r'^live/(?P<req_cluster>\d{1,2})/(?P<req_node>\d{1,2})/$', 'show_data'),
        (r'^m/$', 'mobile_ui_main'),
        (r'^m/(?P<req_cluster>\d{1,2})/$', 'mobile_ui_cluster_overview'),
        )


# Route API calls to api/urls.py
urlpatterns += patterns('',
        (r'^api/', include('ep.api.urls')),
        )
