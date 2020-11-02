from django.db import models

# Create your models here.


class Link(models.Model):
    qrcode = models.CharField(verbose_name='图片链接', max_length=255)
    name = models.CharField(verbose_name='图片名称', max_length=30, null=True, blank=True)
    image = models.ImageField(verbose_name='图片路径', null=True, blank=True)

    class Meta:
        db_table = 'tb_link'
        verbose_name = '链接'
        verbose_name_plural = verbose_name
