from django.conf.urls import url

from packages.qrcode.views import LinkModelViewSet

urlpatterns = [

    url(r'^input_link/$', LinkModelViewSet.as_view({'post': 'input_link'})),
    url(r'^get_image/$', LinkModelViewSet.as_view({'get': 'get_image'})),

]