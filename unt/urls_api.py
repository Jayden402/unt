from django.conf.urls import url
from django.urls import include
from rest_framework import routers

router = routers.SimpleRouter()

urlpatterns = router.urls


urlpatterns += [
    url(r'^', include('packages.qrcode.urls')),
]
