from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns

from .views import CreateView, DetailsView

# Format suffix patterns: Allow us to specify the data format(JSON, HTML, etc...)
urlpatterns = {
    url(r'^bucketlists/$', CreateView.as_view(), name='create'),
    url(r'^bucketlists/(?P<pk>[0-9]+)/$', DetailsView.as_view(), name='details')
}

urlpatterns = format_suffix_patterns(urlpatterns)
