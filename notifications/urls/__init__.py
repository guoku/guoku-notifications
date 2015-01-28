from django.conf.urls import url, patterns, include

urlpatterns = patterns(
    'apps.notifications.views',
    url(r'^$', 'messages', name='web_messages'),
)


__author__ = 'edison7500'
