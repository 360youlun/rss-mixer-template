from django.conf.urls import patterns, url
from mixer.views import MixerView

urlpatterns = patterns('',
    url(r'^$', MixerView.as_view(), name='mixer'),
)
