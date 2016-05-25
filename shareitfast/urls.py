from django.conf.urls import url
from sif import views
from django.conf import settings

handler404 = 'sif.views.handler404'
handler500 = 'sif.views.handler404'

urlpatterns = [
    url(r'^$', views.index),
    url(r'^' + settings.MEDIA_URL + '(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
]
