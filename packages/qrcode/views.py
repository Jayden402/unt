from django.core.files.uploadedfile import UploadedFile, SimpleUploadedFile
from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from packages.qrcode.models import Link
from packages.qrcode.utils import make_qrcode


class LinkModelViewSet(ModelViewSet):

    permission_classes = ()

    def input_link(self, request):
        data = [
            {'qrcode': 'https://c.weixin.com/g/rEialNbM4Z4mX4T5', 'name': 'wx_group1.png'},
            {'qrcode': 'https://c.weixin.com/g/k873XT5RpymvPL13', 'name': 'wx_group2.png'},
            {'qrcode': 'https://c.weixin.com/g/FU3EH-Glae_S7FBR', 'name': 'wx_group3.png'},
            {'qrcode': 'https://c.weixin.com/g/xZ8VOOv5YTFlXNro', 'name': 'wx_group4.png'},
            {'qrcode': 'https://c.weixin.com/g/yOgpqpvsOpjnl28Z', 'name': 'wx_group5.png'},
            {'qrcode': 'https://c.weixin.com/g/fZZISDFfLxzE98hV', 'name': 'wx_group6.png'},
            {'qrcode': 'https://c.weixin.com/g/5t4UTZamObqhrEh_', 'name': 'wx_group7.png'},
            {'qrcode': 'https://c.weixin.com/g/5Z6GYW1nXqlWQow2', 'name': 'wx_group8.png'},
            {'qrcode': 'https://c.weixin.com/g/lE_i1DGDicaCAvKg', 'name': 'wx_group9.png'},
            {'qrcode': 'https://c.weixin.com/g/4GevOiShMhyNbz5B', 'name': 'wx_group10.png'},
        ]
        Link.objects.bulk_create(Link(**item) for item in data)
        return Response(data={'success': '插入成功！'}, status=status.HTTP_200_OK)

    def get_image(self, request):
        id = self.request.query_params.get('id', None)
        link = Link.objects.filter(id=id).first()
        if link.image:
            return Response(data={'url': link.image.url}, status=status.HTTP_200_OK)
        image = make_qrcode(link.name, link.qrcode)
        dm_file = SimpleUploadedFile(link.name, image, content_type='image/png')
        link.image = dm_file
        link.save()
        return Response(data={'url': link.image.url}, status=status.HTTP_200_OK)
